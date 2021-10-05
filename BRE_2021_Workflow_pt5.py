
"""
Mapping column names from original to current Salesforce names

This is for new property records being added.
"""

import pandas as pd

# for some reason the other csv had a ton of empty header rows
new_df = pd.read_csv('/Users/ep9k/Desktop/BRE_2021_update_outputs/NEW_2021_PARCELS_FINAL_noheaders.csv')


#copy data from existing parcel fields into new fields with correct salesforce names

#new name    #old name
new_df['ALTERNATIVE_PARCEL_NUMBER__C'] = new_df['altparno']
new_df['COUNTY__C'] = new_df['cntyname']
new_df['ACRES__C'] = new_df['gisacres']
new_df['IMPROVEMENT_VALUE__C'] = new_df['improvval']
new_df['LAND_VALUE__C'] = new_df['landval']
new_df['MAILING_ADDRESS__C'] = new_df['mailadd']
new_df['MAILING_CITY__C'] = new_df['mcity']
new_df['MAILING_STATE__C'] = new_df['mstate']
new_df['PBA__POSTALCODE_PB__C'] = new_df['mzip']
new_df['N_PARCEL_NUMBER__C'] = new_df['nparno']
new_df['MAILING_NAME__C'] = new_df['ownname']
new_df['NAME'] = new_df['parno']
new_df['PIN__C'] = new_df['parno']
new_df['PARCEL_USE_CODE_2__C'] = new_df['parusecd2']
new_df['PARCEL_USE_CCODE__C'] = new_df['parusecode']
new_df['PARCEL_USE_DESCRIPTION__C'] = new_df['parusedesc']
new_df['PARCEL_VALUE__C'] = new_df['parval']
new_df['REVISE_DATE__C'] = new_df['revisedate']
new_df['REVISE_YEAR__C'] = new_df['reviseyear']
new_df['SALE_DATE__C'] = new_df['saledate']
new_df['PBA__ADDRESS_PB__C'] = new_df['siteadd']
new_df['SOURCE_DATE__C'] = new_df['sourcedate']
new_df['PBA__STATECODE_PB__C'] = new_df['stname']
new_df['PBA__YEARBUILT_PB__C'] = new_df['structyear']
new_df['SUBDIVISION__C'] = new_df['subdivisio']
new_df['GEOLOCATION__LONGITUDE__S'] = new_df['longitude']
new_df['GEOLOCATION__LATITUDE__S'] = new_df['latitude']
new_df['PBA__LONGITUDE_PB__C'] = new_df['longitude']
new_df['PBA__LATITUDE_PB__C'] = new_df['latitude']
new_df['GEOMETRY_SHAPE__C'] = new_df['geometry']


#columns that are not needed in salesforce records
columns_to_drop = ['cntyfips','gnisid','legdecfull','maddpref','maddrno','maddstname','maddstr','maddstsuf',
                   'maddsttyp','mapref','multistruc','munit','ownfrst','ownlast','ownname2','owntype',
                   'parusedsc2','parvaltype','presentval','recareano','recareatx','revdatetx','saddno','saddpref',
                   'saddstname','saddstr','saddstsuf','saddsttyp','saledatetx','scity','sourceagnt','sourceref',
                   'sstate','stcntyfips','stfips','struct','structno','subowntype','subsurfown','sunit','szip',
                   'transfdate','layer','path']

new_df.drop(columns_to_drop, inplace=True, axis=1)

#columns that are duplicated and now no longer needed
columns_to_drop = ['altparno','cntyname','gisacres','improvval','landval','mailadd','mcity','mstate','mzip','nparno',
                   'ownname','parno','parusecd2','parusecode','parusedesc','parval','revisedate','reviseyear','saledate',
                   'siteadd','sourcedate','stname','structyear','subdivisio','longitude','latitude','geometry', 'sourcedatx']

new_df.drop(columns_to_drop, inplace=True, axis=1)

