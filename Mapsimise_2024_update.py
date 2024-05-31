
import pandas as pd
import geopandas as gpd
from shapely import wkt
import BRE_2024_Lookup as Lookup


#import data
df = pd.read_csv('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE 2024/FullProperties-Export-2024-05-13-extract.csv')
mapsimize = pd.read_csv('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE 2024/CustomAreaBlankorCustomAreaequalsoutofarea.csv')



def wkt_loads(x):
    try: 
        return wkt.loads(x)
    except Exception:
        return None


#temporary export to QGIS to see what these properties look like
df['geometry'] = df['vz__Boundary_Wkt__c'].apply(wkt_loads)


#convert pandas dataframe to geopandas dataframe
gdf = gpd.GeoDataFrame(df, geometry=df['geometry'], crs='EPSG:4269')



# Merge mapsimize and gdf based on 'Record ID' and 'Id' to include the 'geometry' column
merged_df = mapsimize.merge(gdf[['Id', 'geometry']], left_on='Record ID', right_on='Id', how='inner')

# Check which records in mapsimize are in gdf
mapsimize['In_gdf'] = mapsimize['Record ID'].isin(gdf['Id'])

# Filter mapsimize for records that are in gdf and include the 'geometry' column
in_gdf = mapsimize[mapsimize['In_gdf']].merge(gdf[['Id', 'geometry']], left_on='Record ID', right_on='Id', how='left')

# Convert the DataFrame to a GeoDataFrame
in_gdf = gpd.GeoDataFrame(in_gdf, geometry='geometry')

# Optionally, set the CRS (Coordinate Reference System) if it's known
in_gdf.set_crs('EPSG:4269', inplace=True)  # Replace 'EPSG:4326' with your CRS


# Populate 'County_Name_Lookup__c' field
# Start with giving all values in 'County_Name_Lookup__c' field a value of "out of area"
in_gdf['County_Name_Lookup__c'] = 'a2E3u000000fUvcEAE'

# Iterate over each custom area and perform spatial join to fill in column
for county_name, (county_gdf, county_id) in Lookup.counties.items():
    # Perform the spatial join
    intersecting = gpd.sjoin(in_gdf, county_gdf, how='inner', op='intersects')
    # Update the 'County_Name_Lookup__c' column for intersecting rows
    in_gdf.loc[intersecting.index, 'County_Name_Lookup__c'] = county_id

# Populate 'Display_County_Name__c' field
# Start with giving all values an 'Out of County' value
in_gdf['Display_County_Name__c'] = 'Out of County'

# Iterate over each custom area and perform spatial join to fill in column
for county_name, (county_gdf, county_id) in Lookup.counties.items():
    # Perform the spatial join
    intersecting = gpd.sjoin(in_gdf, county_gdf, how='inner', op='intersects')
    # Update the 'Display_County_Name__c' column for intersecting rows
    in_gdf.loc[intersecting.index, 'Display_County_Name__c'] = county_name

# Populate 'Custom_Area_Lookup__c' column
# Start by giving an 'Out of County' value 
in_gdf['Custom_Area_Lookup__c'] = 'a2E3u000000fTeLEAU'

# Iterate over each custom area and perform spatial join to fill in column
for area_name, (custom_area_gdf, area_id) in Lookup.custom_areas.items():
    # Perform the spatial join
    intersecting = gpd.sjoin(in_gdf, custom_area_gdf, how='inner', op='intersects')
    # Update the 'Custom_Area_Lookup__c' column for intersecting rows
    in_gdf.loc[intersecting.index, 'Custom_Area_Lookup__c'] = area_id

# Populate 'Display_Custom_Area__c' column
# Start by giving all values "Out of Area" value
in_gdf['Display_Custom_Area__c'] = 'Out of Area'

# Iterate over each custom area and perform spatial join to fill in column
for area_name, (custom_area_gdf, area_id) in Lookup.custom_areas.items():
    # Perform the spatial join
    intersecting = gpd.sjoin(in_gdf, custom_area_gdf, how='inner', op='intersects')
    # Update the 'Display_Custom_Area__c' column for intersecting rows
    in_gdf.loc[intersecting.index, 'Display_Custom_Area__c'] = area_name

