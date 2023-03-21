
"""
This is a new master workflow to add geospatial overlay data from QGIS to tax parcel data throughout the high country area.
Previously this workflow encompassed some manual work in QGIS but now I am able to do it in Geopandas, making for a much
nicer, cleaner, and more concise workflow using just pandas + geopandas and a few other libraries

This is the data/fields that I need to add to the tax parcels (in no particular order)...
    - Nearest Feature
    - Creek       X
    - Custom Area X
    - Zone   X
    - County  X
    - Subdivision (coming soon?)

Part of the issue with this data is that parcels have different geospatial fields
    - Boundary (WKT): This field holds polygon data about object. This is the preferred geometry field
    - Geolocation (Property Record): This field holds point data about object (at point centroid I think?). This is 2nd preference
    - Geolocation: This field holds point data about object. This is 3rd preference
    - Some parcels have no spatial reference. There is nothing I can really do about these
"""



########################## 1: Import libraries and layers ##########################
print('1. initial setup')

import geopandas as gpd
import pandas as pd
import numpy as np
from shapely import wkt
import BRE_Geopandas_Workflow_Mappers as mappers

parcels = pd.read_csv('/Users/ep9k/Desktop/Boone 2023-03-17/37005-37009-37011-37027-37189-37193-47019-47091-2023-01-18.csv')

custom_areas = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/Custom_Areas.gpkg')
zones = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/Zones.gpkg')
creeks = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/Creeks.gpkg')
watauga_lake = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/Watauga_Lake.gpkg')
new_river_south_fork = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/NewRiver_SouthFork.gpkg')
new_river_north_fork = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/NewRiver_NorthFork.gpkg')
watauga_river = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/WataugaRiver.gpkg')
counties = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/Counties.gpkg')

# delete fields that I will recreate in this script
# I exported this dataset out of salesforce so it already has the needed columns in the dataframe
# I will recreate these columns later

#columns_to_drop = ['NEAREST_FEATURE_LOOKUP__C','CREEK_CHECKBOX__C', 'CREEK_LOOKUP__C', 'CUSTOM_AREA_LOOKUP__C', 'ZONE_LOOKUP__C', 'COUNTY_NAME_LOOKUP__C']
#parcels.drop(columns_to_drop, axis=1, inplace=True)


########################## 2: Separate parcels into categories based on spatial data available ##########################
"""
This leaves us with three geodataframes. 
    - First are those that have data in the Boundary (WKT) field (VZ__BOUNDARY_WKT__C)
    - If not, next are those that have data in Geolocation (Property Record) field (VZ__GEOLOCATION_MEASURED__LONGITUDE__S)
    - If not, next are those with data in the Geolocation field (VZ__GEOLOCATION__LONGITUDE__S)
    - else, parcels with no geospatial data
    
I need to separate out these 3 (4) categories and work with them independently
"""
print("2. splitting data into dataframes")

wkt_df = parcels.loc[parcels['vz__Boundary_Wkt__c'].notnull()]
geolocation_measured_df = parcels.loc[(parcels['vz__Boundary_Wkt__c'].isnull()) & (parcels['vz__Geolocation_Measured__Longitude__s'].notnull())]
geolocation_df = parcels.loc[(parcels['vz__Boundary_Wkt__c'].isnull()) & (parcels['vz__Geolocation_Measured__Longitude__s'].isnull()) & (parcels['vz__Geolocation_Mailing__Longitude__s'].notnull())]
no_spatial_info = parcels.loc[(parcels['vz__Boundary_Wkt__c'].isnull()) & (parcels['vz__Geolocation_Measured__Longitude__s'].isnull()) & (parcels['vz__Geolocation_Mailing__Longitude__s'].isnull())]



########################## 3: convert those that have spatial info to GeoDataFrame ##########################
print("3. convert those with spatial info to geodataframe")

def wkt_loads(x):
    try:
        return wkt.loads(x)
    except Exception:
        return None
   
#wkt_gdf
wkt_df['geometry'] = wkt_df['vz__Boundary_Wkt__c'].apply(wkt_loads)
wkt_gdf = gpd.GeoDataFrame(wkt_df, geometry='geometry')

#geolocation_measured_gdf
geolocation_measured_gdf = gpd.GeoDataFrame(geolocation_measured_df, geometry=gpd.points_from_xy(geolocation_measured_df['vz__Geolocation_Measured__Longitude__s'], geolocation_measured_df['vz__Geolocation_Measured__Latitude__s']))

