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
import numpy as np

#import condo_buildings_list function
MODULE_PATH = '/Users/ep9k/Desktop/BRE/BRE 2019/BRE_Condos_List/scripts/CountyFunctions.py'
MODULE_NAME = 'condo_buildings_list'
import importlib
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module 
spec.loader.exec_module(module)



##1. Starting from scratch from original documents. This includes...
##   -Matt's original mailing list (MattOriginalMailingList.xlsx)
##   -Matt's original condo list (MattCondoAddressList2019.xlsx)
##   -All parcels (/Users/ep9k/Desktop/BRE/BRE 2019/All_Parcels_2019.gpkg)
#
original_mailing_list = pd.read_excel('/Users/ep9k/Desktop/BRE/BRE 2019/MattOriginalMailingList.xlsx')          #11,827 addresses
all_2019_parcels = gpd.read_file('/Users/ep9k/Desktop/BRE/BRE 2019/All_Parcels_2019.gpkg')                   #228,393 parcels
all_2018_parcels = pd.read_csv('/Users/ep9k/Desktop/BRE/2018Keepers.csv')                                    #17417 parcels


#2. Drop useless columns from all_2019_parcels to make data cleaner. Create Address columns to merge with original_mailing_list 
columns_to_drop = ['id_0', 'id', 'gnisid', 'maddpref', 'maddrno',
       'maddstname', 'maddstr', 'maddstsuf', 'maddsttyp', 'mapref', 
       'munit', 'ownfrst', 'ownlast', 'owntype', 'parusedsc2', 'revdatetx',
       'saddpref', 'scity', 'structno', 'subdivisio', 'subowntype', 'subsurfown', 'sunit',
       'szip', 'layer', 'path']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)


###3. MattOriginalMailing list is not actually his original, but it is a list I had from June 2019 with the 2+ removed, Subdivision, and Excluded Subdivision column in tact. 
###This had already been joined to the county parcels so I will merge based on the nparno
all_2019_parcels = all_2019_parcels.merge(original_mailing_list, how='left', left_on='nparno', right_on='nparno')

##drop useless columns from all_2019_parcels. All I want to keep after the merge is the 2+ removed, subdivision, and excluded subdivision columns

columns_to_drop = ['LAST NAME','FIRST NAME','MAILING ADDRESS','MAILING CITY','MAILING STATE','MAILING ZIPCODE','PARCEL VALUE','PROPERTY ADDRESS','sourceagnt_y',
 'id_2', 'id','altparno_y','cntyfips_y','cntyname_y','gisacres_y','ownname2_y','gnisid','improvval_y','landval_y','legdecfull_y','maddpref',
 'maddrno','maddstname','maddstr','maddstsuf','mapref','multistruc_y','munit','maddsttyp','ownfrst','ownlast','owntype','parno_y','parusecd2_y',
 'parusecode_y','parusedesc_y','parusedsc2','parvaltype_y','presentval_y','recareano_y','recareatx_y','revdatetx','revisedate_y','reviseyear_y',
 'saddno_y','saddpref','saddstname_y','saddstr_y','saddstsuf_y','saddsttyp_y','saledate_y','saledatetx_y','scity','sourcedate_y','sourcedatx_y',
 'sourceref_y','sstate_y','stcntyfips_y','stfips_y','stname_y','struct_y','structno','structyear_y','subdivisio','subowntype','subsurfown','sunit',
 'szip','transfdate_y','id_0','id_1','layer','path']

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




#4. NOW GO TO QGIS/POSTGRESQL with the all_2019_parcels and do the zones + price filtering

#export to shapefile
#all_2019_parcels = gpd.GeoDataFrame(all_2019_parcels, geometry='geometry')
#move this to PostgreSQL database as new 'all_2019_parcels'

##FINAL RESULT FROM THIS IS allkeepers_2019



#5. Create other new columns. Gray out everything above!

#Start by reading in allkeepers_2019
all_keepers_2019 = gpd.read_file('/Users/ep9k/Desktop/BRE/BRE 2019/all_keepers_2019/all_keepers_2019.shp')

# This includes Property type ('Home', 'Vacant Land', 'Condo'). Owner Moved, Sold_In_Last_Year, No_Change, VacantLandValue (>100k and <200k)

