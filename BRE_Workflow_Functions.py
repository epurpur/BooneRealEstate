

import pandas as pd



def property_type_column(df):
    """creates property type column for dataframe"""

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
    df.loc[df['Property Type'].isnull(), 'Property Type'] = 'Home / Potentially Not Residential'
    
    return df
    