# Populate 'Zone_Lookup__c' column
# Start by giving all values 'out of zone' value
in_gdf['Zone_Lookup__c'] = 'a2E3u000000fUvhEAE'

# Iterate over each zone and perform spatial join to fill in column
for zone_name, (zone_gdf, zone_id) in Lookup.zones.items():
    # Perform the spatial join
    intersecting = gpd.sjoin(in_gdf, zone_gdf, how='inner', op='intersects')
    # Update the 'Zone_Lookup__c' column for intersecting rows
    in_gdf.loc[intersecting.index, 'Zone_Lookup__c'] = zone_id

# Nearest_Feature_Lookup__c column
# Ensure all GeoDataFrames have the same CRS
if not (Lookup.wataugariver.crs == Lookup.wataugalake.crs == Lookup.nforknewriver.crs == Lookup.sforknewriver.crs == in_gdf.crs):
    Lookup.wataugariver = Lookup.wataugariver.to_crs(in_gdf.crs)
    Lookup.wataugalake = Lookup.wataugalake.to_crs(in_gdf.crs)
    Lookup.nforknewriver = Lookup.nforknewriver.to_crs(in_gdf.crs)
    Lookup.sforknewriver = Lookup.sforknewriver.to_crs(in_gdf.crs)

# Add a 'feature_name' column to each river/lake GeoDataFrame
Lookup.wataugariver['feature_name'] = 'a2E3u000000fPmwEAE'
Lookup.wataugalake['feature_name'] = 'a2E3u000000fPmrEAE'
Lookup.nforknewriver['feature_name'] = 'a2E3u000000fPsfEAE'
Lookup.sforknewriver['feature_name'] = 'a2E3u000000fPskEAE'

# Combine all rivers and lake into a single GeoDataFrame
features = pd.concat([Lookup.wataugariver, Lookup.wataugalake, Lookup.nforknewriver, Lookup.sforknewriver], ignore_index=True)

# Initialize the 'Nearest_Feature_Lookup__c' column in in_gdf
in_gdf['Nearest_Feature_Lookup__c'] = 'None'

# Function to find the intersecting feature
def find_intersecting_feature(polygon, features):
    if polygon is None or polygon.is_empty:
        return 'None'
    for _, feature in features.iterrows():
        if polygon.intersects(feature.geometry):
            return feature['feature_name']
    return 'None'

# Apply the function to each row in in_gdf
in_gdf['Nearest_Feature_Lookup__c'] = in_gdf.geometry.apply(lambda polygon: find_intersecting_feature(polygon, features))

# CREEKS
# Ensure both GeoDataFrames have the same CRS
if in_gdf.crs != Lookup.minor_creeks.crs:
    Lookup.minor_creeks = Lookup.minor_creeks.to_crs(in_gdf.crs)

# Initialize the columns in in_gdf
in_gdf['Creek_Checkbox__c'] = 'FALSE'
in_gdf['Creek_Lookup__c'] = ''

# Function to check for intersection and update columns
def check_creek_intersection(polygon, creeks):
    if polygon is None or polygon.is_empty:
        return 'FALSE', ''
    for _, creek in creeks.iterrows():
        if creek.geometry is not None and not creek.geometry.is_empty and polygon.intersects(creek.geometry):
            return 'TRUE', creek['gnis_name']
    return 'FALSE', ''

# Apply the function to each row in in_gdf
in_gdf[['Creek_Checkbox__c', 'Creek_Lookup__c']] = in_gdf.geometry.apply(
    lambda polygon: pd.Series(check_creek_intersection(polygon, Lookup.minor_creeks))
)

# Convert creek names to Salesforce ID
in_gdf['Creek_Lookup__c'] = in_gdf['Creek_Lookup__c'].map(Lookup.creeks)

#convert 'Record Id' column to call it just 'Id'
in_gdf['Id'] = in_gdf['Record ID']
in_gdf.to_csv('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE 2024/Mapsimise_mystery_properties_update.csv')