#Start with Property Type column
all_keepers_2019.loc[(all_keepers_2019['parusedesc'] == 'RESIDENTIAL VACANT'), 'Property Type'] = 'Vacant Land'
all_keepers_2019.loc[(all_keepers_2019['parusedesc'] == 'AGRICULTURAL-VACANT'), 'Property Type'] = 'Vacant Land'
all_keepers_2019.loc[(all_keepers_2019['parusedesc'] == 'APARTMENT LAND VACANT'), 'Property Type'] = 'Vacant Land'
all_keepers_2019.loc[(all_keepers_2019['parusedesc'] == 'COMMERCIAL LAND VACANT'), 'Property Type'] = 'Vacant Land'
all_keepers_2019.loc[(all_keepers_2019['parusedesc'] == 'INDUSTRIAL TRACT VACANT'), 'Property Type'] = 'Vacant Land'
all_keepers_2019.loc[(all_keepers_2019['parusedesc'] == 'UTILITY VACANT LAND'), 'Property Type'] = 'Vacant Land'

#if landval = parval, it is vacant land. Meaning there is no structure on it. 
all_keepers_2019.loc[(all_keepers_2019['landval'] == all_keepers_2019['parval']), 'Property Type'] == 'Vacant Land'
#
#Make sure I got all Townhomes in Watauga County in condos list just in case
all_keepers_2019.loc[(all_keepers_2019['parusedesc'] == 'TOWNHOUSE'), 'Property Type'] = 'Townhome'

#all other parcels will be given the Property Type value of 'Home / Potentially not residential'. This includes a lot of non-residential properties but these will be filtered out later
all_keepers_2019.loc[all_keepers_2019['Property Type'].isnull(), 'Property Type'] = 'Home / Potentially Not Residential'


#These are the known residential parcel use codes from Watauga County only. I am re-labeling these as 'Home'
all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL 1 FAMILY', 'Property Type'] = 'Home'
all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL 2 FAMILY', 'Property Type'] = 'Home'
all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL 3 FAMILY', 'Property Type'] = 'Home'
all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL STRUCTURE ON COMMERCIAL LAND', 'Property Type'] = 'Home'
all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL UNDER CONSTRUCTION', 'Property Type'] = 'Home'
all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL UNDER CONSTRUCTION/LONG TERM', 'Property Type'] = 'Home'

