#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:23:30 2020

@author: ep9k
"""

""" This is the master workflow script I'm using for the 2019 Boone Real Estate mailing list

Following steps as outlines in Trello document: https://trello.com/b/Up0JxHMB/boone-real-estate"""


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


#1. Starting from scratch from original documents. This includes...
#   -Matt's original mailing list (MattOriginalMailingList.xlsx)
#   -Matt's original condo list (MattCondoAddressList2019.xlsx)
#   -All parcels (/Users/ep9k/Desktop/BRE/BRE 2019/All_Parcels_2019.gpkg)
#
original_mailing_list = pd.read_excel('/Users/ep9k/Desktop/BRE/BRE 2019/MattOriginalMailingList.xlsx')          #11,827 addresses
all_2019_parcels = gpd.read_file('/Users/ep9k/Desktop/BRE/BRE 2019/All_Parcels_2019.gpkg')                   #228,393 parcels
all_2018_parcels = pd.read_csv('/Users/ep9k/Desktop/BRE/2018Keepers.csv')                                    #17417 parcels
condos_list_2019 = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList2019.xlsx')          #3139 parcels



#2. Drop useless columns from all_2019_parcels to make data cleaner. Create Address columns to merge with original_mailing_list 
columns_to_drop = ['id_0', 'id', 'gnisid', 'maddpref', 'maddrno',
       'maddstname', 'maddstr', 'maddstsuf', 'maddsttyp', 'mapref', 
       'munit', 'ownfrst', 'ownlast', 'owntype', 'parusedsc2', 'revdatetx',
       'saddpref', 'scity', 'structno', 'subdivisio', 'subowntype', 'subsurfown', 'sunit',
       'szip', 'layer', 'path']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)



#3. MattOriginalMailing list is not actually his original, but it is a list I had from June 2019 with the 2+ removed, Subdivision, and Excluded Subdivision column in tact. 
##This had already been joined to the county parcels so I will merge based on the nparno
all_2019_parcels = all_2019_parcels.merge(original_mailing_list, how='left', left_on='nparno', right_on='nparno')
#
##drop useless columns from all_2019_parcels. All I want to keep after the merge is the 2+ removed, subdivision, and excluded subdivision columns

columns_to_drop = ['LAST NAME','FIRST NAME','MAILING ADDRESS','MAILING CITY','MAILING STATE','MAILING ZIPCODE','PARCEL VALUE','PROPERTY ADDRESS','sourceagnt_y','id_2','fid','id',
 'altparno_y','cntyfips_y','cntyname_y','gisacres_y','ownname2_y','gnisid','improvval_y','landval_y','legdecfull_y','maddpref','maddrno','maddstname',
 'maddstr','maddstsuf','mapref','multistruc_y','munit','maddsttyp','ownfrst','ownlast','owntype','parno_y','parusecd2_y','parusecode_y','parusedesc_y',
 'parusedsc2','parvaltype_y','presentval_y','recareano_y','recareatx_y','revdatetx','revisedate_y','reviseyear_y','saddno_y','saddpref','saddstname_y','saddstr_y',
 'saddstsuf_y','saddsttyp_y','saledate_y','saledatetx_y','scity','sourcedate_y','sourcedatx_y','sourceref_y','sstate_y','stcntyfips_y','stfips_y','stname_y',
 'struct_y','structno','structyear_y','subdivisio','subowntype','subsurfown','sunit','szip','transfdate_y','id_0','id_1','layer','path']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)

##the columns in all_2019_parcels get renamed (ex:altparno_x) so I rename them to keep things clean
all_2019_parcels.rename(columns = {'altparno_x': 'altparno','cntyfips_x': 'cntyfips','cntyname_x': 'cntyname','gisacres_x': 'gisacres',
                                   'improvval_x': 'improvval','landval_x': 'landval','legdecfull_x': 'ledgecfull','multistruc_x': 'multistruc',
                                   'ownname2_x': 'ownname2','parno_x': 'parno','parusecd2_x': 'parusecd2','parusecode_x': 'parusecode','parusedesc_x': 'parusedesc',
                                   'parval': 'parval','parvaltype_x': 'parvaltype','presentval_x': 'presentval','recareano_x': 'recareano',
                                   'recareatx_x': 'recareatx','revisedate_x': 'revisedate','reviseyear_x': 'reviseyear','saddno_x': 'saddno',
                                   'saddstname_x': 'saddstname','saddstr_x': 'saddstr','saddstsuf_x': 'saddstsuf','saddsttyp_x': 'saddsttyp',
                                   'saledate_x': 'saledate','saledatetx_x': 'saledatetx','sourceagnt_x': 'sourceagnt','sourcedate_x': 'sourcedate',
                                   'sourcedatx_x': 'sourcedatx','sourceref_x': 'sourceref','sstate_x': 'sstate','stcntyfips_x': 'stcntyfips','stfips_x': 'stfips',
                                   'stname_x': 'stname','struct_x': 'struct','structyear_x': 'structyear','transfdate_x': 'transfdate'},
                                    inplace=True)



#3. Create Vacant Land Property Type

#create 'Property Type' column and populate with true/false  alues
all_2019_parcels['Property Type'] = all_2019_parcels['landval'] == all_2019_parcels['parval']

#change true/false values to 'Vacant Land' or no value. There are 95593 vacant land parcels.
all_2019_parcels.loc[(all_2019_parcels['Property Type'] == True), 'Property Type'] = 'Vacant Land'
all_2019_parcels.loc[(all_2019_parcels['Property Type'] == False), 'Property Type'] = ''


##Label others from Watauga County using parusedesc. Now there are 95783 vacant land parcels (added about 200 parcels)
all_2019_parcels = bwf.property_type_column(all_2019_parcels)

#make vacant land dataframe
vacant_land_df = all_2019_parcels[all_2019_parcels['Property Type'] == 'Vacant Land']
#drop non-vacant land parcels from all_2019_parcels
all_2019_parcels = all_2019_parcels[all_2019_parcels['Property Type'] != 'Vacant Land']

#apply filters to vacant land df
vacant_land_df = bwf.vacant_land_filters(vacant_land_df)
#we are left with 4787 vacant land parcels



#4. Label condo buildings as 'Property Type' = 'Condo Building'
#first, read in condos list
#uses condo_buildings_list function from BRE_condos_list folder (import statements at top)
condo_building_ids = module.condo_buildings_list(condos_list_2019)

#iterate over list (condo_building_ids) and add 'Property Type' of 'Condo Building'
all_2019_parcels.loc[all_2019_parcels['parno'].isin(condo_building_ids), 'Property Type'] = 'Condo Building'

#remove condo buildings from list
all_2019_parcels = all_2019_parcels.loc[all_2019_parcels['Property Type'] != 'Vacant Land']


#export to shapefile
all_2019_parcels = gpd.GeoDataFrame(all_2019_parcels, geometry='geometry')
all_2019_parcels.to_file('/Users/ep9k/Desktop/all_2019_parcels.shp')
#move this to PostgreSQL database as new 'all_2019_parcels'

vacant_land_df = gpd.GeoDataFrame(vacant_land_df, geometry='geometry')
#vacant_land_df.to_file('/Users/ep9k/Desktop/vacant_land.shp')
##FINAL RESULT FROM THIS IS allkeepers_2019 and vacant_land_df




#5. GO TO QGIS/POSTGRESQL with the all_2019_parcels and do the zones + price filtering
#output of this is all_keepers2019
#Also with vacant_land_df, clip parcels to extent of AllZonesExtent
#output of this is vacant_land_keepers