#geolocation_gdf
geolocation_gdf = gpd.GeoDataFrame(geolocation_df, geometry=gpd.points_from_xy(geolocation_df['vz__Geolocation_Mailing__Longitude__s'], geolocation_df['vz__Geolocation_Mailing__Latitude__s']))



########################## 4:  Make sure all layers and geodataframes have same CRS ##########################
print("4. setting CRS for all layers")

wkt_gdf = wkt_gdf.set_crs("epsg:4269")   
geolocation_measured_gdf = geolocation_measured_gdf.set_crs("epsg:4269")
geolocation_gdf = geolocation_gdf.set_crs("epsg:4269")
custom_areas = custom_areas.to_crs(epsg=4269)
zones = zones.to_crs(epsg=4269)
creeks = creeks.to_crs(epsg=4269)
watauga_lake = watauga_lake.to_crs(epsg=4269)
new_river_south_fork = new_river_south_fork.to_crs(epsg=4269)
new_river_north_fork = new_river_north_fork.to_crs(epsg=4269)
watauga_river = watauga_river.to_crs(epsg=4269)
counties = counties.to_crs(epsg=4269)




########################## 5: Add Custom Area ##########################
"""
Spatial join to add 'CUSTOM_AREA_LOOKUP__C' column to parcels. 
This is a left join which will keep parcels that are outside the custom areas.
This also creates duplicates for those parcels that overlap more than 1 custom area
"""

print("5. Adding Custom Area to data")

# do spatial join
wkt_gdf = wkt_gdf.sjoin(custom_areas, how='left', predicate='intersects')
geolocation_measured_gdf = geolocation_measured_gdf.sjoin(custom_areas, how='left', predicate='intersects')
geolocation_gdf = geolocation_gdf.sjoin(custom_areas, how='left', predicate='intersects')

# drop duplicated indexes
wkt_gdf = wkt_gdf[~wkt_gdf.index.duplicated(keep="first")]
geolocation_measured_gdf = geolocation_measured_gdf[~geolocation_measured_gdf.index.duplicated(keep='first')]
geolocation_gdf = geolocation_gdf[~geolocation_gdf.index.duplicated(keep='first')]

# rename 'custom area' column to Salesforce Name
wkt_gdf['CUSTOM_AREA_LOOKUP__C'] = wkt_gdf['Name_right']
geolocation_measured_gdf['CUSTOM_AREA_LOOKUP__C'] = geolocation_measured_gdf['Name_right']
geolocation_gdf['CUSTOM_AREA_LOOKUP__C'] = geolocation_gdf['Name_right']

# fill NA values in 'custom area' column with 'Out of Area'
wkt_gdf['CUSTOM_AREA_LOOKUP__C'] = wkt_gdf['CUSTOM_AREA_LOOKUP__C'].fillna(value='Out of Area')
geolocation_measured_gdf['CUSTOM_AREA_LOOKUP__C'] = geolocation_measured_gdf['CUSTOM_AREA_LOOKUP__C'].fillna(value='Out of Area')
geolocation_gdf['CUSTOM_AREA_LOOKUP__C'] = geolocation_gdf['CUSTOM_AREA_LOOKUP__C'].fillna(value='Out of Area')

# drop unneeded columns
columns_to_drop = ['index_right','Name_right','layer','path']
wkt_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)



########################## 6: Add Zones ##########################
"""
Spatial join to add 'ZONE_LOOKUP__C' column to parcels.
This is a left join which will keep parcels that are outside the zones.
This also creates duplicates for those parecels that overlap more than 1 zone.
"""

print("6. Adding Zones to data")

# do spatial join
wkt_gdf = wkt_gdf.sjoin(zones, how='left', predicate='intersects')
geolocation_measured_gdf = geolocation_measured_gdf.sjoin(zones, how='left', predicate='intersects')
geolocation_gdf = geolocation_gdf.sjoin(zones, how='left', predicate='intersects')

# drop duplicated indexes
wkt_gdf = wkt_gdf[~wkt_gdf.index.duplicated(keep="first")]
geolocation_measured_gdf = geolocation_measured_gdf[~geolocation_measured_gdf.index.duplicated(keep="first")]
geolocation_gdf = geolocation_gdf[~geolocation_gdf.index.duplicated(keep="first")]