#Map CUSTOM_AREA__C column values to id of each custom area
new_df.loc[new_df['Custom Area'] == 'Banner Elk', 'CUSTOM_AREA__C'] = 'a2E3u000000fPH4EAM'
new_df.loc[new_df['Custom Area'] == 'Beech Mountain', 'CUSTOM_AREA__C'] = 'a2E3u000000fPH5EAM'
new_df.loc[new_df['Custom Area'] == 'Bethel', 'CUSTOM_AREA__C'] = 'a2E3u000000fPH6EAM'
new_df.loc[new_df['Custom Area'] == 'Blowing Rock', 'CUSTOM_AREA__C'] = 'a2E3u000000fPH7EAM'
new_df.loc[new_df['Custom Area'] == 'Boone', 'CUSTOM_AREA__C'] = 'a2E3u000000fPH8EAM'
new_df.loc[new_df['Custom Area'] == 'Colletsville', 'CUSTOM_AREA__C'] = 'a2E3u000000fPH9EAM'
new_df.loc[new_df['Custom Area'] == 'Creston', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHAEA2'
new_df.loc[new_df['Custom Area'] == 'Crossnore', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHBEA2'
new_df.loc[new_df['Custom Area'] == 'Crumpler', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHCEA2'
new_df.loc[new_df['Custom Area'] == 'Deep Gap', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHDEA2'
new_df.loc[new_df['Custom Area'] == 'Elk Park', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHEEA2'
new_df.loc[new_df['Custom Area'] == 'Fleetwood', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHFEA2'
new_df.loc[new_df['Custom Area'] == 'Foscoe', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHGEA2'
new_df.loc[new_df['Custom Area'] == 'Glendale Springs', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHHEA2'
new_df.loc[new_df['Custom Area'] == 'Grassy Creek', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHIEA2'
new_df.loc[new_df['Custom Area'] == 'Jefferson', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHJEA2'
new_df.loc[new_df['Custom Area'] == 'Lansing', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHKEA2'
new_df.loc[new_df['Custom Area'] == 'Laurel Springs', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHLEA2'
new_df.loc[new_df['Custom Area'] == 'Linville', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHMEA2'
new_df.loc[new_df['Custom Area'] == 'Matney', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHNEA2'
new_df.loc[new_df['Custom Area'] == 'Minneapolis', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHOEA2'
new_df.loc[new_df['Custom Area'] == 'Pineola', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHPEA2'
new_df.loc[new_df['Custom Area'] == 'Piney Creek', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHQEA2'
new_df.loc[new_df['Custom Area'] == 'Scottville', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHREA2'
new_df.loc[new_df['Custom Area'] == 'Seven Devils', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHSEA2'
new_df.loc[new_df['Custom Area'] == 'Sparta', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHTEA2'
new_df.loc[new_df['Custom Area'] == 'Sugar Grove', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHUEA2'
new_df.loc[new_df['Custom Area'] == 'Sugar Mountain', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHVEA2'
new_df.loc[new_df['Custom Area'] == 'Todd', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHWEA2'
new_df.loc[new_df['Custom Area'] == 'Triplett', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHXEA2'
new_df.loc[new_df['Custom Area'] == 'Valle Crucis', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHYEA2'
new_df.loc[new_df['Custom Area'] == 'Vilas', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHZEA2'
new_df.loc[new_df['Custom Area'] == 'Warrensville', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHaEAM'
new_df.loc[new_df['Custom Area'] == 'West Jefferson', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHbEAM'
new_df.loc[new_df['Custom Area'] == 'Zionville', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHcEAM'
new_df.loc[new_df['Custom Area'] == 'Newland', 'CUSTOM_AREA__C'] = 'a2E3u000000fPHdEAM'


#export output to csv file
# new_df.to_csv('/Users/ep9k/Desktop/BRE_2021_update_outputs/final.csv')


