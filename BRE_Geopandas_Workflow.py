
"""
This is a new master workflow to add geospatial overlay data from QGIS to tax parcel data throughout the high country area.
Previously this workflow encompassed some manual work in QGIS but now I am able to do it in Geopandas, making for a much
nicer, cleaner, and more concise workflow using just pandas + geopandas and a few other libraries

This is the data/fields that I need to add to the tax parcels (in no particular order)...
    - Nearest Feature
    - Creek
    - Custom Area
    - Zone
    - County 
    - Subdivision (coming soon?)

Part of the issue with this data is that parcels have different geospatial fields
    - Boundary (WKT): This field holds polygon data about object. This is the preferred geometry field
    - Geolocation (Property Record): This field holds point data about object (at point centroid I think?). This is 2nd preference
    - Geolocation: This field holds point data about object. This is 3rd preference
    - Some parcels have no spatial reference. There is nothing I can really do about these
"""



########################## 1: Import libraries and layers ##########################
import geopandas as gpd
import pandas as pd
import numpy as np
from shapely import wkt

parcels = pd.read_csv('/Users/ep9k/Desktop/geopandas_test/BRE_Test/all_bre_properties.csv')
custom_areas = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/Custom_Areas.gpkg')
zones = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/Zones.gpkg')
creeks = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/Creeks.gpkg')
watauga_lake = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/Watauga_Lake.gpkg')
new_river_south_fork = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/NewRiver_SouthFork.gpkg')
new_river_north_fork = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/NewRiver_NorthFork.gpkg')
watauga_river = gpd.read_file('/Users/ep9k/Desktop/geopandas_test/BRE_Test/WataugaRiver.gpkg')

# delete fields that I will recreate in this script
# I exported this dataset out of salesforce so it already has the needed columns in the dataframe
# I will recreate these columns later
columns_to_drop = ['NEAREST_FEATURE_LOOKUP__C','CREEK_CHECKBOX__C', 'CREEK_LOOKUP__C', 'CUSTOM_AREA_LOOKUP__C', 'ZONE_LOOKUP__C', 'COUNTY_NAME_LOOKUP__C']
parcels.drop(columns_to_drop, axis=1, inplace=True)



########################## 2: Separate parcels into categories based on spatial data available ##########################
"""
This leaves us with three geodataframes. 
    - First are those that have data in the Boundary (WKT) field (VZ__BOUNDARY_WKT__C)
    - If not, next are those that have data in Geolocation (Property Record) field (VZ__GEOLOCATION_MEASURED__LONGITUDE__S)
    - If not, next are those with data in the Geolocation field (VZ__GEOLOCATION__LONGITUDE__S)
    - else, parcels with no geospatial data
    
I need to separate out these 3 (4) categories and work with the independently
"""
wkt_df = parcels.loc[parcels['VZ__BOUNDARY_WKT__C'].notnull()]
geolocation_measured_df = parcels.loc[(parcels['VZ__BOUNDARY_WKT__C'].isnull()) & (parcels['VZ__GEOLOCATION_MEASURED__LONGITUDE__S'].notnull())]
geolocation_df = parcels.loc[(parcels['VZ__BOUNDARY_WKT__C'].isnull()) & (parcels['VZ__GEOLOCATION_MEASURED__LONGITUDE__S'].isnull()) & (parcels['VZ__GEOLOCATION__LONGITUDE__S'].notnull())]
no_spatial_info = parcels.loc[(parcels['VZ__BOUNDARY_WKT__C'].isnull()) & (parcels['VZ__GEOLOCATION_MEASURED__LONGITUDE__S'].isnull()) & (parcels['VZ__GEOLOCATION__LONGITUDE__S'].isnull())]



########################## 3: convert those that have spatial info to GeoDataFrame ##########################
def wkt_loads(x):
    try:
        return wkt.loads(x)
    except Exception:
        return None
   
#wkt_gdf
wkt_df['geometry'] = wkt_df['VZ__BOUNDARY_WKT__C'].apply(wkt_loads)
wkt_gdf = gpd.GeoDataFrame(wkt_df, geometry='geometry')

#geolocation_measured_gdf
geolocation_measured_gdf = gpd.GeoDataFrame(geolocation_measured_df, geometry=gpd.points_from_xy(geolocation_measured_df['VZ__GEOLOCATION_MEASURED__LONGITUDE__S'], geolocation_measured_df['VZ__GEOLOCATION_MEASURED__LATITUDE__S']))

#geolocation_gdf
geolocation_gdf = gpd.GeoDataFrame(geolocation_df, geometry=gpd.points_from_xy(geolocation_df['VZ__GEOLOCATION__LONGITUDE__S'], geolocation_df['VZ__GEOLOCATION__LATITUDE__S']))