# rename 'zones' column to Salesforce Name
wkt_gdf['ZONE_LOOKUP__C'] = wkt_gdf['ZoneName']
geolocation_measured_gdf['ZONE_LOOKUP__C'] = geolocation_measured_gdf['ZoneName']
geolocation_gdf['ZONE_LOOKUP__C'] = geolocation_gdf['ZoneName']

# fill NA values in 'Zone' column with 'Out of Zone'
wkt_gdf['ZONE_LOOKUP__C'] = wkt_gdf['ZONE_LOOKUP__C'].fillna(value='Out of Zone')
geolocation_measured_gdf['ZONE_LOOKUP__C'] = geolocation_measured_gdf['ZONE_LOOKUP__C'].fillna(value='Out of Zone')
geolocation_gdf['ZONE_LOOKUP__C'] = geolocation_gdf['ZONE_LOOKUP__C'].fillna(value='Out of Zone')

# drop unneeded columns
columns_to_drop = ['index_right','ZoneName']
wkt_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)



########################## 7: Add Counties ##########################
""" 
Spatial join to add 'COUNTY_NAME_LOOKUP__C' to parcels.
This is a left join which will keep parcels that are outside the counties.
This also creates duplicates for those parcels that overlap more than one county.
"""

print("7. Adding Counties to data")

# do spatial join
wkt_gdf = wkt_gdf.sjoin(counties, how='left', predicate='intersects')
geolocation_measured_gdf = geolocation_measured_gdf.sjoin(counties, how='left', predicate='intersects')
geolocation_gdf = geolocation_gdf.sjoin(counties, how='left', predicate='intersects')

# drop duplicated indexes
wkt_gdf = wkt_gdf[~wkt_gdf.index.duplicated(keep="first")]
geolocation_measured_gdf = geolocation_measured_gdf[~geolocation_measured_gdf.index.duplicated(keep="first")]
geolocation_gdf = geolocation_gdf[~geolocation_gdf.index.duplicated(keep="first")]

# rename 'counties' column to 'COUNTY_NAME_LOOKUP__C'
wkt_gdf['COUNTY_NAME_LOOKUP__C'] = wkt_gdf['NAME']
geolocation_measured_gdf['COUNTY_NAME_LOOKUP__C'] = geolocation_measured_gdf['NAME']
geolocation_gdf['COUNTY_NAME_LOOKUP__C'] = geolocation_gdf['NAME']

# fill NA values in 'County' column with 'Out of County'
wkt_gdf['COUNTY_NAME_LOOKUP__C'] = wkt_gdf['COUNTY_NAME_LOOKUP__C'].fillna(value='Out of County')
geolocation_measured_gdf['COUNTY_NAME_LOOKUP__C'] = geolocation_measured_gdf['COUNTY_NAME_LOOKUP__C'].fillna(value='Out of County')
geolocation_gdf['COUNTY_NAME_LOOKUP__C'] = geolocation_gdf['COUNTY_NAME_LOOKUP__C'].fillna(value='Out of County')

# drop unneeded columns
columns_to_drop = ['index_right','STATEFP','COUNTYFP','COUNTYNS','GEOID','NAME','NAMELSAD','LSAD','CLASSFP',
                   'MTFCC','CSAFP','CBSAFP','METDIVFP','FUNCSTAT','ALAND','AWATER','INTPTLAT','INTPTLON']
wkt_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)


########################## 8: Add Creeks ##########################
"""
Spatial join to add 'CREEK_LOOKUP__C' field with creek names to parcels
This is a left join which will keep parcels that are outside of the zones/areas
This also creates duplicates for those parcels that overlap 1 or more creeks
                     
Add a True of False (boolean) value in field 'CREEK_CHECKBOX__C' if a parcel intersects a creek

"""

print("8. Adding Creeks to data")

# fill 'None' value of no-name creeks with empty string
creeks['gnis_name'] = creeks['gnis_name'].fillna(value='')

# for wkt_gdf, do spatial join for creeks
wkt_gdf = wkt_gdf.sjoin(creeks, how='left', predicate='intersects')
# remove duplicated indexes
wkt_gdf = wkt_gdf[~wkt_gdf.index.duplicated(keep="first")]
# rename 'gnis_name' column to 'CREEK_LOOKUP__C' column
wkt_gdf['CREEK_LOOKUP__C'] = wkt_gdf['gnis_name']
# drop unneeded columns
columns_to_drop = [ 'index_right','OBJECTID','permanent_identifier','fdate','resolution','gnis_id',
                    'gnis_name','lengthkm','reachcode','flowdir','wbarea_permanent_identifier','ftype','fcode','mainpath',
                    'innetwork','visibilityfilter','SHAPE_Length','resolution_description','flowdir_description','mainpath_description',
                    'innetwork_description','visibilityfilter_description','fcode_description']
