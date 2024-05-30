
# look for records of properties that don't have data in custom fields
# look for those that are "out of zone" or "out of area". Are they really?
# Gingercake Acres IS in our zones after all! Zone 5o


import pandas as pd
import geopandas as gpd
from shapely import wkt
import BRE_2024_Lookup as Lookup

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






#populate 'County_Name_Lookup__c' field
#start with giving all values in 'County_Name_Lookup' field a value of "out of area"
gdf['County_Name_Lookup__c'] = 'a2E3u000000fUvcEAE'

#iterate over each custom area and perform spatial join to fill in column
for county_name, (county_gdf, county_id) in Lookup.counties.items():
    #Perform the spatial join
    intersecting = gpd.sjoin(gdf, county_gdf, how='inner', op='intersects')
    #Update the 'County_Name_Lookup__c' column for intersecting rows
    gdf.loc[intersecting.index, 'County_Name_Lookup__c'] = county_id


# populate 'Display_County_Name__c' field
# start with giving all values an 'Out of County' value
gdf['Display_County_Name__c'] = 'Out of County'

#iterate over each custom area and perform spatial join to fill in column
for county_name, (county_gdf, county_id) in Lookup.counties.items():
    #Perform the spatial join
    intersecting = gpd.sjoin(gdf, county_gdf, how='inner', op='intersects')
    #Update the 'Display_County_Name__c' column for intersecting rows
    gdf.loc[intersecting.index, 'Display_County_Name__c'] = county_name



# populate 'Custom_Area_Lookup__c' column
# Start by giving an 'Out of County' value 
gdf['Custom_Area_Lookup__c'] = 'a2E3u000000fTeLEAU'

#iterate over each custom area and perform spatial join to fill in column
for area_name, (custom_area_gdf, area_id) in Lookup.custom_areas.items():
    #perform the spatial join
    intersecting = gpd.sjoin(gdf, custom_area_gdf, how='inner', op='intersects')
    #update the 'Custom_Area_Lookup__c' column for intersecting rows
    gdf.loc[intersecting.index, 'Custom_Area_Lookup__c'] = area_id




#populate 'Display_Custom_Area__c' column
# Start by giving all values "Out of Area" value
gdf['Display_Custom_Area__c'] = 'Out of Area'

#iterate over each custom area and perform spatial join to fill in column
for area_name, (custom_area_gdf, area_id) in Lookup.custom_areas.items():
    #perform the spatial join
    intersecting = gpd.sjoin(gdf, custom_area_gdf, how='inner', op='intersects')
    #update the 'Custom_Area_Lookup__c' column for intersecting rows
    gdf.loc[intersecting.index, 'Display_Custom_Area__c'] = area_name
    
    
#populate 'Zone_Lookup__c column
# start by giving all values 'out of zone' value
gdf['Zone_Lookup__c'] = 'a2E3u000000fUvhEAE'

#iterate over each zone and perform spatial join to fill in column
for zone_name, (zone_gdf, zone_id) in Lookup.zones.items():
    #perform the spatial join
    intersecting = gpd.sjoin(gdf, zone_gdf, how='inner', op='intersects')
    #update the 'Custom_Area_Lookup__c' column for intersecting rows
    gdf.loc[intersecting.index, 'Zone_Lookup__c'] = zone_id
    
    
    
    

# Nearest_Feature_Lookup__c column
# Ensure all GeoDataFrames have the same CRS
if not (Lookup.wataugariver.crs == Lookup.wataugalake.crs == Lookup.nforknewriver.crs == Lookup.sforknewriver.crs == gdf.crs):
    Lookup.wataugariver = Lookup.wataugariver.to_crs(gdf.crs)
    Lookup.wataugalake = Lookup.wataugalake.to_crs(gdf.crs)
    Lookup.nforknewriver = Lookup.nforknewriver.to_crs(gdf.crs)
    Lookup.sforknewriver = Lookup.sforknewriver.to_crs(gdf.crs)

# Add a 'feature_name' column to each river/lake GeoDataFrame
Lookup.wataugariver['feature_name'] = 'a2E3u000000fPmwEAE'
Lookup.wataugalake['feature_name'] = 'a2E3u000000fPmrEAE'
Lookup.nforknewriver['feature_name'] = 'a2E3u000000fPsfEAE'
Lookup.sforknewriver['feature_name'] = 'a2E3u000000fPskEAE'

# Combine all rivers and lake into a single GeoDataFrame
features = pd.concat([Lookup.wataugariver,Lookup.wataugalake, Lookup.nforknewriver, Lookup.sforknewriver], ignore_index=True)

# Initialize the 'Nearest_Feature_Lookup__c' column in gdf
gdf['Nearest_Feature_Lookup__c'] = 'None'

# Function to find the intersecting feature
def find_intersecting_feature(polygon, features):
    if polygon is None or polygon.is_empty:
        return 'None'
    for _, feature in features.iterrows():
        if polygon.intersects(feature.geometry):
            return feature['feature_name']
    return 'None'


# Apply the function to each row in gdf
gdf['Nearest_Feature_Lookup__c'] = gdf.geometry.apply(lambda polygon: find_intersecting_feature(polygon, features))




# CREEKS
#########START HERE. LOOK AT CREEKS AGAIN IN BRE_2024_LOOKUP FILE AND REDO THIS PART
# Ensure both GeoDataFrames have the same CRS
if gdf.crs != Lookup.minor_creeks.crs:
    Lookup.minor_creeks = Lookup.minor_creeks.to_crs(gdf.crs)

# Initialize the columns in gdf
gdf['Creek_Checkbox__c'] = 'FALSE'
gdf['Creek_Lookup__c'] = ''

# Function to check for intersection and update columns
def check_creek_intersection(polygon, creeks):
    if polygon is None or polygon.is_empty:
        return 'FALSE', ''
    for _, creek in creeks.iterrows():
        if creek.geometry is not None and not creek.geometry.is_empty and polygon.intersects(creek.geometry):
            return 'TRUE', creek['gnis_name']
    return 'FALSE', ''

# Apply the function to each row in gdf
gdf[['Creek_Checkbox__c', 'Creek_Lookup__c']] = gdf.geometry.apply(
    lambda polygon: pd.Series(check_creek_intersection(polygon, Lookup.minor_creeks))
)



# print('Exporting gdf')
# gdf.to_csv('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE 2024/BRE_2024_update.csv')
