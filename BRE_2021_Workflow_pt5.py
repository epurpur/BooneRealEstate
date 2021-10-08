
"""
Mapping column names from original to current Salesforce names

This is for new property records being added.
"""

import pandas as pd

# for some reason the other csv had a ton of empty header rows
new_df = pd.read_csv('/Users/ep9k/Desktop/BRE_2021_update_outputs/NEW_2021_PARCELS_FINAL_noheaders.csv')


#copy data from existing parcel fields into new fields with correct salesforce names

#new name                                  #old name
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



#clean erroneous values out of SUBDIVISION__C field


#first need to get list of all subdivisions and areas
custom_objects = ['Willow Valley', 'Windcrest', 'Windy Hill', 'Windy Mountain',
       'Winkler Highlands', 'Wintergreen Acres', 'Wiseman',
       'Wonderland Woods', 'Wood Acres', 'Woodcroft Estates', 'Woodlawn',
       'Woodridge', 'Woodside', 'Woodwinds', 'Yonahlossee',
       'Yonahlossee Estates', 'Yonahlossee Saddle Club', 'Young Hollow',
       'Little Bavaria', 'Little Creek', 'Locust Hills',
       'Lodges At Winklers Creek', 'Lonestar Estates', 'Longview Meadows',
       'Lynnview', "Madison'S Place", 'Maple Springs',
       'Martindale Estates', 'Mast Farm Ridge', 'Matilda Acres',
       'Mayfield', 'Mayview', 'Mayview Center Court',
       'Mayview Manor Cliff', 'Mayview Park', 'Mccorkle Acres',
       'Mccorkle Acres Ii', 'Meadow Ridge', 'Meadowbrook',
       'Meadows Brook', 'Meadowview', 'Middlebrook', 'Mill Race Village',
       'Mill Ridge', 'Millers Ridge', 'Millstone Ridge - I',
       'Millstone Ridge - Ii', 'Mining Town Estates', 'Mink Hill',
       'Misty Acres', 'Misty Mountain', 'Monte Crucis', 'Morningside',
       'Morningview', 'Mountain Haven', 'Mountain Lake Estates',
       'Mountain Meadow', 'Mountain Ridge Estates', 'Mountain Shadows',
       'Mountain Shore', 'Mountain Springs Gardens', 'Mountain View',
       'Mountain View Estates', 'Mountain View Retreat', 'Murray Hill',
       'Myria Forest', 'Myrtle Hills', 'Mystic Woods', 'Nautica Cove',
       'New Market Estates', 'New River Falls', 'New River Heights',
       'New River Lakes', 'New Village At Green Park', 'Nile Park',
       'North Heights', 'North Ivy', 'Northriver Shores', 'Northview',
       'Oak Hill', 'Oak Hill Estates', 'Oak Point Estates', 'Oak Ridge',
       'Okalona Acres', 'Old Keller Farm', 'Old Mill Stream', 'Old Pond',
       'Opalbrook', 'Orchard Meadows', 'Outback', 'Painted Mountain',
       'Panhandle Farms', 'Panorama Estates', 'Park Place',
       'Old Mill Ridge Estate', 'Parkside', 'Parkway Crossing',
       'Parkway Forest', 'Pate Acres', 'Patriot Place', 'Paty Place',
       'Pfeiffer Ridge Estates', 'Pine Hill', 'Pine Hill At Poplar Grove',
       'Pine Ridge', 'Pine Village', 'Pinecrest', 'Pinewoods',
       'Pinnacle Wods', 'Pioneer', 'Plymouth Rock', 'Plymouth Trace',
       'Point 8 Pines', 'Powder Horn', 'Quail Hollow Estates',
       'Quail Meadows', 'Quail Ridge', 'Quail View', 'Banner Elk',
       'Beech Mountain', 'Bethel', 'Blowing Rock', 'Boone',
       'Colletsville', 'Creston', 'Crossnore', 'Crumpler', 'Deep Gap',
       'Elk Park', 'Fleetwood', 'Foscoe', 'Glendale Springs',
       'Grassy Creek', 'Jefferson', 'Lansing', 'Laurel Springs',
       'Linville', 'Matney', 'Minneapolis', 'Pineola', 'Piney Creek',
       'Scottville', 'Seven Devils', 'Sparta', 'Sugar Grove',
       'Sugar Mountain', 'Todd', 'Triplett', 'Valle Crucis', 'Vilas',
       'Warrensville', 'West Jefferson', 'Zionville', 'Newland',
       'Ledford Gardens', 'Leisure Acres', 'Liberty', 'Liberty Landing',
       'Lincoln Heights', 'Lincoln Place', 'Link Hill Estates',
       'Linville Ridge', 'Butler', 'Hampton', 'Laurel Bloomery',
       'Mountain City', 'Roan Mountain', 'Shady Valley', 'Watauga Lake',
       'Trade', 'Greenfield', 'Greenhill', 'Greystone I', 'Greystone Iv',
       'Grove Park', 'Grovehurst', 'Hamilton Estates', 'Hampton Estates',
       'Hampton Farms', 'Hampton Hills', 'Harbin Hill', 'Hartley Knob',
       'Hawks Peak', 'Hawks Peak South', 'Hawks Peak Villas',
       'Hawks Peak West', 'Hawthorne Landing', 'Headwaters At Banner Elk',
       'Heartwood', 'Heather Ridge', 'Heaton Creek Estates',
       'Heavenly Mountain', 'Hemlock Village', 'Heritage Ridge',
       'Heritage Village', 'Heritage Villlage', 'Hi-Acres',
       'Hickory Heights', 'Hickory Hills Estates', 'Hickory Ridge',
       'Hidden Acres', 'Hidden Hills', 'Hidden Meadows', 'Hidden Oaks',
       'Hidden Valley Retreat', 'Hidden Wood Estates',
       'Hide Away Estates', 'Lakes Community', 'Lakeside Acres',
       'Laurel Chase', 'Laurel Creek', 'Laurel Crest', 'Laurel Highlands',
       'Laurel Hill', 'Laurel Mountain Estates', 'Laurel Park',
       'Laurel Ridge', 'Laurelwood Estates', 'Leatherwood',
       'Hillwinds Estates', 'Holiday Hills', 'Holly Meadows Farms',
       'Holston Heights', 'Holston View Court', 'Hillmont Heights',
       'Horizon Heights', 'Horseshoe Cove', 'Hound Ears',
       'Hound Ears - Fairway', 'Hound Ears - The Lakes',
       'Howards Landing', 'Huckleberry Knob', 'Hummingbird Hill',
       'Hunters Ridge', 'Hunting Hills', 'Hylander Estates', 'Idlewylde',
       'Island Creek', 'Ivywood', 'June Apple Estates',
       'June Appleestates', 'Kalmia Acres', 'Kel Pat', 'Keller Acres',
       'Keller Farm', 'Kellwood', 'Kellwood - Bunny Ln',
       'Kellwood - Carriage Lamp', 'Kellwood - Creekside',
       'Kellwood - New Village On The Green',
       'Kellwood - Village On The Green', 'Kellwood Ii',
       'Kensington Gate', 'King Springs Add', 'Kings Ransom', 'Kingswood',
       'Knob Hill', 'Lake Watauga Vista', 'Lakeridge', 'High Pine Ridge',
       'Highland Acres', 'Highland Hills', 'Rainbow Creek Estates',
       'Rainbow Mountain', 'Rainbow Mountain Estates', 'Ranger Estates',
       'Raven Rock', 'Raven Rock Cove', 'Ravens Ridge', 'Rayon Terrace',
       'Red Fox Ridge', 'Red Tail Mountain', 'Reserve', 'Reserve I',
       'Reserve Ii', 'Rhododendron Estates', 'Rhododendron Ridge',
       'Rich Mountain Ranches', 'Ridgecrest Estates',
       'Ridgecrest On The Parkway', 'Ridgefield Estates',
       'Ridgefield Glen', 'Ridgeview', 'Ridgeview Acres',
       'Ridgeview Estates', 'Rio Vista', 'River Bluff', 'River Oaks',
       'River Pointe', 'River Ridge', 'River Valley',
       'River Valley Meadows', 'Riverbend', 'Riverland Court',
       'Rivers End', 'Riverside Homes', 'Riversound', 'Riverstone',
       'Riverwood At Valle Crucis', 'Roan Creek Estates', 'Roan Highland',
       'Roan Springs', 'Roan Valley Golf Estate',
       'Roan Valley Golf Estates', 'Roan Valley Golg Estates',
       'Roan Vista', 'Roanwood', 'Rock Springs Estates', 'Rocky Branch',
       'Rocky Heights', 'Rocky Knob', 'Rocky Meadows',
       'Rocky Mountain Heights', 'Rolling Hills', 'Royal Oaks',
       'Rustic Manor', 'Saddle Hills', 'Saddle Ridge Park',
       'Salem Village', 'Sauls Camp Ridge', 'Scenic View', 'Scenoramic',
       'Seasons Ridge', 'Sebastian Woods', 'Seths Way', 'Seven Oaks',
       'Seven Springs', 'Sevier Gardens', 'Shady Acres', 'Shady Meadows',
       'Shady Valley Apple', 'Shenandoah Heights', "Shore'S Farm",
       "Shull'S Farm", 'Sierra Vista', 'Silo Ridge', 'Silver Springs',
       'Ski Crest Park', 'Ski Mountain', 'Smithdeal Estates',
       'Snaggy Mountain', 'Sommerset', 'Sorrento', 'Sorrento Falls',
       'Sorrento Forest', 'Sorrento Highlands', 'Sorrento Knolls',
       'Sorrento Skies', 'Sorrento Woods', 'South Hills',
       'Southern Skies', 'Southwood', 'Spice Branch At Grandfather',
       'Spring Hill', 'Sprucy Ridge', 'Ssunalei Preserve',
       'Stanmoore Estates', 'State Line Park', 'Stillhouse Creek',
       'Stonebridge', 'Stoneview Estates', 'Sugar Cove',
       'Stonecliff Preserve', 'Stonecrest', 'Stonegate', 'Summerwood',
       'Summit Park', 'Sunalei Preserve', 'Sunny Acres',
       'Sunny Chestnut Forest', 'Sunny View', 'Sunrise',
       'Sunrise Estates', 'Sunset', 'Sweetgrass', 'Sycamore Gardens',
       'Sycamore Shoals', 'Sunset Mountain', 'Sunset Ranch',
       'Sunset Ridge', 'Sunset Spring', 'Superior Acres', 'Talons',
       'Teaberry Hills', 'The Cones', 'The Farm', 'The Forest',
       'The Gables', 'The Glen', 'The Glens Of Grandfather', 'The Grove',
       'The Hamptons Of Blowing Rock', 'The Harbour', 'The Homestead',
       'The Lodges At Elkmont', 'The Maples At Shulls Mill', 'The Pines',
       'The Pinnacle', 'The Reserve At Roan Mtn', 'The Meadows',
       'The Overlook', 'The Ridge', 'The Ridge At Watauga Lake',
       'The Timbers', 'The Vistas', 'The Woods', 'Thunder Hill Estates',
       'Timber Creek At Blowing Rock', 'Timber Hill Acres',
       'Timber Ridge Acres', 'Timbercrest', 'Timberlakes', 'Timberlane',
       'Timberridge', "Top O' Boone", 'Top Of Boone', 'Treadway',
       'Treadway Estates', 'Trojan Horse', 'Turtle Creek', 'Twin Rivers',
       'Tynecastle', 'University Village', 'Valle Cay', 'Valle Meadows',
       'Valle Ridge', 'Valley Overlook', 'Valley View',
       'Valley View Acres', 'Village At Green Park', 'Village Green',
       'Village Hideaway', 'Village On The Green',
       'Walnut Mountain Farms', 'Warrior Estates', 'Watauga Falls',
       'Watauga River Heights', 'Watauga Valle Trail', 'Watauga Woods',
       'Wellington Place', 'West End', 'West Links Estates',
       'West Mountain City Heights', 'West Town Estates', 'Westover Park',
       'Westside', 'Westview', 'Westwood', 'Whippoorwill Estates',
       'Whispering Hills', 'Whispering Meadows', 'Whispering Pines',
       'Whispering Streams', 'Whisperwood', 'White Pine Hills',
       'White Rock Village', 'Whitney Estates', 'Wickham Square',
       'Wild Apple', 'Wildwinds', 'Wildwood', 'Willow Mountain',
       'Tennessee', 'Creekside', 'Creekside Estates', 'Creekside Park',
       'Creekside Villas', 'Crestmoor', 'Crestview Estates', 'Crestwood',
       'Critcher Meadows', 'Crooked Creek', 'Cross Creek',
       'Cross Mountain', 'Crown Point', 'Crystal Mountain',
       'Crystal Mountain Reserve', 'Curwood', 'Daisy Ridge', 'Dakota',
       'Daniel Boone', 'Dark Hollow', 'Daytona Place',
       'Deer Creek Crossing', 'Deer Creek Falls', 'Deer Crossing',
       'Deer Falls Creek', 'Deer Lick Falls', 'Deer Ridge', 'Deer Run',
       'Deer Run Acres', 'Deer Tracks', 'Deer Trail Acres', 'Deer Valley',
       'Deerfield Estates', 'Deerfield Forest', 'Deerfield Heights',
       'Devils Den', 'Devonwood', 'Diamond Creek', 'Doe Mountain Retreat',
       'Doe River', 'Doe River Estates', 'Dogwood Acres',
       'Dry Run Retreat', 'Eagle Ridge Estates', 'East Brook',
       'East River Park', 'Eastridge Acres', 'Echota',
       'Echota On The Ridge', 'Elk Ridge Estates', 'Elk River',
       'Emeline Hills', 'Emerald Hill', 'Emerald Mountain',
       'Escape Mountain', 'Eureka Hills', 'Evergreen',
       'Evergreen Springs', 'Fair Mountain', 'Fairfield At Aho',
       'Avondale Courts', 'Ayers Mountain', 'Banjo Ridge', 'Bare Hollow',
       'Barefoot Woods', 'Bear Creek', 'Bear Hill', 'Bear Ridge Estates',
       'Bear Run', 'Bear Trail Estates', 'Beechwood', 'Big Springs',
       'Big Tree', 'Biltmore', 'Birchfield Estates', "Bishop'S Ridge",
       'Black Bear Knoll', 'Blackburn', 'Blairmont', 'Candice Court',
       'Candlewood', 'Carefree Cove', 'Castle Court', 'Castle Heights',
       'Cedar Heights', 'Cedar Place', 'Cedar Point', 'Cedar West',
       'Central Heights', 'Chalakee', 'Chapel Hills', 'Charter Ridge',
       'Chateaux Cloud', 'Cherry Hill', 'Cherry Springs', 'Chestnut Hill',
       'Chestnut Hill Village', 'Chestnut Knob', 'Chestnut Lane',
       'Alderly Heights', 'Aldridge Ponds', 'Allen Heights',
       'Almost Heaven', 'Alpine Meadows', 'Alpine Village',
       'Ansley Heights', 'Apple Orchard', 'Arrowhead', 'Ashley Woods',
       'Autumn Chase', 'Autumn Hills', 'Avery Meadows',
       'Blue Ridge Estates', 'Blue Ridge Mountain Club',
       'Blue Ridge Park', 'Boone Fork Camp', 'Boone Pointe',
       'Boone Ridge', 'Boulder Cay', 'Boulder Creek', 'Boulder Gardens',
       'Boulder Shadow', 'Briarclift Estates', 'Briarwood', 'Brightwood',
       'Broadview', 'Brookside Estates', 'Brown Mountain',
       'Brownstone Ridge', 'Buckshot Estates', 'Buckshot Ridge',
       'Buena Vista', 'Buffalo Ridge', 'Buffalo View', 'Cabin Cove',
       'Callalantee', 'Cameron Ridge', 'Camp Rock', 'Cheswyck', 'Chetola',
       'Chetola Estates', 'Cobble Creek', 'Cobblestone Hill',
       'College Park', 'College Place', 'College View Heights',
       'Colonial Acres', 'Continental Divide', 'Fairview',
       'Fairview Terrace', 'Fairway Ridge', 'Fairway Villas',
       'Fairways On The Green', 'Fieldstream', 'Firethorn', 'Five Oaks',
       'Flannery Fork Farms', 'Flat Top Overlook', 'Fleetwood Falls',
       'Forest Acres', 'Forest At Crestwood', 'Forest Edge',
       'Forest Glen', 'Cottages At Banner Elk',
       'Cottages At Wyndham Hill', 'Councill Hills', 'Councill Oaks',
       'Country Acres', 'Country Club Estates', 'Country Place',
       'Countryside', 'Courtside Homes', 'Creek Run', 'Forest Hills',
       'Forest Park', 'Forest Ridge', 'Forest View', 'Fox Cove',
       'Fox Den', 'Fox Meadow Farm', 'Fox Run Ridge', 'Foxtrot',
       'Foxwood', 'Friendly Mountain Acres', 'Friendship',
       'Gable Farm Estates', 'Glen Burney', 'Glen Laurel', 'Glenmoore',
       'Glenwood Springs', 'Golf Club Acres', 'Goshen Valley',
       'Grandfather Farms', 'Grandfather Golf & Country Club',
       'Grandview Terrace', 'Green Acres', 'Green Hills',
       'Green Knob Mountain', 'Green Pines', 'Greene Meadows',
       'Apple Knoll']



