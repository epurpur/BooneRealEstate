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

columns_to_drop = ['MAILING ADDRESS','MAILING CITY','MAILING STATE','MAILING ZIPCODE','PARCEL VALUE','PROPERTY ADDRESS','sourceagnt_y','id_2','fid','id',
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



#3. Label condo buildings as 'Property Type' = 'Condo Building'
#first, read in condos list
#uses condo_buildings_list function from BRE_condos_list folder (import statements at top)
condo_building_ids = module.condo_buildings_list(condos_list_2019)

#iterate over list (condo_building_ids) and add 'Property Type' of 'Condo Building'
all_2019_parcels.loc[all_2019_parcels['parno'].isin(condo_building_ids), 'Property Type'] = 'Condo Building'



#4. Create Vacant Land Property Type

#Start with Property Type column
all_2019_parcels.loc[(all_2019_parcels['parusedesc'] == 'RESIDENTIAL VACANT'), 'Property Type'] = 'Vacant Land'
all_2019_parcels.loc[(all_2019_parcels['parusedesc'] == 'AGRICULTURAL-VACANT'), 'Property Type'] = 'Vacant Land'
all_2019_parcels.loc[(all_2019_parcels['parusedesc'] == 'APARTMENT LAND VACANT'), 'Property Type'] = 'Vacant Land'
all_2019_parcels.loc[(all_2019_parcels['parusedesc'] == 'COMMERCIAL LAND VACANT'), 'Property Type'] = 'Vacant Land'
all_2019_parcels.loc[(all_2019_parcels['parusedesc'] == 'INDUSTRIAL TRACT VACANT'), 'Property Type'] = 'Vacant Land'
all_2019_parcels.loc[(all_2019_parcels['parusedesc'] == 'UTILITY VACANT LAND'), 'Property Type'] = 'Vacant Land'

########START HERE
#if landval = parval, it is vacant land. Meaning there is no structure on it.  There are 17998 vacant land parcels in total 
all_2019_parcels.loc[(all_2019_parcels['landval'] == all_2019_parcels['parval']), 'Property Type'] == 'Vacant Land'

#make new dataframe with just vacant land parcels
#vacant_land_df = all_2019_parcels.loc[all_2019_parcels['Property Type'] == 'Vacant Land']
#
##drop non-vacant land parcels from all_2019_parcels
#all_2019_parcels = all_2019_parcels[all_2019_parcels['Property Type'] != 'Vacant Land']
#
##vacant land filters: 1-10 acres and >100k. >10acres and >200k. 'gisacres' column
#filter1 = vacant_land_df.loc[(vacant_land_df['gisacres'] > 1) & (vacant_land_df['gisacres'] < 10) & (vacant_land_df['parval'] > 100000)]
#filter2 = test2 = vacant_land_df.loc[(vacant_land_df['gisacres'] > 10) & (vacant_land_df['parval'] > 200000)]
#
#vacant_land_df = pd.concat([filter1, filter2])




#5. GO TO QGIS/POSTGRESQL with the all_2019_parcels and do the zones + price filtering

#export to shapefile
#all_2019_parcels = gpd.GeoDataFrame(all_2019_parcels, geometry='geometry')
#move this to PostgreSQL database as new 'all_2019_parcels'

##FINAL RESULT FROM THIS IS allkeepers_2019

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#6. Create other new columns. Gray out everything above!

#Start by reading in allkeepers_2019
#all_keepers_2019 = gpd.read_file('/Users/ep9k/Desktop/BRE/BRE 2019/all_keepers_2019/all_keepers_2019.gpkg')



# This includes Property type ('Home', 'Vacant Land', 'Condo'). VacantLandValue (>100k and <200k)

#rename 'property t' column (I am not sure why it becomes this after Postgres Filtering)
#all_keepers_2019['Property Type'] = all_keepers_2019['property t']
##drop 'property t' column
#all_keepers_2019.drop('property t', inplace=True, axis=1)

##drop townhomes. The vast majority of these are already in Matt's Condo list
#all_keepers_2019 = all_keepers_2019[all_keepers_2019['parusedesc'] != 'TOWNHOUSE']
###Make sure I got all Townhomes in Watauga County in condos list just in case
###all_keepers_2019.loc[(all_keepers_2019['parusedesc'] == 'TOWNHOUSE'), 'Property Type'] = 'Townhome'



##all other parcels will be given the Property Type value of 'Home / Potentially not residential'. This includes a lot of non-residential properties but these will be filtered out later
#all_keepers_2019.loc[all_keepers_2019['Property Type'].isnull(), 'Property Type'] = 'Home / Potentially Not Residential'
#
#
##These are the known residential parcel use codes from Watauga County only. I am re-labeling these as 'Home'
#all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL 1 FAMILY', 'Property Type'] = 'Home'
#all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL 2 FAMILY', 'Property Type'] = 'Home'
#all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL 3 FAMILY', 'Property Type'] = 'Home'
#all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL STRUCTURE ON COMMERCIAL LAND', 'Property Type'] = 'Home'
#all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL UNDER CONSTRUCTION', 'Property Type'] = 'Home'
#all_keepers_2019.loc[all_keepers_2019['parusedesc'] == 'RESIDENTIAL UNDER CONSTRUCTION/LONG TERM', 'Property Type'] = 'Home'
#
#
##These are known undesirable 'parusecode' values (Only Watauga County). I'll compile a list of these and later drop rows with these values
#bad_parusedesc = [ 'AGRICULTURAL-IMPROVED' , 'AGRICULTURAL-VACANT' , 'AMBULANCE SERVICE' , 'AMERICAN LEGION/ETC' , 'AMUSEMENT PARK' , 'APARTMENT - HIGH RISE' , 
#                  'APARTMENT-GARDEN (1-3 STORIES)' , 'ASPHALT PLANT' , 'AUTO DEALERSHIP' , 'AUTO SERVICE GARAGE' , 'AUXILIARY IMPROVEMENT' , 'BANK' , 
#                  'BOARDING/ROOMING HOUSE' , 'BOWLING ALLEY' , 'CAR WASH (AUTOMATIC)' , 'CAR WASH (MANUAL)' , 'CEMENT MFG.' , 'CHARITABLE (ALL OTHER)' , 'CHARITABLE (HOMES)' , 
#                  'CHARITABLE (HOSPITAL)' , 'CLUB HOUSE' , 'COMMERCIAL AUXILIARY IMPROVEMENT' , 'COMMERCIAL LAND VACANT' , 'COMMERCIAL UNDER CONSTRUCTION' , 'COMMUNITY SHOPPING CENTER' , 
#                  'CONCRETE MFG.' , 'CONDOMINIUM (COMMON AREA)' , 'CONVENIENCE STORE' , 'COUNTRY CLUB WITHOUT GOLF COURSE' , 'DAY CARE CENTER' , 'DEPARTMENT STORE' , 
#                  'DISCOUNT DEPARTMENT STORE' , 'DOWNTOWN ROW TYPE' , 'EDUCATION' , 'EDUCATION RELIGIOUS' , 'ELECTRIC UTILITY' , 'EXCLUSIONS (ALL OTHERS)' , 'EXCLUSIONS (COMMONE AREAS)' , 
#                  'EXEMPTIONS (ALL OTHERS)' , 'EXEMPTIONS (CEMETERY)' , 'FAST FOOD' , 'FOOD STAND' , 'FUNERAL HOME' , 'FURNITURE MFG.' , 'GOLF COURSE' , 'GOVERNMENT' , 'HEALTH SPA' , 
#                  'HOTEL HIGH RISE W/O LOUNGE OR RESTAURANT' , 'HOTEL HIGH RISE WITH LOUNGE OR RESTAURANT' , 'HOTEL LOW RISE W/O LOUNGE OR RESTAURANT' , 'INDUSTRIAL TRACT VACANT' , 
#                  'LEATHER PRODUCTS MFG.' , 'LUMBER STORAGE FACILITY' ,  'MANUFACTURING/PROCESSING' , 'MEAT PACKING & SLAUGHTERHOUSE' , 'MEDICAL OFFICE' , 'METAL WORKING' , 'MINI WAREHOUSE' , 
#                  'MISCELLANEOUS AMUSEMENT' ,  'MOTEL LOW RISE WITH LOUNGE OR RESTAURANT' , 'NEWSPAPER PLANT' , 'NON-EX-SCHOOL' , 'NURSING/CONVALESCENT HOME' , 'OFFICE BUILDING LOW RISE (1-4 ST)' , 
#                  'OFFICE CONDOMINIUMS' , 'OFFICE/RETAIL' , 'PAR 3 GOLF COURSE' , 'PARKING (MISCELLANEOUS)' , 'REGIONAL SHOPPING MALL' , 'RELIGIOUS' , 'RESTAURANT' , 
#                  'RETAIL - MULTIPLE OCCUPANCY' , 'RETAIL - SINGLE OCCUPANCY' , 'RETAIL CONDOMINIUM'  'SAVINGS INSTITUTION' , 'SERVICE STATION WITH BAYS' , 'SERVICE STATION WITHOUT BAYS' , 
#                  'SKATING RINK' , 'SOCIAL/FRATERNAL HALL' , 'STONE/MINERAL QUARRY' , 'STRIP SHOPPING CENTER' , 'SUPERMARKET' , 'TELEPHONE UTILITY NEC' , 'TENNIS CLUB INDOOR' , 'TRUCK TERMINAL' , 
#                  'UNSOUND COMM. STRUCTURE' , 'UTILITY VACANT LAND' , 'VETERINARY CLINIC' , 'WAREHOUSE' , 'WAREHOUSE WITH INTERIOR OFFICE SPACE' , 'WAREHOUSE-PREFABRICATED' , 'WATER AMUSEMENT' , 
#                  'WOODWORKING SHOP' ]
#
##drop rows with these parusedesc from all_keepers_2019. Drops 1719 rows
#for parusedesc in bad_parusedesc:
#    all_keepers_2019.drop(all_keepers_2019[all_keepers_2019['parusedesc'] == parusedesc].index, inplace=True)
#
#
#
###Now Create 'VacantLandValue' column for parcels >$100k and >$200k
#all_keepers_2019.loc[(all_keepers_2019['Property Type'] == 'Vacant Land') & (all_keepers_2019['parval'] > 100000), 'Vacant Land Value'] = '> $100k'
#all_keepers_2019.loc[(all_keepers_2019['Property Type'] == 'Vacant Land') & (all_keepers_2019['parval'] > 200000), 'Vacant Land Value'] = '> $200k'
#
##
#
##Create the 'owner moved' column by comparing the 2018 Mailing Address to the 2019 Mailing Address
##First build full Mailing Address column for 2018 data
#all_2018_parcels['FullMailAddress_2018'] = all_2018_parcels['MAILING ADDRESS'] + ' ' + all_2018_parcels['MAILING CITY'] + ' ' + all_2018_parcels['MAILING STATE']
#all_2018_parcels['FullMailAddress_2018'] = all_2018_parcels['FullMailAddress_2018'].str.replace(' ','')   #got rid of all spaces for simplicity
#
##build full mailing address for all_2019_parcels
#all_keepers_2019['FullMailingAddress_2019'] = all_keepers_2019['mailadd'] + ' ' + all_keepers_2019['mcity'] + ' ' + all_keepers_2019['mstate']
#all_keepers_2019['FullMailingAddress_2019'] = all_keepers_2019['FullMailingAddress_2019'].str.replace(' ','')   #got rid of all spaces for simplicity
#
#
##COME BACK TO THIS. OWNER MOVED COLUMN
###compare 2018 mailing address to 2019 mailing address
##all_keepers_2019['FullMail2018'] = all_2018_parcels['FullMailAddress_2018']
##compare 2019 mail address to 2018 mail address to see if there are changes
##all_keepers_2019['Owner Moved'] = np.where(all_keepers_2019['FullMailingAddress_2019'] != all_keepers_2019['FullMail2018'], 'Yes', 'No')
#
#
#
#
## 7. Drop remaining Condo Buildings from all_keepers_2019
#
##iterate over list (condo_building_ids) and drop matching parcel numbers
#all_keepers_2019 = all_keepers_2019[all_keepers_2019['Property Type'] != 'Condo Building']     #only 6 remaining buildings
#
#
#
#
##8. Make list of known bad owner names from 'ownname' column
##read in bad owner names. This is instead of manually sorting at the end which is haphazard and inconsistent.
#bad_owner_names = ['U S A FOREST SERVICE','UNITED COMMUNITY BANK','UNITED STATES AGRICULTURE','UNITED STATES DEPT OF INTERIOR','UNITED STATES FOREST SERVICE','UNITED STATES OF AMERICA','UNIVERSITY OF MOUNT OLIVE INC','UPPER MOUNTAIN RESEARCH STATION','USA','USA % BLUE RIDGE PARKWAY SUPT','ALLEGHANY COUNTY',
#                   'ALLEGHANY COUNTY BOARD OF EDUCATION','ALLEGHANY COUNTY COURTHOUSE','ALLEGHANY MEMORIAL HOSPITAL','ALLEGHANY WELLNESS CENTER INC.','APPALACHIAN CHURCH INC','APPALACHIAN REGIONAL HEALTCARE SYS INC','APPALACHIAN SKI MTN INC','APPALACHIAN STATE UNIVERSITY','APPALACHIAN STATE UNIVERSITY FOUNDATION & ET AL',
#                   'ASHE COUNTY OF','ASHE COUNTY TRANSPORTATION AUTHORITY','ASHE FEDERAL BANK','APPALACHIAN CHURCH INC','BAILEYS CAMP BAPTIST CHURCH','BALD MOUNTAIN BAPTIST CHURCH INC.','BALDWIN COMMUNITY CHURCH','BANNER ELK PRESBYTERIAN CHURCH','BEAVER CREEK CHRISTIAN CHURCH INC','BETHANY UNITED METHODIST CHURCH','BETHEL BAPTIST CHURCH',
#                   'BIG FLATTS BAPTIST CHURCH','BLUE RIDGE MOUNTAIN CHURCH ASSOCIATION','BRISTOL BAPTIST CHURCH','BUFFALO MISSIONARY BAPTIST CHURCH','CALVARY FREE-WILL BAPTIST CHURCH','CALVARY FREEWILL BAPTIST CHURCH','CHURCH OF JESUS CHRIST TRUSTEES','CHURCH OF THE BRETHERN CAMP','COVENANT REFORMED CHURCH',
#                   'CROSSNORE FIRST BAPTIST CHURCH','CROSSNORE PRESBYTERIAN CHURCH','EMMANUEL BAPTIST CHURCH','EMMANUEL BAPTIST CHURCH-TRUSTEES','FALL CREEK BAPTIST CHURCH','FIRST BAPTIST CHURCH - NEWLAND','FIRST BAPTIST CHURCH OF SPARTA TRUSTEES','FLETCHER MEMORIAL BAPTIST CHURCH','FRIENDLY GROVE BAPTIST CHURCH',
#                   'FRIENDSHIP BAPTIST CHURCH OF','HEATON CHRISTIAN CHURCH','JEFFERSON UNITED METHODIST CHURCH','LAUREL KNOB BAPTIST CHURCH','LIBERTY GROVE BAPTIST CHURCH &','LIGHTHOUSE MISSIONARY BAPTIST CHURCH','MIDWAY BAPTIST CHURCH','MORAVIAN CHURCH','MORAVIAN CHURCH IN AMERICA SOUTHERN PROV',
#                   'MOUNT CALVARY BAPTIST CHURCH','MT JEFFERSON BAPTIST CHURCH INC.','MT JEFFERSON PRESBYTERIAN CHURCH','MT PADDY CHURCH INC','MT. ZION UNITED METHODIST CHURCH OF ALLEGHANY','NEW HOPEWELL BAPTIST CHURCH','NEWLAND PRESBYTERIAN CHURCH','NORTH BEAVER BAPTIST CHURCH','OBIDS BAPTIST CHURCH',
#                   'OLD FIELDS BAPTIST CHURCH -CECIL','PINEY RIDGE BAPTIST CHURCH','SEVENTH DAY ADVENT CHURCH','SHILOH UNITED METHODIST CHURCH','SMETHPORT BAPTIST CHURCH','SMETHPORT METHODIST CHURCH TRUSTEES','SOUTH BEAVER BAPTIST CHURCH','SOUTH FORK BAPTIST CHURCH &','SPARTA PRESBYTERIAN CHURCH',
#                   'SPARTA UNITED METHODIST CHURCH','ST. FRANCIS CATHOLIC CHURCH','STONY HILL BAPTIST CHURCH','TUCKERDALE BAPTIST CHURCH','WEST JEFFERSON CHURCH OF CHRIST','WEST JEFFERSON METHODIST CHURCH','ZION METHODIST CHURCH','APPALACHIAN CHURCH INC','BAILEYS CAMP BAPTIST CHURCH','BALD MOUNTAIN BAPTIST CHURCH INC.',
#                   'BALDWIN COMMUNITY CHURCH','BANNER ELK PRESBYTERIAN CHURCH','BEAVER CREEK CHRISTIAN CHURCH INC','BETHANY UNITED METHODIST CHURCH','BETHEL BAPTIST CHURCH','BIG FLATTS BAPTIST CHURCH','BLUE RIDGE MOUNTAIN CHURCH ASSOCIATION','BRISTOL BAPTIST CHURCH','BUFFALO MISSIONARY BAPTIST CHURCH',
#                   'CALVARY FREE-WILL BAPTIST CHURCH','CALVARY FREEWILL BAPTIST CHURCH','CHURCH OF JESUS CHRIST TRUSTEES','CHURCH OF THE BRETHERN CAMP','CROSSNORE FIRST BAPTIST CHURCH','CROSSNORE PRESBYTERIAN CHURCH','EMMANUEL BAPTIST CHURCH','EMMANUEL BAPTIST CHURCH-TRUSTEES','FALL CREEK BAPTIST CHURCH',
#                   'FIRST BAPTIST CHURCH - NEWLAND','FIRST BAPTIST CHURCH OF SPARTA TRUSTEES','FLETCHER MEMORIAL BAPTIST CHURCH','FRIENDLY GROVE BAPTIST CHURCH','FRIENDSHIP BAPTIST CHURCH OF','HEATON CHRISTIAN CHURCH','JEFFERSON UNITED METHODIST CHURCH','LAUREL KNOB BAPTIST CHURCH','LIBERTY GROVE BAPTIST CHURCH &',
#                   'LIGHTHOUSE MISSIONARY BAPTIST CHURCH','MIDWAY BAPTIST CHURCH','MINNEAPOLIS BAPTIST CHURCH CHAMP YOUNG & DENNIS KING &','MORAVIAN CHURCH','MORAVIAN CHURCH IN AMERICA SOUTHERN PROV','MOUNT CALVARY BAPTIST CHURCH','MT JEFFERSON BAPTIST CHURCH INC.','MT JEFFERSON PRESBYTERIAN CHURCH',
#                   'MT PADDY CHURCH INC','MT. ZION UNITED METHODIST CHURCH OF ALLEGHANY','NEW HOPEWELL BAPTIST CHURCH','NEWLAND PRESBYTERIAN CHURCH','NORTH BEAVER BAPTIST CHURCH','OBIDS BAPTIST CHURCH','OLD FIELDS BAPTIST CHURCH -CECIL','PINEY RIDGE BAPTIST CHURCH','PRUITT VIRGINIA CHURCH','SEVENTH DAY ADVENT CHURCH',
#                   'SHILOH UNITED METHODIST CHURCH','SMETHPORT BAPTIST CHURCH','SMETHPORT METHODIST CHURCH TRUSTEES','SOUTH BEAVER BAPTIST CHURCH','SOUTH FORK BAPTIST CHURCH &','SPARTA PRESBYTERIAN CHURCH','SPARTA UNITED METHODIST CHURCH','ST. FRANCIS CATHOLIC CHURCH','STONY HILL BAPTIST CHURCH',
#                   'TUCKERDALE BAPTIST CHURCH','UPCHURCH LEWIS MARVIN JR & BETTY DANIEL (TRUSTEES)','WEST JEFFERSON CHURCH OF CHRIST','WEST JEFFERSON METHODIST CHURCH','ZION METHODIST CHURCH','COUNTY OF AVERY','COUNTY OF AVERY, NORTH CAROLINA','AVERY COUNTY BOARD OF EDUCATION','COUNTY OF AVERY',
#                   'COUNTY OF AVERY NORTH CAROLINA','ASHE COUNTY OF','ASHE FEDERAL BANK','COUNTY OF ASHE','ASHE COUNTY BOARD OF EDUCATION','ASHE COUNTY OF','ASHE COUNTY TRANSPORTATION AUTHORITY','ASHE COUNTY WILDLIFE CLUB INC','ASHE FEDERAL BANK','ASHE MEMORIAL HOSPITAL INC','CARTER COUNTY BANK','WILKES COMMUNITY COLLEGE',
#                   'WILKES COMMUNITY COLLEGE', 'NORTH CAROLINA WILDLIFE COMMISSION', 'STATE OF NORTH CAROLINA', 'BALD MOUNTAIN TRUST THE (TRUSTEES)', 'NATURE CONSERVANCY, THE', 'THE NATURE CONSERVANCY', 'STATE OF NORTH CAROLINA C/O STATE PROPERTY OFFICE','STATE OF NORTH CAROLINA THE','THE THE STATE OF NORTH CAROLINA',
#                    'RICHARDSON, H SMITH JR ET AL (TRUSTEES),BALD MTN TRUST','RICHARDSON, H SMITH TRUSTEES,RICHARDSON TESTAMENTARY TRUST','CHARLES A CANNON, JR. MEMORIAL HOSPITAL, INC', 'CROSSNORE SCHOOL INC', 'WAL-MART REAL ESTATE BUSINESS TRUST', "LOWE'S HOME CENTER INC", 'GRANDFATHER MOUNTAIN STEWARDSHIP FOUNDATION, INC',
#                    'BANNER ELK, TOWN OF', 'TOWN OF BANNER ELK', 'LEES MC RAE COLLEGE FIXED ASSETS COORDINATOR', 'INGLES MARKETS INC', 'BOARD OF EDUCATION OF ALLEGHANY COUNTY', 'NATURE CONSERVANCY', 'VILLAGE OF SUGAR MOUNTAIN', 'BANNER ELK MEDICAL INVESTORS A TENN. LIMITED LIABILITY CO.', 'FIRST UNION NATIONAL BANK',
#                    'AF BANK','BANK OF AMERICA NA,.NATIONSBANK NA','BLUE RIDGE BANK','CENTURA BANK','COMERICA BANK & TRUST, NA-TRUSTEE CAPASEE, LINDA C-TRUSTEE','FIFTH THIRD BANK','FIRST CITIZENS BANK & TRUST COMPANY','FIRST UNION NATIONAL BANK','FIRST UNION NATIONAL BANK,.MARY BOST C GRAY 1953 TRUST','HIGH COUNTRY BANK',
#                    'HIGH POINT BANK & TRUST CO SUCCESSOR TR,THE T HENRY WILSON FAMILY TRUST','HIGH POINT BANK & TRUST CO TRUSTEE FOR T HENRY WILSON III','HIGHLANDS UNION BANK','LIFESTORE BANK','SKYLINE NATIONAL BANK','YADKIN VALLEY BANK & TRUST CO','YADKIN VALLEY BANK & TRUST COMPANY','WACHOVIA BANK NA,.JAMES M ATKINS IRREVOCABLE AGREEMENT',
#                    'YADKIN BANK 3660 GLENWOOD AVE, STE 300', 'AVERY COUNTY, NC HUMANE SOCIETY, INC', 'STATE EMPLOYEES CREDIT UNION INC,BOONE BRANCH LOCATION',"STATE EMPLOYEES' CREDIT UNION", 'MAHARISHI UNIVERSITY OF ENLIGHTENMENT', "YOUNG MEN'S CHRISTIAN ASSOCIATION OF AVERY COUNTY",'PIONEER ECLIPSE CORPORATION','WEST JEFFERSON FIRST BAPTIST',
#                    'JEFFERSON TOWN OF','BANNER ELK, TOWN OF','LANSING TOWN OF','NEWLAND, TOWN OF','TOWN OF BLOWING ROCK','TOWN OF SPARTA','WEST JEFFERSON TOWN OF','BANNER ELK, TOWN OF','JEFFERSON TOWN OF','LANSING TOWN OF','NEWLAND, TOWN OF', 'SUN FARMS INC', 'NORTH CAROLINA DEPARTMENT OF TRANSPORTATION', 'DOLLAR FARMS INC', 'STATE OF NC',
#                    'OLEANDER COMPANY THE', 'CHESTER BAR OF NORTH CAROLINA', 'AVERY DEVELOPMENT CORPORATION', 'AVERY TIMBER RESOURCES, LLC 1/2 PHILLIPS, MARTHA ETAL 1/2', 'NATURE CONSERVANCY THE', 'BLUE RIDGE CONSERVANCY', 'NORTH CAROLINA STATE OF', 'NORTH CAROLINA WILDERNESS LTD', 'BANNER ELK LOWES LLC',
#                    'LONE OAK CORPORATION', 'INN AT CRESTWOOD INC', 'LUTHERIDGE LUTHEROCK MINISTRY INC','SHOPPES OF TYNECASTLE, LLC', 'HALCORE GROUP INC.','ALLEGHANY WELLNESS CENTER, INC.', 'HOLSTON PRESBYTERY CAMP CORP','BOWER & JOHNSON CORP', 'CHARMING INNS OF BLOWING ROCK HILLWINDS', 'LANSING CHEMI-CON INC', 'ASHE SENIOR VILLAGE INC',
#                    'GOODWILL INDUSTRIES OF NORTHWEST', 'CORNERSTONE CHRISTIAN FELLOWSHIP INC.', 'WILBERN REALTY & INVESTMENT CO', 'WEST JEFFERSON HOUSING PARTNERSHIP','CALDWELL REALTY & INVESTMENT', ]
#
##drop rows with these ownname from all_keepers_2019. Drops 335 rows
#for owner_name in bad_owner_names:
#    all_keepers_2019.drop(all_keepers_2019[all_keepers_2019['ownname'] == owner_name].index, inplace=True)
#
#
#
#
## 9. Drop duplicates
#
##change saledate column to object type from datetime
#all_keepers_2019['saledate'] = all_keepers_2019['saledate'].astype(str)
#
#all_keepers_2019 = all_keepers_2019.drop_duplicates()



