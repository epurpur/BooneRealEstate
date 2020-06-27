
import psycopg2
import pandas as pd
import geopandas as gpd
import numpy as np
from sqlalchemy import create_engine


######why are zones overwriting eachother?

postgres_connection = psycopg2.connect(host="localhost", port=5432, database="BRE_2019_Test", user="postgres", password="battlebot")


all_2019_parcels = gpd.read_postgis(('SELECT * FROM public."All_Parcels_2019" '), postgres_connection)

zone_1a_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1a" AS z1a, public."homes_df" AS res WHERE st_intersects(z1a.geom, res.geom)'), postgres_connection)
zone_1b_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1b" AS z1b, public."homes_df" AS res WHERE st_intersects(z1b.geom, res.geom)'), postgres_connection)
zone_1c_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1c" AS z1c, public."homes_df" AS res WHERE st_intersects(z1c.geom, res.geom)'), postgres_connection)
# zone_1d_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1d" AS z1d, public."homes_df" AS res WHERE st_intersects(z1d.geom, res.geom)'), postgres_connection)


all_2019_parcels['zone_checker'] = zone_1a_parcels['parno'].isin(all_2019_parcels['parno'])
all_2019_parcels.loc[all_2019_parcels['zone_checker'] == True, 'Zone'] = 'Zone1a'
    
all_2019_parcels['zone_checker'] = zone_1b_parcels['parno'].isin(all_2019_parcels['parno'])
all_2019_parcels.loc[all_2019_parcels['zone_checker'] == True, 'Zone'] = 'Zone1b'

all_2019_parcels['zone_checker'] = zone_1c_parcels['parno'].isin(all_2019_parcels['parno'])
all_2019_parcels.loc[all_2019_parcels['zone_checker'] == True, 'Zone'] = 'Zone1c'

# all_2019_parcels['zone_checker'] = zone_1d_parcels['parno'].isin(all_2019_parcels['parno'])
# all_2019_parcels.loc[all_2019_parcels['zone_checker'] == True, 'Zone'] = 'Zone1d'







def property_type_column(df):
    """creates property type column for dataframe and labels vacant land property types as such"""

    #create 'Property Type' column and populate with true/false  alues
    df['Property Type'] = df['landval'] == df['parval']
    
    #change true/false values to 'Vacant Land' or no value. There are 95593 vacant land parcels.
    df.loc[(df['Property Type'] == True), 'Property Type'] = 'Vacant Land'
    df.loc[(df['Property Type'] == False), 'Property Type'] = ''
    
    
    #Label others from Watauga County using parusedesc. Now there are 95783 vacant land parcels (added about 200 parcels)
    df.loc[(df['parusedesc'] == 'RESIDENTIAL VACANT'), 'Property Type'] = 'Vacant Land'
    df.loc[(df['parusedesc'] == 'AGRICULTURAL-VACANT'), 'Property Type'] = 'Vacant Land'
    df.loc[(df['parusedesc'] == 'APARTMENT LAND VACANT'), 'Property Type'] = 'Vacant Land'
    df.loc[(df['parusedesc'] == 'COMMERCIAL LAND VACANT'), 'Property Type'] = 'Vacant Land'
    df.loc[(df['parusedesc'] == 'INDUSTRIAL TRACT VACANT'), 'Property Type'] = 'Vacant Land'
    df.loc[(df['parusedesc'] == 'UTILITY VACANT LAND'), 'Property Type'] = 'Vacant Land'
    
    return df


def vacant_land_filters(vacant_land_df):
    """Takes the vacant land dataframe and filters all vacant land.
    
    Filter 1: vacant land parcels 1-10 acres and >$100k value.
    Filter 2: vacant land parcels >10 acres and >$200k value
    
    Labels 'filter' column as either 'Filter 1' or 'Filter 2'
    
    Lastly, combines filter 1 and filter into final vacant land df
    """
    
    filter1 = vacant_land_df.loc[(vacant_land_df['gisacres'] > 1) & (vacant_land_df['gisacres'] < 10) & (vacant_land_df['parval'] > 100000)]
    filter1['Filter'] = 'Filter 1'
    filter2 = vacant_land_df.loc[(vacant_land_df['gisacres'] > 10) & (vacant_land_df['parval'] > 200000)]
    filter2['Filter'] = 'Filter 2'
    
    #we are left with 4787 vacant land parcels
    vacant_land_df = pd.concat([filter1, filter2])

    return vacant_land_df
    