########################## 4:  Make sure all layers and geodataframes have same CRS ##########################
wkt_gdf = wkt_gdf.set_crs("epsg:32617")   
geolocation_measured_gdf = geolocation_measured_gdf.set_crs("epsg:32617")
geolocation_gdf = geolocation_gdf.set_crs("epsg:32617")
custom_areas = custom_areas.to_crs(epsg=32617)
zones = zones.to_crs(epsg=32617)
creeks = creeks.to_crs(epsg=32617)
watauga_lake = watauga_lake.to_crs(epsg=32617)
new_river_south_fork = new_river_south_fork.to_crs(epsg=32617)
new_river_north_fork = new_river_north_fork.to_crs(epsg=32617)
watauga_river = watauga_river.to_crs(epsg=32617)



########################## 5: Add Custom Area ##########################
"""
Spatial join to add 'CUSTOM_AREA_LOOKUP__C' column to parcels. 
This is a left join which will keep parcels that are outside the custom areas.
This also creates duplicates for those parcels that overlap more than 1 custom area
"""

# do spatial join
wkt_gdf = wkt_gdf.sjoin(custom_areas, how='left', predicate='intersects')
geolocation_measured_gdf = geolocation_measured_gdf.sjoin(custom_areas, how='left', predicate='intersects')
geolocation_gdf = geolocation_gdf.sjoin(custom_areas, how='left', predicate='intersects')

# drop duplicated indexes
wkt_gdf = wkt_gdf[~wkt_gdf.index.duplicated(keep="first")]
geolocation_measured_gdf = geolocation_measured_gdf[~geolocation_measured_gdf.index.duplicated(keep='first')]
geolocation_gdf = geolocation_gdf[~geolocation_gdf.index.duplicated(keep='first')]

# rename 'custom area' column to Salesforce Name
wkt_gdf['CUSTOM_AREA_LOOKUP__C'] = wkt_gdf['Name']
geolocation_measured_gdf['CUSTOM_AREA_LOOKUP__C'] = geolocation_measured_gdf['Name']
geolocation_gdf['CUSTOM_AREA_LOOKUP__C'] = geolocation_gdf['Name']

# fill NA values in 'custom area' column with 'Out of Area'
wkt_gdf['CUSTOM_AREA_LOOKUP__C'] = wkt_gdf['CUSTOM_AREA_LOOKUP__C'].fillna(value='Out of Area')
geolocation_measured_gdf['CUSTOM_AREA_LOOKUP__C'] = geolocation_measured_gdf['CUSTOM_AREA_LOOKUP__C'].fillna(value='Out of Area')
geolocation_gdf['CUSTOM_AREA_LOOKUP__C'] = geolocation_gdf['CUSTOM_AREA_LOOKUP__C'].fillna(value='Out of Area')

# drop unneeded columns
columns_to_drop = ['index_right','Name','layer','path']
wkt_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)



########################## 6: Add Zones ##########################
"""
Spatial join to add 'ZONE_LOOKUP__C' column to parcels.
This is a left join which will keep parcels that are outside the zones.
This also creates duplicates for those parecels that overlap more than 1 zone.
"""

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

#fill NA values in 'Zone' column with 'Outside of Zone'
wkt_gdf['ZONE_LOOKUP__C'] = wkt_gdf['ZONE_LOOKUP__C'].fillna(value='Out of Zone')
geolocation_measured_gdf['ZONE_LOOKUP__C'] = geolocation_measured_gdf['ZONE_LOOKUP__C'].fillna(value='Out of Zone')
geolocation_gdf['ZONE_LOOKUP__C'] = geolocation_gdf['ZONE_LOOKUP__C'].fillna(value='Out of Zone')

# drop unneeded columns
columns_to_drop = ['index_right','ZoneName',]
wkt_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_measured_gdf.drop(columns_to_drop, axis=1, inplace=True)
geolocation_gdf.drop(columns_to_drop, axis=1, inplace=True)



########################## 7: Add Creeks ##########################
"""
Spatial join to add 'CREEK_LOOKUP__C' field with creek names to parcels
This is a left join which will keep parcels that are outside of the zones/areas
This also creates duplicates for those parcels that overlap 1 or more creeks
                     
Add a True of False (boolean) value in field 'CREEK_CHECKBOX__C' if a parcel intersects a creek
"""

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
geolocation_measured_gdf = geolocation_measured_gdf.sjoin_nearest(creeks, distance_col='distance_to_creek')
# convert ft to miles for 'distance_to_creek' column
geolocation_measured_gdf['distance_creek_mi'] = geolocation_measured_gdf['distance_to_creek'] * 0.000621371


#####START HERE

# test = geolocation_measured_gdf.head(100)
# ax=test['geometry'].plot()
# zones['geometry'].plot(ax=ax, color='green')