#These are known undesirable 'parusecode' values (Only Watauga County). I'll compile a list of these and later drop rows with these values
bad_parusedesc = [ 'AGRICULTURAL-IMPROVED' , 'AGRICULTURAL-VACANT' , 'AMBULANCE SERVICE' , 'AMERICAN LEGION/ETC' , 'AMUSEMENT PARK' , 'APARTMENT - HIGH RISE' , 
                  'APARTMENT-GARDEN (1-3 STORIES)' , 'ASPHALT PLANT' , 'AUTO DEALERSHIP' , 'AUTO SERVICE GARAGE' , 'AUXILIARY IMPROVEMENT' , 'BANK' , 
                  'BOARDING/ROOMING HOUSE' , 'BOWLING ALLEY' , 'CAR WASH (AUTOMATIC)' , 'CAR WASH (MANUAL)' , 'CEMENT MFG.' , 'CHARITABLE (ALL OTHER)' , 'CHARITABLE (HOMES)' , 
                  'CHARITABLE (HOSPITAL)' , 'CLUB HOUSE' , 'COMMERCIAL AUXILIARY IMPROVEMENT' , 'COMMERCIAL LAND VACANT' , 'COMMERCIAL UNDER CONSTRUCTION' , 'COMMUNITY SHOPPING CENTER' , 
                  'CONCRETE MFG.' , 'CONDOMINIUM (COMMON AREA)' , 'CONVENIENCE STORE' , 'COUNTRY CLUB WITHOUT GOLF COURSE' , 'DAY CARE CENTER' , 'DEPARTMENT STORE' , 
                  'DISCOUNT DEPARTMENT STORE' , 'DOWNTOWN ROW TYPE' , 'EDUCATION' , 'EDUCATION RELIGIOUS' , 'ELECTRIC UTILITY' , 'EXCLUSIONS (ALL OTHERS)' , 'EXCLUSIONS (COMMONE AREAS)' , 
                  'EXEMPTIONS (ALL OTHERS)' , 'EXEMPTIONS (CEMETERY)' , 'FAST FOOD' , 'FOOD STAND' , 'FUNERAL HOME' , 'FURNITURE MFG.' , 'GOLF COURSE' , 'GOVERNMENT' , 'HEALTH SPA' , 
                  'HOTEL HIGH RISE W/O LOUNGE OR RESTAURANT' , 'HOTEL HIGH RISE WITH LOUNGE OR RESTAURANT' , 'HOTEL LOW RISE W/O LOUNGE OR RESTAURANT' , 'INDUSTRIAL TRACT VACANT' , 
                  'LEATHER PRODUCTS MFG.' , 'LUMBER STORAGE FACILITY' ,  'MANUFACTURING/PROCESSING' , 'MEAT PACKING & SLAUGHTERHOUSE' , 'MEDICAL OFFICE' , 'METAL WORKING' , 'MINI WAREHOUSE' , 
                  'MISCELLANEOUS AMUSEMENT' ,  'MOTEL LOW RISE WITH LOUNGE OR RESTAURANT' , 'NEWSPAPER PLANT' , 'NON-EX-SCHOOL' , 'NURSING/CONVALESCENT HOME' , 'OFFICE BUILDING LOW RISE (1-4 ST)' , 
                  'OFFICE CONDOMINIUMS' , 'OFFICE/RETAIL' , 'PAR 3 GOLF COURSE' , 'PARKING (MISCELLANEOUS)' , 'REGIONAL SHOPPING MALL' , 'RELIGIOUS' , 'RESTAURANT' , 
                  'RETAIL - MULTIPLE OCCUPANCY' , 'RETAIL - SINGLE OCCUPANCY' , 'RETAIL CONDOMINIUM'  'SAVINGS INSTITUTION' , 'SERVICE STATION WITH BAYS' , 'SERVICE STATION WITHOUT BAYS' , 
                  'SKATING RINK' , 'SOCIAL/FRATERNAL HALL' , 'STONE/MINERAL QUARRY' , 'STRIP SHOPPING CENTER' , 'SUPERMARKET' , 'TELEPHONE UTILITY NEC' , 'TENNIS CLUB INDOOR' , 'TRUCK TERMINAL' , 
                  'UNSOUND COMM. STRUCTURE' , 'UTILITY VACANT LAND' , 'VETERINARY CLINIC' , 'WAREHOUSE' , 'WAREHOUSE WITH INTERIOR OFFICE SPACE' , 'WAREHOUSE-PREFABRICATED' , 'WATER AMUSEMENT' , 
                  'WOODWORKING SHOP' ]

#drop rows with these parusedesc from all_keepers_2019. Drops 1719 columns
for parusedesc in bad_parusedesc:
    all_keepers_2019.drop(all_keepers_2019[all_keepers_2019['parusedesc'] == parusedesc].index, inplace=True)



##Now Create 'VacantLandValue' column for parcels >$100k and >$200k
all_keepers_2019.loc[(all_keepers_2019['Property Type'] == 'Vacant Land') & (all_keepers_2019['parval'] > 100000), 'Vacant Land Value'] = '> $100k'
all_keepers_2019.loc[(all_keepers_2019['Property Type'] == 'Vacant Land') & (all_keepers_2019['parval'] > 200000), 'Vacant Land Value'] = '> $200k'


#convert 'saledate' column to datetime
all_keepers_2019['saledate'] = pd.to_datetime(all_keepers_2019['saledate'])
all_keepers_2019['Sold In Last Year'] = all_keepers_2019['saledate'].dt.year >= 2018
all_keepers_2019['Sold In Last Year'] = all_keepers_2019['Sold In Last Year'].replace(True, 'Yes')        
all_keepers_2019['Sold In Last Year'] = all_keepers_2019['Sold In Last Year'].replace(False, '')


#Create the 'owner moved' column by comparing the 2018 Mailing Address to the 2019 Mailing Address
#First build full Mailing Address column for 2018 data
all_2018_parcels['FullMailAddress_2018'] = all_2018_parcels['MAILING ADDRESS'] + ' ' + all_2018_parcels['MAILING CITY'] + ' ' + all_2018_parcels['MAILING STATE']
all_2018_parcels['FullMailAddress_2018'] = all_2018_parcels['FullMailAddress_2018'].str.replace(' ','')   #got rid of all spaces for simplicity

#build full mailing address for all_2019_parcels
all_keepers_2019['FullMailingAddress_2019'] = all_keepers_2019['mailadd'] + ' ' + all_keepers_2019['mcity'] + ' ' + all_keepers_2019['mstate']
all_keepers_2019['FullMailingAddress_2019'] = all_keepers_2019['FullMailingAddress_2019'].str.replace(' ','')   #got rid of all spaces for simplicity