def residential_parcels(df):
    """According to parusedesc, labels 'property type' column as residential"""
    
    #These are the known residential parcel use codes from Watauga County only. I am re-labeling these as 'Home'
    df.loc[df['parusedesc'] == 'RESIDENTIAL 1 FAMILY', 'Property Type'] = 'Home'
    df.loc[df['parusedesc'] == 'RESIDENTIAL 2 FAMILY', 'Property Type'] = 'Home'
    df.loc[df['parusedesc'] == 'RESIDENTIAL 3 FAMILY', 'Property Type'] = 'Home'
    df.loc[df['parusedesc'] == 'RESIDENTIAL STRUCTURE ON COMMERCIAL LAND', 'Property Type'] = 'Home'
    df.loc[df['parusedesc'] == 'RESIDENTIAL UNDER CONSTRUCTION', 'Property Type'] = 'Home'
    df.loc[df['parusedesc'] == 'RESIDENTIAL UNDER CONSTRUCTION/LONG TERM', 'Property Type'] = 'Home'
 
    #all other parcels will be given the Property Type value of 'Home / Potentially not residential'. This includes a lot of non-residential properties but these will be filtered out later
    df.loc[df['Property Type'] == '', 'Property Type'] = 'Home / Potentially Not Residential'
    
    return df
    

def zone_6a_vacant_land_filters(vacant_land_df):
    """These are different vacant land filters, especially for zone 6a as this is Joel's territory
    
    Filter 1: vacant land parcels > 15 acres of any value
    Filter 2: vacant land parcels < 15 acres and > $100k value
    
    """
    
    filter1 = vacant_land_df.loc[(vacant_land_df['gisacres'] > 15)]
    filter2 = vacant_land_df.loc[(vacant_land_df['gisacres'] < 15) & (vacant_land_df['parval'] > 100000)]
    
    vacant_land_df = pd.concat([filter1, filter2])
    
    return vacant_land_df


