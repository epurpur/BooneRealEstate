
"""
This is the third script in the series of updating the 2021 tax parcel data.

Between scripts 2 and 3 I exported the data into QGIS and added the following geographic columns:
latitude, longitude, custom area, zone, distToNewRiver, NewRiver, DistToWataugaRiver, WataugaRiver

Steps:
1. Import shapefile data from QGIS and read into geopandas dataframe.

2. Rename columns

3. Artificially change distance columns to 0 if distance to new or watauga river is less than .25 miles

4. Create 'Nearest Feature' column. To do this I compare distance to either new or watauga river. First I choose distance that is shortest. Then depending whether this is new or watauga river I take that distance and the 'distance to feature'

5. Drop unnecessary columns

6. Rename columns so they match to Salesforce columns
"""

import pandas as pd
import geopandas as gpd
from shapely import wkt
import numpy as np


# Import 2021 new data. Geometry column will be created automatically
filepath = '/Users/ep9k/Desktop/BRE_AREAS/new_2021_extract_final.shp'
new_2021_parcels_df = gpd.read_file(filepath)

# rename columns I created in QGIS to something meaningful
new_2021_parcels_df.rename(columns={'added_ge_1': 'longitude', 
                                    'added_ge_2': 'latitude', 
                                    'added_ge_3': 'Custom Area', 
                                    'added_ge_4': 'Zone', 
                                    'added_ge_5': 'DistToNewRiver',
                                    'added_ge_6': 'NewRiver',
                                    'added_ge_7': 'DistToWataugaRiver',
                                    'added_ge_8': 'WataugaRiver',
                                    'new_2021_1': 'Property Type'}, 
                                    inplace=True)

# if parcels < .25mi from new river, artificially change that distance to 0
new_2021_parcels_df.loc[new_2021_parcels_df['DistToNewRiver'] <= .25, 'DistToNewRiver'] = 0

# if parcels < .25mi from watauga river, artificially change that distance to 0
new_2021_parcels_df.loc[new_2021_parcels_df['DistToWataugaRiver'] <= .25, 'DistToWataugaRiver'] = 0


#determine nearest river
#first see if parcel is closer to new or watauga river
new_2021_parcels_df['Nearest Feature'] = new_2021_parcels_df['DistToNewRiver'] < new_2021_parcels_df['DistToWataugaRiver']

#if new is closer, change 'nearest feature' column to "New River", else if false then "Watauga River"
new_2021_parcels_df['Nearest Feature'].loc[new_2021_parcels_df['Nearest Feature'] == True] = 'New River'
new_2021_parcels_df['Nearest Feature'].loc[new_2021_parcels_df['Nearest Feature'] == False] = 'Watauga River'

#now create 'Distance to Feature' column. If 'Nearest Feature' is "New River", take value from 'DistToNewRiver' column, otherwise take 'DistToWataugaRiver' column

#create 'Distance to Feature' Column
new_2021_parcels_df['Distance To Feature'] = new_2021_parcels_df['Nearest Feature']
new_2021_parcels_df.loc[new_2021_parcels_df['Distance To Feature'] == 'New River', 'Distance To Feature'] = new_2021_parcels_df['DistToNewRiver']
new_2021_parcels_df.loc[new_2021_parcels_df['Distance To Feature'] == 'Watauga River', 'Distance To Feature'] = new_2021_parcels_df['DistToWataugaRiver']



# remove unneeded columns
columns_to_drop = ['NewRiver', 'WataugaRiver', 'DistToNewRiver', 'DistToWataugaRiver', 'new_2021_p', 'added_geom', 'fid']
new_2021_parcels_df.drop(columns_to_drop, inplace=True, axis=1)



# rename columns so they match to Salesforce column names
new_2021_parcels_df.rename(columns={'id': 'ID',
                                 'altparno': 'ALTERNATIVE_PARCEL_NUMBER__C',
                                 'cntyname': 'COUNTY__C',
                                 'gisacres': 'ACRES__C',
                                 'improvval':'IMPROVEMENT_VALUE_C',
                                 'landval':'LAND_VALUE__C',
                                 'mailadd': 'MAILING_ADDRESS__C',
                                 'mcity': 'MAILING_CITY__C',
                                 'mstate': 'MAILING_STATE__C',
                                 'mzip': 'MAILING_POSTAL_CODE__C',
                                 'parno': 'NAME',
                                 'parusecd2': 'PARCEL_USE_CODE_2__C',
                                 'parval': 'PARCEL_VALUE__C',
                                 'revisedate':'REVISE_DATE__C',
                                 'reviseyear': 'REVISE_YEAR__C',
                                 'saledate': 'SALE_DATE__C',
                                 'siteadd': 'PBA__ADDRESS_PB__C',
                                 'sourcedatx': 'SOURCE_DATE__C',
                                 'sstate': 'PBA__STATE_PB__C',
                                 'Property Type': 'PBA_PROPERTYTYPE__C',
                                 'longitude': 'GEOLOCATION__LONGITUDE__S',
                                 'latitude': 'GEOLOCATION__LATITUDE__S',
                                 'Custom Area': 'CUSTOM_AREA__C',
                                 'Zone': 'ZONE__C',
                                 'geometry': 'GEOMETRY_SHAPE__C',
                                 'Nearest Feature': 'NEAREST_FEATURE__C',
                                 'Distance To Feature': 'DISTANCE_TO_FEATURE__C'
                                }, inplace=True)
    

#create a couple columns that don't exist yet
new_2021_parcels_df['PBA__LATITUDE_PB__C'] = new_2021_parcels_df['GEOLOCATION__LATITUDE__S']
new_2021_parcels_df['PBA__LONGITUDE_PB__C'] = new_2021_parcels_df['GEOLOCATION__LONGITUDE__S']




