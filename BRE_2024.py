
# look for records of properties that don't have data in custom fields
# look for those that are "out of zone" or "out of area". Are they really?
# Gingercake Acres IS in our zones after all! Zone 5o


import pandas as pd
import geopandas as gpd
from shapely import wkt

#import data
df = pd.read_csv('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE 2024/FullProperties-Export-2024-05-13-extract.csv')
# 276,000 properties total


# look for records of properties have no data in the custom fields
""" I'm choosing the properties with no counties as all the fields are nearly identical results but counties have the most, just slightly"""
no_county_df = df[(df['Display_County_Name__c'].isna())]         #6739
# no_custom_area_df = df[(df['Display_Custom_Area__c'].isna())]    #6737
# no_zone_df = df[(df['Display_Zone__c'].isna())]                  #6732


#keep just the columns I need in the dataframe
columns_to_keep = [
 'County_Name_Lookup__c',
 'Creek_Checkbox__c',
 'Creek_Lookup__c',
 'Custom_Area_Lookup__c',
 'Display_County_Name__c',
 'Display_Custom_Area__c',
 'Display_Zone__c',
 'Id',
 'Name',
 'Nearest_Feature_Lookup__c',
 'Property_Type__c',
 'Zone_Lookup__c',
 'vz__Boundary_Wkt__c'
 ]

# this leaves us with parcels that do not have data in the custom fields for some reason
df_filtered = no_county_df[columns_to_keep]


def wkt_loads(x):
    try: 
        return wkt.loads(x)
    except Exception:
        return None


#temporary export to QGIS to see what these properties look like
df_filtered['geometry'] = df_filtered['vz__Boundary_Wkt__c'].apply(wkt_loads)


#convert pandas dataframe to geopandas dataframe
gdf = gpd.GeoDataFrame(df_filtered, geometry=df_filtered['geometry'], crs='EPSG:4269')

# export geodataframe to file
# gdf.to_file('/Users/ep9k/Desktop/QGIS_TEST.gpkg', driver='GPKG', layer='VeezlaProperties')

#######START HERE
# compare to counties. Need to import county data
caldwell = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Counties/Caldwell_County.gpkg')
joined = gpd.sjoin(gdf, caldwell, how='left', op='within')