wkt_gdf.drop(columns_to_drop, axis=1, inplace=True)

# for geolocation_measured_gdf and geolocation_gdf, I will use sjoin.nearest() to find distance to nearest creek
# need to convert layers to a different CRS for measuring distance
creeks = creeks.to_crs(epsg=2264)
geolocation_measured_gdf = geolocation_measured_gdf.to_crs(epsg=2264)
geolocation_gdf = geolocation_gdf.to_crs(epsg=2264)

geolocation_measured_gdf = geolocation_measured_gdf.sjoin_nearest(creeks, distance_col='distance_to_creek')
geolocation_gdf = geolocation_gdf.sjoin_nearest(creeks, distance_col='distance_to_creek')

# drop duplicates
geolocation_measured_gdf = geolocation_measured_gdf[~geolocation_measured_gdf.index.duplicated(keep="first")]
geolocation_gdf = geolocation_gdf[~geolocation_gdf.index.duplicated(keep="first")]

# if distance greater than 0.2 miles, it is decided that the property is not on a creeka and value wil be empty. 1056 ft = 0.2 mi
# overwriting geometry column from point data to polygon (buffer)
geolocation_measured_gdf['geometry'] = geolocation_measured_gdf.buffer(1056)
geolocation_gdf['geometry'] = geolocation_gdf.buffer(1056)

#drop unneeded columns
columns_to_drop = ['index_right','OBJECTID','permanent_identifier','fdate','resolution','gnis_id','gnis_name','lengthkm','reachcode','flowdir','wbarea_permanent_identifier',
                   'ftype','fcode','mainpath','innetwork','visibilityfilter','SHAPE_Length','resolution_description','flowdir_description','mainpath_description','innetwork_description',
                   'visibilityfilter_description','fcode_description','distance_to_creek']
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)

# do sjoin on buffer to see if creek in buffer. If so, then use that creek as 'nearest creek'
geolocation_measured_gdf = geolocation_measured_gdf.sjoin(creeks, how='left', predicate='intersects')
geolocation_gdf = geolocation_gdf.sjoin(creeks, how='left', predicate='intersects')

# remove duplicated indexes
geolocation_measured_gdf = geolocation_measured_gdf[~geolocation_measured_gdf.index.duplicated(keep="first")]
geolocation_gdf = geolocation_gdf[~geolocation_gdf.index.duplicated(keep="first")]

# rename 'gnis_name' column to 'CREEK_LOOKUP__C' column
geolocation_measured_gdf['CREEK_LOOKUP__C'] = geolocation_measured_gdf['gnis_name']
geolocation_gdf['CREEK_LOOKUP__C'] = geolocation_gdf['gnis_name']

# drop unneeded columns
columns_to_drop = [ 'index_right','OBJECTID','permanent_identifier','fdate','resolution','gnis_id','gnis_name','lengthkm','reachcode','flowdir','wbarea_permanent_identifier','ftype',
                    'fcode','mainpath','innetwork','visibilityfilter','SHAPE_Length','resolution_description','flowdir_description','mainpath_description','innetwork_description','visibilityfilter_description','fcode_description']
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)


########################## 9: Add Nearest Feature ##########################

"""
This section will determine a parcel's location relative to the 'nearest feature'.
The features are: New River North Fork, New River South Fork, Watauga River, Watauga Lake.

The result of this stip will be the 'NEAREST_FEATURE_LOOKUP__C' field

Will perform sjoin_nearest on all parcels
"""

print("9. Adding nearest feature to data")

# convert all layers to different CRS (epsg 2264)
wkt_gdf = wkt_gdf.to_crs(epsg=2264)
new_river_north_fork = new_river_north_fork.to_crs(epsg=2264)
new_river_south_fork = new_river_south_fork.to_crs(epsg=2264)
watauga_river = watauga_river.to_crs(epsg=2264)
watauga_lake = watauga_lake.to_crs(epsg=2264)



# will need to get centroid point for wkt_gdf parcels
wkt_gdf['centroid'] = wkt_gdf.centroid