# need to capitalize all objects in custom_objects
custom_objects = [item.upper() for item in custom_objects]

# see which objects are not in SUBDIVISION__C column
new_df['Bad Custom Area'] = new_df['SUBDIVISION__C'].isin(custom_objects)

# if 'Bad Custom Area' column is False, erase value from SUBDIVISION__C column
new_df.loc[(new_df['Bad Custom Area'] == False), 'SUBDIVISION__C'] = ''

# drop 'Bad Custom Area' column
new_df.drop('Bad Custom Area', inplace=True, axis=1)



#Map CUSTOM_AREA_LOOKUP__C column values to id of each custom area
new_df.loc[new_df['Custom Area'] == 'Banner Elk', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPH4EAM'
new_df.loc[new_df['Custom Area'] == 'Beech Mountain', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPH5EAM'
new_df.loc[new_df['Custom Area'] == 'Bethel', 'CUSTOM_AREA__C'] = 'a2E3u000000fPH6EAM'
new_df.loc[new_df['Custom Area'] == 'Blowing Rock', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPH7EAM'
new_df.loc[new_df['Custom Area'] == 'Boone', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPH8EAM'
new_df.loc[new_df['Custom Area'] == 'Colletsville', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPH9EAM'
new_df.loc[new_df['Custom Area'] == 'Creston', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHAEA2'
new_df.loc[new_df['Custom Area'] == 'Crossnore', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHBEA2'
new_df.loc[new_df['Custom Area'] == 'Crumpler', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHCEA2'
new_df.loc[new_df['Custom Area'] == 'Deep Gap', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHDEA2'
new_df.loc[new_df['Custom Area'] == 'Elk Park', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHEEA2'
new_df.loc[new_df['Custom Area'] == 'Fleetwood', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHFEA2'
new_df.loc[new_df['Custom Area'] == 'Foscoe', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHGEA2'
new_df.loc[new_df['Custom Area'] == 'Glendale Springs', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHHEA2'
new_df.loc[new_df['Custom Area'] == 'Grassy Creek', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHIEA2'
new_df.loc[new_df['Custom Area'] == 'Jefferson', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHJEA2'
new_df.loc[new_df['Custom Area'] == 'Lansing', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHKEA2'
new_df.loc[new_df['Custom Area'] == 'Laurel Springs', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHLEA2'
new_df.loc[new_df['Custom Area'] == 'Linville', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHMEA2'
new_df.loc[new_df['Custom Area'] == 'Matney', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHNEA2'
new_df.loc[new_df['Custom Area'] == 'Minneapolis', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHOEA2'
new_df.loc[new_df['Custom Area'] == 'Pineola', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHPEA2'
new_df.loc[new_df['Custom Area'] == 'Piney Creek', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHQEA2'
new_df.loc[new_df['Custom Area'] == 'Scottville', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHREA2'
new_df.loc[new_df['Custom Area'] == 'Seven Devils', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHSEA2'
new_df.loc[new_df['Custom Area'] == 'Sparta', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHTEA2'
new_df.loc[new_df['Custom Area'] == 'Sugar Grove', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHUEA2'
new_df.loc[new_df['Custom Area'] == 'Sugar Mountain', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHVEA2'
new_df.loc[new_df['Custom Area'] == 'Todd', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHWEA2'
new_df.loc[new_df['Custom Area'] == 'Triplett', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHXEA2'
new_df.loc[new_df['Custom Area'] == 'Valle Crucis', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHYEA2'
new_df.loc[new_df['Custom Area'] == 'Vilas', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHZEA2'
new_df.loc[new_df['Custom Area'] == 'Warrensville', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHaEAM'
new_df.loc[new_df['Custom Area'] == 'West Jefferson', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHbEAM'
new_df.loc[new_df['Custom Area'] == 'Zionville', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPHcEAM'
new_df.loc[new_df['Custom Area'] == 'Butler', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPTxEAM'
new_df.loc[new_df['Custom Area'] == 'Hampton', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPTyEAM'
new_df.loc[new_df['Custom Area'] == 'Laurel Bloomery', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPTzEAM'
new_df.loc[new_df['Custom Area'] == 'Mountain City', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPU0EAM'
new_df.loc[new_df['Custom Area'] == 'Roan Mountain', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPU1EAM'
new_df.loc[new_df['Custom Area'] == 'Shady Valley', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPU2EAM'
new_df.loc[new_df['Custom Area'] == 'Watauga Lake', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPU3EAM'
new_df.loc[new_df['Custom Area'] == 'Trade', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPU9EAM'
new_df.loc[new_df['Custom Area'] == 'Tennessee', 'CUSTOM_AREA_LOOKUP__C'] = 'a2E3u000000fPRrEAM'





#Map SUBDIVISION_LOOKUP__C column values to id of each subdivision
# There are only about 15 columns with a valid subdivision
new_df.loc[new_df['SUBDIVISION__C'] == 'WHISPERING PINES', 'SUBDIVISION_LOOKUP__C'] = 'a2E3u000000fPROEA2'
new_df.loc[new_df['SUBDIVISION__C'] == 'LAUREL MOUNTAIN ESTATES', 'SUBDIVISION_LOOKUP__C'] = 'a2E3u000000fPMWEA2'
new_df.loc[new_df['SUBDIVISION__C'] == 'HIGHLAND HILLS', 'SUBDIVISION_LOOKUP__C'] = 'a2E3u000000fPLkEAM'
new_df.loc[new_df['SUBDIVISION__C'] == 'GREEN ACRES', 'SUBDIVISION_LOOKUP__C'] = 'a2E3u000000fPL2EAM'
new_df.loc[new_df['SUBDIVISION__C'] == 'BRIARWOOD', 'SUBDIVISION_LOOKUP__C'] = 'a2E3u000000fPIbEAM'
new_df.loc[new_df['SUBDIVISION__C'] == 'BEAR CREEK', 'SUBDIVISION_LOOKUP__C'] = 'a2E3u000000fPICEA2'



#export output to csv file
new_df.to_csv('/Users/ep9k/Desktop/BRE_2021_update_outputs/final.csv')


