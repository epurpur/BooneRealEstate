
"""
THIS IS THE WORKFLOW TO INTEGRATE MATT'S CHANGES TO THE DATA.

One problem we identified is that there are duplicate 'parno' values, meaning the 'parno' is not truly a unique identifier.
However, after looking at the duplicate 'parno's, they are basically all one parcel with holes cut in them by roads, etc.
So there are different shapes for all the pieces (on the map) but they are all the same parcel sharing the same information.

What I figured out is that I have my original parcel list (made up of a combination of all the counties parcels) and I have 
Matt's updated lists with updated '2+ removed' column info, etc. The lists are essentially the same, except Matt's has more
and updated information. I have removed duplicate parcel numbers from Matt's updated lists, which creates a one-to-many
relationship between the master list and his list. Upon merging, multiple shapes(of the same parcel number), all the shapes of
one parcel get updated with one record of information from Matt's list. 

The rest is copy and pasted from my bre_master_workflow_pt1 

"""



import geopandas as gpd
import pandas as pd

#import condo_buildings_list function
MODULE_PATH = '/Users/ep9k/Desktop/BRE/BRE 2019/BRE_Condos_List/scripts/CountyFunctions.py'
MODULE_NAME = 'condo_buildings_list'
import importlib
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module 
spec.loader.exec_module(module)

import BRE_Workflow_Functions as bwf





#matt's original mailing list aka 'new list'
all_2019_parcels = gpd.read_file('/Users/ep9k/Desktop/BRE/BRE 2019/All_Parcels_2019.gpkg')                   #228,393 parcels
matt_parcel_update_excel = pd.read_excel(r'/Users/ep9k/Desktop/master_parcel_list(4-20-20)-matt-final.xlsx')

#drop duplicates from matt_parcel_update_excel so that I have one to many relationship between the two lists
matt_parcel_update_excel = matt_parcel_update_excel.drop_duplicates(subset='parno', keep='first')

#merge list without duplicates (matt_parcel_update_excel) to all_2019_parcels (master_list)
all_2019_parcels = all_2019_parcels.merge(matt_parcel_update_excel, how='left', left_on='parno', right_on='parno')



columns_to_drop = ['id_0',
 'id',
 'altparno_x',
 'cntyfips_x',
 'cntyname_x',
 'gisacres_x',
 'gnisid',
 'improvval_x',
 'landval_x',
 'legdecfull',
 'maddpref',
 'maddrno',
 'maddstname',
 'maddstr',
 'maddstsuf',
 'maddsttyp',
 'mailadd_x',
 'mapref',
 'mcity_x',
 'mstate_x',
 'multistruc_x',
 'munit',
 'mzip_x',
 'nparno',
 'ownfrst',
 'ownlast',
 'ownname_x',
 'ownname2_x',
 'owntype',
 'parusecd2_x',
 'parusecode_x',
 'parusedesc_x',
 'parusedsc2',
 'parval_x',
 'parvaltype_x',
 'presentval_x',
 'recareano_x',
 'recareatx_x',
 'revdatetx',
 'revisedate_x',
 'reviseyear_x',
 'saddno_x',
 'saddpref',
 'saddstname_x',
 'saddstr_x',
 'saddstsuf_x',
 'saddsttyp_x',
 'saledate_x',
 'saledatetx_x',
 'scity',
 'siteadd_x',
 'sourceagnt_x',
 'sourcedate_x',
 'sourcedatx_x',
 'sourceref_x',
 'sstate_x',
 'stcntyfips_x',
 'stfips_x',
 'stname_x',
 'struct_x',
 'structno',
 'structyear_x',
 'subdivisio',
 'subowntype',
 'subsurfown',
 'sunit',
 'szip',
 'transfdate_x',
 'layer',
 'path',
 'geometry_y',
 'alt alt parno (from CRS)',
 'Successful Merge']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)