# Need to move 'geometry' column temporarily to another column. This is because later steps require the 'geometry' column for operations. 
wkt_gdf['geom_temp'] = wkt_gdf['geometry']
geolocation_measured_gdf['geom_temp'] = geolocation_measured_gdf['geometry']
geolocation_gdf['geom_temp'] = geolocation_gdf['geometry']


# make buffer of 0.2 miles 1056ft = 0.2 mi
wkt_gdf['geometry'] = wkt_gdf.buffer(1056)
geolocation_measured_gdf['geometry'] = geolocation_measured_gdf.buffer(1056)
geolocation_gdf['geometry'] = geolocation_gdf.buffer(1056)

# run sjoin on parcel layers to see which intersect with nearest features
wkt_gdf = wkt_gdf.sjoin(watauga_lake, how='left', predicate='intersects')
geolocation_measured_gdf = geolocation_measured_gdf.sjoin(watauga_lake, how='left', predicate='intersects')
geolocation_gdf = geolocation_gdf.sjoin(watauga_lake, how='left', predicate='intersects')

# where there is a match for WATAUGA LAKE, fill 'NEAREST_FEATURE_LOOKUP__C' column with value 'Watauga Lake'
wkt_gdf['NEAREST_FEATURE_LOOKUP__C'] = np.where((wkt_gdf['gnis_name'] == 'Watauga Lake'), 'Watauga Lake', '')
geolocation_measured_gdf['NEAREST_FEATURE_LOOKUP__C'] = np.where((geolocation_measured_gdf['gnis_name'] == 'Watauga Lake'), 'Watauga Lake', '')
geolocation_gdf['NEAREST_FEATURE_LOOKUP__C'] = np.where((geolocation_gdf['gnis_name'] == 'Watauga Lake'), 'Watauga Lake', '')

#drop unneeded columns
columns_to_drop = ['index_right','OBJECTID','permanent_identifier','fdate','resolution','gnis_id','gnis_name','areasqkm','elevation','reachcode','ftype','fcode','visibilityfilter','SHAPE_Length',
                    'SHAPE_Area','resolution_description','visibilityfilter_description','fcode_description']
wkt_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)

# run sjoin on WATAUGA RIVER
wkt_gdf = wkt_gdf.sjoin(watauga_river, how='left', predicate='intersects')
geolocation_measured_gdf = geolocation_measured_gdf.sjoin(watauga_river, how='left', predicate='intersects')
geolocation_gdf = geolocation_gdf.sjoin(watauga_river, how='left', predicate='intersects')

# drop duplicates
wkt_gdf = wkt_gdf[~wkt_gdf.index.duplicated(keep="first")]
geolocation_measured_gdf = geolocation_measured_gdf[~geolocation_measured_gdf.index.duplicated(keep="first")]
geolocation_gdf = geolocation_gdf[~geolocation_gdf.index.duplicated(keep="first")]

# where there is a match on watauga river, fill 'NEAREST_FEATURE_LOOKUP__C' column with value 'Watauga River'
wkt_gdf.loc[wkt_gdf['LABEL'] == 2.0, 'NEAREST_FEATURE_LOOKUP__C'] = 'Watauga River'
geolocation_measured_gdf.loc[geolocation_measured_gdf['LABEL'] == 2.0, 'NEAREST_FEATURE_LOOKUP__C'] = 'Watauga River'
geolocation_gdf.loc[geolocation_gdf['LABEL'] == 2.0, 'NEAREST_FEATURE_LOOKUP__C'] = 'Watauga River'

# drop unneeded columns
columns_to_drop = [ 'index_right','id','MILES','LABEL','FIPS','StrmName']
wkt_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)

# run sjoin on NEW RIVER NORTH FORK
wkt_gdf = wkt_gdf.sjoin(new_river_north_fork, how='left', predicate='intersects')
geolocation_measured_gdf = geolocation_measured_gdf.sjoin(new_river_north_fork, how='left', predicate='intersects')
geolocation_gdf = geolocation_gdf.sjoin(new_river_north_fork, how='left', predicate='intersects')

# drop duplicates
wkt_gdf = wkt_gdf[~wkt_gdf.index.duplicated(keep="first")]
geolocation_measured_gdf = geolocation_measured_gdf[~geolocation_measured_gdf.index.duplicated(keep="first")]
geolocation_gdf = geolocation_gdf[~geolocation_gdf.index.duplicated(keep="first")]