def create_zone_column(df):
    """This will take in the all_2019_parcels dataframe and create the 'Zone' column, assigning a label
    in that column to the corresponding Zone each parcel belongs to (ex: 1a, 1b, 4c, etc). This is done using a 
    database query in geopandas and some pandas  dataframe manipulation."""
    
    postgres_connection = psycopg2.connect(host="localhost", port=5432, database="BRE_2019_Test", user="postgres", password="battlebot")

    #make database queries to select all parcels from each zone
    zone_1a_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1a" AS z1a, public."homes_df" AS res WHERE st_intersects(z1a.geom, res.geom)'), postgres_connection)
    zone_1b_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1b" AS z1b, public."homes_df" AS res WHERE st_intersects(z1b.geom, res.geom)'), postgres_connection)
    zone_1c_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1c" AS z1c, public."homes_df" AS res WHERE st_intersects(z1c.geom, res.geom)'), postgres_connection)
    zone_1d_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1d" AS z1d, public."homes_df" AS res WHERE st_intersects(z1d.geom, res.geom)'), postgres_connection)
    zone_1e_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1e" AS z1e, public."homes_df" AS res WHERE st_intersects(z1e.geom, res.geom)'), postgres_connection)
    zone_1f_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1f" AS z1f, public."homes_df" AS res WHERE st_intersects(z1f.geom, res.geom)'), postgres_connection)
    zone_1g_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1g" AS z1g, public."homes_df" AS res WHERE st_intersects(z1g.geom, res.geom)'), postgres_connection)
    zone_1h_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1h" AS z1h, public."homes_df" AS res WHERE st_intersects(z1h.geom, res.geom)'), postgres_connection)
    zone_1i_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1i" AS z1i, public."homes_df" AS res WHERE st_intersects(z1i.geom, res.geom)'), postgres_connection)
    zone_1j_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone1j" AS z1j, public."homes_df" AS res WHERE st_intersects(z1j.geom, res.geom)'), postgres_connection)
    # zone_2a_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone2a" AS z2a, public."homes_df" AS res WHERE st_intersects(z2a.geom, res.geom)'), postgres_connection)
    # zone_2b_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone2b" AS z2b, public."homes_df" AS res WHERE st_intersects(z2b.geom, res.geom)'), postgres_connection)
    # zone_2c_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone2c" AS z2c, public."homes_df" AS res WHERE st_intersects(z2c.geom, res.geom)'), postgres_connection)
    # zone_2d_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone2d" AS z2d, public."homes_df" AS res WHERE st_intersects(z2d.geom, res.geom)'), postgres_connection)
    # zone_2e_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone2e" AS z2e, public."homes_df" AS res WHERE st_intersects(z2e.geom, res.geom)'), postgres_connection)
    # zone_2f_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone2f" AS z2f, public."homes_df" AS res WHERE st_intersects(z2f.geom, res.geom)'), postgres_connection)
    # zone_2g_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone2g" AS z2g, public."homes_df" AS res WHERE st_intersects(z2g.geom, res.geom)'), postgres_connection)
    # zone_2h_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone2h" AS z2h, public."homes_df" AS res WHERE st_intersects(z2h.geom, res.geom)'), postgres_connection)
    # zone_2i_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone2i" AS z2i, public."homes_df" AS res WHERE st_intersects(z2i.geom, res.geom)'), postgres_connection)
    # zone_2j_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone2j" AS z2j, public."homes_df" AS res WHERE st_intersects(z2j.geom, res.geom)'), postgres_connection)
    # zone_3a_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone3a" AS z3a, public."homes_df" AS res WHERE st_intersects(z3a.geom, res.geom)'), postgres_connection)
    # zone_3b_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone3b" AS z3b, public."homes_df" AS res WHERE st_intersects(z3b.geom, res.geom)'), postgres_connection)
    # zone_3c_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone3c" AS z3c, public."homes_df" AS res WHERE st_intersects(z3c.geom, res.geom)'), postgres_connection)
    # zone_3d_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone3d" AS z3d, public."homes_df" AS res WHERE st_intersects(z3d.geom, res.geom)'), postgres_connection)
    # zone_3e_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone3e" AS z3e, public."homes_df" AS res WHERE st_intersects(z3e.geom, res.geom)'), postgres_connection)
    # zone_3f_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone3f" AS z3f, public."homes_df" AS res WHERE st_intersects(z3f.geom, res.geom)'), postgres_connection)
    # zone_3g_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone3g" AS z3g, public."homes_df" AS res WHERE st_intersects(z3g.geom, res.geom)'), postgres_connection)
    # zone_4a_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone4a" AS z4a, public."homes_df" AS res WHERE st_intersects(z4a.geom, res.geom)'), postgres_connection)
    # zone_4b_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone4b" AS z4b, public."homes_df" AS res WHERE st_intersects(z4b.geom, res.geom)'), postgres_connection)
    # zone_4c_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone4c" AS z4c, public."homes_df" AS res WHERE st_intersects(z4c.geom, res.geom)'), postgres_connection)
    # zone_4d_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone4d" AS z4d, public."homes_df" AS res WHERE st_intersects(z4d.geom, res.geom)'), postgres_connection)
    # zone_4e_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone4e" AS z4e, public."homes_df" AS res WHERE st_intersects(z4e.geom, res.geom)'), postgres_connection)
    # zone_4f_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone4f" AS z4f, public."homes_df" AS res WHERE st_intersects(z4f.geom, res.geom)'), postgres_connection)
    # zone_4g_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone4g" AS z4g, public."homes_df" AS res WHERE st_intersects(z4g.geom, res.geom)'), postgres_connection)
    # zone_4h_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone4h" AS z4h, public."homes_df" AS res WHERE st_intersects(z4h.geom, res.geom)'), postgres_connection)
    # zone_5a_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5a" AS z5a, public."homes_df" AS res WHERE st_intersects(z5a.geom, res.geom)'), postgres_connection)
    # zone_5b_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5b" AS z5b, public."homes_df" AS res WHERE st_intersects(z5b.geom, res.geom)'), postgres_connection)
    # zone_5c_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5c" AS z5c, public."homes_df" AS res WHERE st_intersects(z5c.geom, res.geom)'), postgres_connection)
    # zone_5d_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5d" AS z5d, public."homes_df" AS res WHERE st_intersects(z5d.geom, res.geom)'), postgres_connection)
    # zone_5e_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5e" AS z5e, public."homes_df" AS res WHERE st_intersects(z5e.geom, res.geom)'), postgres_connection)
    # zone_5f_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5f" AS z5f, public."homes_df" AS res WHERE st_intersects(z5f.geom, res.geom)'), postgres_connection)
    # zone_5g_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5g" AS z5g, public."homes_df" AS res WHERE st_intersects(z5g.geom, res.geom)'), postgres_connection)
    # zone_5h_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5h" AS z5h, public."homes_df" AS res WHERE st_intersects(z5h.geom, res.geom)'), postgres_connection)
    # zone_5i_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5i" AS z5i, public."homes_df" AS res WHERE st_intersects(z5i.geom, res.geom)'), postgres_connection)
    # zone_5j_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5j" AS z5j, public."homes_df" AS res WHERE st_intersects(z5j.geom, res.geom)'), postgres_connection)
    # zone_5k_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5k" AS z5k, public."homes_df" AS res WHERE st_intersects(z5k.geom, res.geom)'), postgres_connection)
    # zone_5l_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5l" AS z5l, public."homes_df" AS res WHERE st_intersects(z5l.geom, res.geom)'), postgres_connection)
    # zone_5m_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5m" AS z5m, public."homes_df" AS res WHERE st_intersects(z5m.geom, res.geom)'), postgres_connection)
    # zone_5n_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone5n" AS z1n, public."homes_df" AS res WHERE st_intersects(z5n.geom, res.geom)'), postgres_connection)
    # zone_6a_parcels = gpd.read_postgis(('SELECT res.* FROM public."Zone6a" AS z6a, public."homes_df" AS res WHERE st_intersects(z6a.geom, res.geom)'), postgres_connection)
    
    #now compare those slices to master dataframe using 'parno' field, then populate 'Zone' field with zone name using 'zone_checker' field to hold True/False values
    df['zone_checker'] = zone_1a_parcels['parno'].isin(df['parno'])
    df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone1a'
    df['zone_checker'] = zone_1b_parcels['parno'].isin(df['parno'])
    df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone1b'
    df['zone_checker'] = zone_1c_parcels['parno'].isin(df['parno'])
    df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone1c'
    df['zone_checker'] = zone_1d_parcels['parno'].isin(df['parno'])
    df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone1d'
    df['zone_checker'] = zone_1e_parcels['parno'].isin(df['parno'])
    df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone1e'
    df['zone_checker'] = zone_1f_parcels['parno'].isin(df['parno'])
    df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone1f'
    df['zone_checker'] = zone_1g_parcels['parno'].isin(df['parno'])
    df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone1g'
    df['zone_checker'] = zone_1h_parcels['parno'].isin(df['parno'])
    df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone1h'
    df['zone_checker'] = zone_1i_parcels['parno'].isin(df['parno'])
    df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone1i'
    df['zone_checker'] = zone_1j_parcels['parno'].isin(df['parno'])
    df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone1j'
    # df['zone_checker'] = zone_2a_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone2a'
    # df['zone_checker'] = zone_2b_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone2b'
    # df['zone_checker'] = zone_2c_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone2c'
    # df['zone_checker'] = zone_2d_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone2d'
    # df['zone_checker'] = zone_2e_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone2e'
    # df['zone_checker'] = zone_2f_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone2f'
    # df['zone_checker'] = zone_2g_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone2g'
    # df['zone_checker'] = zone_2h_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone2h'
    # df['zone_checker'] = zone_2i_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone2i'
    # df['zone_checker'] = zone_2j_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone2j'
    # df['zone_checker'] = zone_3a_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone3a'
    # df['zone_checker'] = zone_3b_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone3b'
    # df['zone_checker'] = zone_3c_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone3c'
    # df['zone_checker'] = zone_3d_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone3d'
    # df['zone_checker'] = zone_3e_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone3e'
    # df['zone_checker'] = zone_3f_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone3f'
    # df['zone_checker'] = zone_3g_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone3g'
    # df['zone_checker'] = zone_3h_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone3h'
    # df['zone_checker'] = zone_4a_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone4a'
    # df['zone_checker'] = zone_4b_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone4b'
    # df['zone_checker'] = zone_4c_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone4c'
    # df['zone_checker'] = zone_4d_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone4d'
    # df['zone_checker'] = zone_4e_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone4e'
    # df['zone_checker'] = zone_4f_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone4f'
    # df['zone_checker'] = zone_4g_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone4g'
    # df['zone_checker'] = zone_4h_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone4h'
    # df['zone_checker'] = zone_5a_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5a'
    # df['zone_checker'] = zone_5b_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5b'
    # df['zone_checker'] = zone_5c_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5c'
    # df['zone_checker'] = zone_5d_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5d'
    # df['zone_checker'] = zone_5e_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5e'
    # df['zone_checker'] = zone_5f_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5f'
    # df['zone_checker'] = zone_5g_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5g'
    # df['zone_checker'] = zone_5h_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5h'
    # df['zone_checker'] = zone_5i_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5i'
    # df['zone_checker'] = zone_5j_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5j'
    # df['zone_checker'] = zone_5k_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5k'
    # df['zone_checker'] = zone_5l_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5l'
    # df['zone_checker'] = zone_5m_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5m'
    # df['zone_checker'] = zone_5n_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone5n'
    # df['zone_checker'] = zone_6a_parcels['parno'].isin(df['parno'])
    # df.loc[df['zone_checker'] == True, 'Zone'] = 'Zone6a'
        
    #drop zone_checker field from dataframe
    df.drop(['zone_checker'], inplace=True, axis=1)
    
    
    return df

    
    
    

    