#COME BACK TO THIS. OWNER MOVED COLUMN
###compare 2018 mailing address to 2019 mailing address
#all_keepers_2019['FullMail2018'] = all_2018_parcels['FullMailAddress_2018']
##compare 2019 mail address to 2018 mail address to see if there are changes
#all_keepers_2019['Owner Moved'] = np.where(all_keepers_2019['FullMailingAddress_2019'] != all_keepers_2019['FullMail2018'], 'Yes', 'No')




# 6. Drop Condo Buildings from all_keepers_2019

#first, read in condos list
condos_list_2019 = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList2019.xlsx')

#uses condo_buildings_list function from BRE_condos_list folder (import statements at top)
condo_building_ids = module.condo_buildings_list(condos_list_2019)

#iterate over list (condo_building_ids) and drop matching parcel numbers
#for building_id in condo_building_ids:
#    all_keepers_2019.drop(all_keepers_2019[all_keepers_2019['parno'] == building_id].index, inplace=True)

#iterate over list (condo_building_ids) and add 'Condo Building' value to Property Type column
all_keepers_2019.loc[all_keepers_2019['parno'].isin(condo_building_ids), 'Property Type'] = 'Condo Building'
###START HERE






##5. Now I want to merge to condos list to the all_2019_parcels 
#
##I try to merge via several columns. First is parno/Parcel ID
#all_2019_parcels = all_2019_parcels.merge(original_condo_list, how='left', left_on='parno', right_on='Parcel ID')
#all_2019_parcels.loc[all_2019_parcels['Removed'].notnull(), 'CondoList Removed'] = all_2019_parcels['Removed']    #this preserved the 'Removed' column by moving it to a new column 'CondoList Removed'
#all_2019_parcels.loc[all_2019_parcels['Unit #'].notnull(), 'CondoList Unit #'] = all_2019_parcels['Unit #']       #this preserved the 'Unit #' column by moving it to a new column 'CondoList Unit #'
#all_2019_parcels.loc[all_2019_parcels['Subdivsion'].notnull(), 'CondoList Subdivision'] = all_2019_parcels['Subdivsion']       #this preserved the 'Subdivsion' column by moving it to a new column 'CondoList Subdivision'
#
#results1 = all_2019_parcels.loc[all_2019_parcels['Parcel ID'].notnull()]                          #629 unique results
#
##now drop all unneeded columns
#
#columns_to_drop = ['Parcel ID','Last Name','First Name','Mailing #','Mailing Address','Mailing City','Removed','Property #','Property Address',
#                   'Unit #','Subdivsion','Property City','Property State','Property Zipcode','Mailing State','Mailing Zipcode','Returned',
#                   'Bad Address','Section','Zone','Mad Children','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26',
#                   'Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32','Unnamed: 33','Unnamed: 34','Unnamed: 35',
#                   'Unnamed: 36','Unnamed: 37','Unnamed: 38']
#
#all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)
#
#
##Now try to merge after stripping the dashes from Parcel ID field and then join altparno/Parcel ID Stripped
#original_condo_list['Parcel ID Stripped'] = original_condo_list['Parcel ID'].str.replace('-','')
#all_2019_parcels = all_2019_parcels.merge(original_condo_list, how='left', left_on='altparno', right_on='Parcel ID Stripped')
#all_2019_parcels.loc[all_2019_parcels['Removed'].notnull(), 'CondoList Removed'] = all_2019_parcels['Removed']    #this preserved the 'Removed' column by moving it to a new column 'CondoList Removed'
#all_2019_parcels.loc[all_2019_parcels['Unit #'].notnull(), 'CondoList Unit #'] = all_2019_parcels['Unit #']       #this preserved the 'Unit #' column by moving it to a new column 'CondoList Unit #'
#all_2019_parcels.loc[all_2019_parcels['Subdivsion'].notnull(), 'CondoList Subdivision'] = all_2019_parcels['Subdivsion']       #this preserved the 'Subdivsion' column by moving it to a new column 'CondoList Subdivision'
#
#results2 = all_2019_parcels.loc[all_2019_parcels['Parcel ID'].notnull()]                          #612 unique results             
#
##now drop all unneeded columns
#
#columns_to_drop = ['Parcel ID','Last Name','First Name','Mailing #','Mailing Address','Mailing City','Removed','Property #','Property Address',
#                   'Unit #','Subdivsion','Property City','Property State','Property Zipcode','Mailing State','Mailing Zipcode','Returned',
#                   'Bad Address','Section','Zone','Mad Children','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26',
#                   'Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32','Unnamed: 33','Unnamed: 34','Unnamed: 35',
#                   'Unnamed: 36','Unnamed: 37','Unnamed: 38', 'Parcel ID Stripped']
#
#all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)
#
#
##Now try to merge just the first 12 characters of condos 'Parcel ID' and compare to 'parno'
#original_condo_list['Parcel ID Shortened'] = original_condo_list['Parcel ID'].str[:12]
#all_2019_parcels = all_2019_parcels.merge(original_condo_list, how='left', left_on='parno', right_on='Parcel ID Shortened')
#all_2019_parcels.loc[all_2019_parcels['Removed'].notnull(), 'CondoList Removed'] = all_2019_parcels['Removed']    #this preserved the 'Removed' column by moving it to a new column 'CondoList Removed'
#all_2019_parcels.loc[all_2019_parcels['Unit #'].notnull(), 'CondoList Unit #'] = all_2019_parcels['Unit #']       #this preserved the 'Unit #' column by moving it to a new column 'CondoList Unit #'
#all_2019_parcels.loc[all_2019_parcels['Subdivsion'].notnull(), 'CondoList Subdivision'] = all_2019_parcels['Subdivsion']       #this preserved the 'Subdivsion' column by moving it to a new column 'CondoList Subdivision'
#
#results3 = all_2019_parcels.loc[all_2019_parcels['Parcel ID'].notnull()]                          #711 unique results             
#
##now drop all unneeded columns
#
#columns_to_drop = ['Parcel ID','Last Name','First Name','Mailing #','Mailing Address','Mailing City','Removed','Property #','Property Address',
#                   'Unit #','Subdivsion','Property City','Property State','Property Zipcode','Mailing State','Mailing Zipcode','Returned',
#                   'Bad Address','Section','Zone','Mad Children','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26',
#                   'Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32','Unnamed: 33','Unnamed: 34','Unnamed: 35',
#                   'Unnamed: 36','Unnamed: 37','Unnamed: 38', 'Parcel ID Stripped', 'Parcel ID Shortened']
#
#all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)
#
#
##Some parcels match to a certain point (first 15 characters)
#original_condo_list['Parcel ID 15'] = original_condo_list['Parcel ID'].str[:15]
#all_2019_parcels = all_2019_parcels.merge(original_condo_list, how='left', left_on=all_2019_parcels['parno'].str[:15], right_on='Parcel ID 15')
#all_2019_parcels.loc[all_2019_parcels['Removed'].notnull(), 'CondoList Removed'] = all_2019_parcels['Removed']    #this preserved the 'Removed' column by moving it to a new column 'CondoList Removed'
#all_2019_parcels.loc[all_2019_parcels['Unit #'].notnull(), 'CondoList Unit #'] = all_2019_parcels['Unit #']       #this preserved the 'Unit #' column by moving it to a new column 'CondoList Unit #'
#all_2019_parcels.loc[all_2019_parcels['Subdivsion'].notnull(), 'CondoList Subdivision'] = all_2019_parcels['Subdivsion']       #this preserved the 'Subdivsion' column by moving it to a new column 'CondoList Subdivision'
#
#results4 = all_2019_parcels.loc[all_2019_parcels['Parcel ID'].notnull()]                          #1735 unique results             
#
#columns_to_drop = ['Parcel ID','Last Name','First Name','Mailing #','Mailing Address','Mailing City','Removed','Property #','Property Address',
#                   'Unit #','Subdivsion','Property City','Property State','Property Zipcode','Mailing State','Mailing Zipcode','Returned',
#                   'Bad Address','Section','Zone','Mad Children','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26',
#                   'Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32','Unnamed: 33','Unnamed: 34','Unnamed: 35',
#                   'Unnamed: 36','Unnamed: 37','Unnamed: 38', 'Parcel ID Stripped', 'Parcel ID Shortened', 'Parcel ID 15']
#
#all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)
#

#
#
#
#
######TODO: CREATE 'owner_moved','sold_in_last_year', 'no_change' columns 
#
#
#
#
#
#
#
#
#
##lastly, drop duplicate parcels
#all_2019_parcels.drop_duplicates(inplace=True)