all_2019_parcels.rename(columns = {'altparno_y': 'altparno','cntyfips_y': 'cntyfips','cntyname_y': 'cntyname','gisacres_y': 'gisacres',
                                   'improvval_y': 'improvval','landval_y': 'landval','legdecfull_y': 'ledgecfull','multistruc_y': 'multistruc',
                                   'ownname2_y': 'ownname2','parno_y': 'parno','parusecd2_y': 'parusecd2','parusecode_y': 'parusecode','parusedesc_y': 'parusedesc',
                                   'parval': 'parval','parvaltype_y': 'parvaltype','presentval_y': 'presentval','recareano_y': 'recareano',
                                   'recareatx_y': 'recareatx','revisedate_y': 'revisedate','reviseyear_y': 'reviseyear','saddno_y': 'saddno',
                                   'saddstname_y': 'saddstname','saddstr_y': 'saddstr','saddstsuf_y': 'saddstsuf','saddsttyp_y': 'saddsttyp',
                                   'saledate_y': 'saledate','saledatetx_y': 'saledatetx','sourceagnt_y': 'sourceagnt','sourcedate_y': 'sourcedate',
                                   'sourcedatx_y': 'sourcedatx','sourceref_y': 'sourceref','sstate_y': 'sstate','stcntyfips_y': 'stcntyfips','stfips_y': 'stfips',
                                   'stname_y': 'stname','struct_y': 'struct','structyear_y': 'structyear','transfdate_y': 'transfdate', 'geometry_x':'geometry'},
                                    inplace=True)


all_2019_parcels.rename(columns = {'mailadd_y':'mailadd','mcity_y':'mcity','ownname_y':'ownname','parval_y':'parval','state_y':'mstate','mzip_y':'mzip', 'siteadd_y':'siteadd','mstate_y':'mstate','nparno_x':'nparno'}, inplace=True)


all_2019_parcels['Property Type'] = all_2019_parcels['landval'] == all_2019_parcels['parval']

#change true/false values to 'Vacant Land' or no value. There are 95600 vacant land parcels.
all_2019_parcels.loc[(all_2019_parcels['Property Type'] == True), 'Property Type'] = 'Vacant Land'
all_2019_parcels.loc[(all_2019_parcels['Property Type'] == False), 'Property Type'] = ''


##Label others from Watauga County using parusedesc. Now there are 95790 vacant land parcels (added about 200 parcels)
all_2019_parcels = bwf.property_type_column(all_2019_parcels)

#make vacant land dataframe
vacant_land_df = all_2019_parcels[all_2019_parcels['Property Type'] == 'Vacant Land']
#drop non-vacant land parcels from all_2019_parcels
all_2019_parcels = all_2019_parcels[all_2019_parcels['Property Type'] != 'Vacant Land']

#apply filters to vacant land df
vacant_land_df = bwf.vacant_land_filters(vacant_land_df)
#we are left with 4788 vacant land parcels


condos_list_2019 = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList2019.xlsx')          #3139 parcels


#5. Label condo buildings as 'Property Type' = 'Condo Building'
#first, read in condos list
#uses condo_buildings_list function from BRE_condos_list folder (import statements at top)
condo_building_ids = module.condo_buildings_list(condos_list_2019)

#iterate over list (condo_building_ids) and add 'Property Type' of 'Condo Building'
all_2019_parcels.loc[all_2019_parcels['parno'].isin(condo_building_ids), 'Property Type'] = 'Condo Building'

#remove condo buildings from list
all_2019_parcels = all_2019_parcels.loc[all_2019_parcels['Property Type'] != 'Condo Building']



#export to shapefile
all_2019_parcels = gpd.GeoDataFrame(all_2019_parcels, geometry='geometry')
all_2019_parcels.to_file('/Users/ep9k/Desktop/all_2019_parcels.shp')
#move this to PostgreSQL database as new 'all_2019_parcels'

vacant_land_df = gpd.GeoDataFrame(vacant_land_df, geometry='geometry')
vacant_land_df.to_file('/Users/ep9k/Desktop/vacant_land.shp')
##FINAL RESULT FROM THIS IS allkeepers_2019 and vacant_land_df