# where there is a match on New River North Fork, fill 'NEAREST_FEATURE_LOOKUP__C' column with value 'New River North Fork'
wkt_gdf.loc[wkt_gdf['id'] == 1.0, 'NEAREST_FEATURE_LOOKUP__C'] = 'New River North Fork'
geolocation_measured_gdf.loc[geolocation_measured_gdf['id'] == 1.0, 'NEAREST_FEATURE_LOOKUP__C'] = 'New River North Fork'
geolocation_gdf.loc[geolocation_gdf['id'] == 1.0, 'NEAREST_FEATURE_LOOKUP__C'] = 'New River North Fork'

# drop unneeded columns
columns_to_drop = ['index_right', 'id']
wkt_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)

# run sjoin on NEW RIVER SOUTH FORK
wkt_gdf = wkt_gdf.sjoin(new_river_south_fork, how='left', predicate='intersects')
geolocation_measured_gdf = geolocation_measured_gdf.sjoin(new_river_south_fork, how='left', predicate='intersects')
geolocation_gdf = geolocation_gdf.sjoin(new_river_south_fork, how='left', predicate='intersects')

# drop duplicates
wkt_gdf = wkt_gdf[~wkt_gdf.index.duplicated(keep="first")]
geolocation_measured_gdf = geolocation_measured_gdf[~geolocation_measured_gdf.index.duplicated(keep="first")]
geolocation_gdf = geolocation_gdf[~geolocation_gdf.index.duplicated(keep="first")]

# where there is a match on NEW RIVER SOUTH FORK, fill 'NEAREST_FEATURE_LOOKUP__C' column with value 'New River South Fork'
wkt_gdf.loc[wkt_gdf['id'] == 1.0, 'NEAREST_FEATURE_LOOKUP__C'] = 'New River South Fork'
geolocation_measured_gdf.loc[geolocation_measured_gdf['id'] == 1.0, 'NEAREST_FEATURE_LOOKUP__C'] = 'New River South Fork'
geolocation_gdf.loc[geolocation_gdf['id'] == 1.0, 'NEAREST_FEATURE_LOOKUP__C'] = 'New River South Fork'

columns_to_drop = ['index_right', 'id']
wkt_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)

# replace 'geometry' with previously created 'geom_temp' column
wkt_gdf['geometry'] = wkt_gdf['geom_temp']
geolocation_measured_gdf['geometry'] = wkt_gdf['geom_temp']
geolocation_gdf['geometry'] = geolocation_gdf['geom_temp']

# drop 'geom2' column
wkt_gdf.drop(['geom_temp'], axis=1, inplace=True)
geolocation_measured_gdf.drop(['geom_temp'], axis=1, inplace=True)
geolocation_gdf.drop(['geom_temp'], axis=1, inplace=True)

########################## 10: Convert to Salesforce ID numbers ##########################
"""
The geographic information has been added to the dataset. Now, we need to convert the feature names to salesforce IDs. I have a helper file called 'workflow mappers'
to accompany this. Workflow mappers is a collection of functions to convert names to salesforce IDs
"""


print("10. Converting feature names to salesforce IDs")

# Custom Areas
wkt_gdf = mappers.map_custom_area_name(wkt_gdf)
geolocation_measured_gdf = mappers.map_custom_area_name(geolocation_measured_gdf)
geolocation_gdf = mappers.map_custom_area_name(geolocation_gdf)

# Zones
wkt_gdf = mappers.map_zone_name(wkt_gdf)
geolocation_measured_gdf = mappers.map_zone_name(geolocation_measured_gdf)
geolocation_gdf = mappers.map_zone_name(geolocation_gdf)

# Counties
wkt_gdf = mappers.map_county_name(wkt_gdf)
geolocation_measured_gdf = mappers.map_county_name(geolocation_measured_gdf)
geolocation_gdf = mappers.map_county_name(geolocation_gdf)

# Creeks
wkt_gdf = mappers.map_creek_name(wkt_gdf)
geolocation_measured_gdf = mappers.map_creek_name(geolocation_measured_gdf)
geolocation_gdf = mappers.map_creek_name(geolocation_gdf)

# Nearest Features
wkt_gdf = mappers.map_nearest_feature_name(wkt_gdf)
geolocation_measured_gdf = mappers.map_nearest_feature_name(geolocation_measured_gdf)
geolocation_gdf = mappers.map_nearest_feature_name(geolocation_gdf)

# Subdivision

### QUESTIONS FOR MATT: where to get list of all subdivisions?  Are we using creek checkbox field?  Which file to use from Benedek?






