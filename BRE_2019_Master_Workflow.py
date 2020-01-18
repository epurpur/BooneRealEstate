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


#1. Starting from scratch from original documents. This includes...
#   -Matt's original mailing list (MattOriginalMailingList.xlsx)
#   -Matt's original condo list (MattCondoAddressList.xlsx)
#   -All parcels (/Users/ep9k/Desktop/BRE/BRE 2019/All_Parcels_2019.gpkg)

original_mailing_list = pd.read_csv('/Users/ep9k/Desktop/BRE/BRE 2019/MattOriginalMailingList.csv')          #11,827 addresses
original_condo_list = pd.read_csv('/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList.csv')               #3,132 condos
all_2019_parcels = gpd.read_file('/Users/ep9k/Desktop/BRE/BRE 2019/All_Parcels_2019.gpkg')                   #228,393 parcels


#2. Drop useless columns from all_2019_parcels to make data cleaner. Create Address columns to merge with original_mailing_list 
columns_to_drop = ['id_0', 'id', 'gnisid', 'maddpref', 'maddrno',
       'maddstname', 'maddstr', 'maddstsuf', 'maddsttyp', 'mapref', 
       'munit', 'ownfrst', 'ownlast', 'owntype', 'parusedsc2', 'revdatetx',
       'saddpref', 'scity', 'structno', 'subdivisio', 'subowntype', 'subsurfown', 'sunit',
       'szip', 'layer', 'path']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)


#3. MattOriginalMailing list is not actually his original, but it is a list I had from June 2019 with the 2+ removed, Subdivision, and Excluded Subdivision column in tact. 
#This had already been joined to the county parcels so I will merge based on the nparno
all_2019_parcels = all_2019_parcels.merge(original_mailing_list, how='left', left_on='nparno', right_on='nparno')

#drop useless columns from all_2019_parcels. All I want to keep after the merge is the 2+ removed, subdivision, and excluded subdivision columns

columns_to_drop = ['LAST NAME','FIRST NAME','MAILING ADDRESS','MAILING CITY','MAILING STATE','MAILING ZIPCODE','PARCEL VALUE','PROPERTY ADDRESS','sourceagnt_y',
 'id_2','fid','id','altparno_y','cntyfips_y','cntyname_y','gisacres_y','ownname2_y','gnisid','improvval_y','landval_y','legdecfull_y','maddpref',
 'maddrno','maddstname','maddstr','maddstsuf','mapref','multistruc_y','munit','maddsttyp','ownfrst','ownlast','owntype','parno_y','parusecd2_y',
 'parusecode_y','parusedesc_y','parusedsc2','parvaltype_y','presentval_y','recareano_y','recareatx_y','revdatetx','revisedate_y','reviseyear_y',
 'saddno_y','saddpref','saddstname_y','saddstr_y','saddstsuf_y','saddsttyp_y','saledate_y','saledatetx_y','scity','sourcedate_y','sourcedatx_y',
 'sourceref_y','sstate_y','stcntyfips_y','stfips_y','stname_y','struct_y','structno','structyear_y','subdivisio','subowntype','subsurfown','sunit',
 'szip','transfdate_y','id_0','id_1','layer','path']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)

#the columns in all_2019_parcels get renamed (ex:altparno_x) so I rename them to keep things clean
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



#4. Now I want to merge to condos list to the all_2019_parcels 

#I try to merge via several columns. First is parno/Parcel ID
all_2019_parcels = all_2019_parcels.merge(original_condo_list, how='left', left_on='parno', right_on='Parcel ID')
all_2019_parcels.loc[all_2019_parcels['Removed'].notnull(), 'CondoList Removed'] = all_2019_parcels['Removed']    #this preserved the 'Removed' column by moving it to a new column 'CondoList Removed'
all_2019_parcels.loc[all_2019_parcels['Unit #'].notnull(), 'CondoList Unit #'] = all_2019_parcels['Unit #']       #this preserved the 'Unit #' column by moving it to a new column 'CondoList Unit #'
all_2019_parcels.loc[all_2019_parcels['Subdivsion'].notnull(), 'CondoList Subdivision'] = all_2019_parcels['Subdivsion']       #this preserved the 'Subdivsion' column by moving it to a new column 'CondoList Subdivision'

results1 = all_2019_parcels.loc[all_2019_parcels['Parcel ID'].notnull()]                          #629 unique results

#now drop all unneeded columns

columns_to_drop = ['Parcel ID','Last Name','First Name','Mailing #','Mailing Address','Mailing City','Removed','Property #','Property Address',
                   'Unit #','Subdivsion','Property City','Property State','Property Zipcode','Mailing State','Mailing Zipcode','Returned',
                   'Bad Address','Section','Zone','Mad Children','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26',
                   'Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32','Unnamed: 33','Unnamed: 34','Unnamed: 35',
                   'Unnamed: 36','Unnamed: 37','Unnamed: 38']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)


#Now try to merge after stripping the dashes from Parcel ID field and then join altparno/Parcel ID Stripped
original_condo_list['Parcel ID Stripped'] = original_condo_list['Parcel ID'].str.replace('-','')
all_2019_parcels = all_2019_parcels.merge(original_condo_list, how='left', left_on='altparno', right_on='Parcel ID Stripped')
all_2019_parcels.loc[all_2019_parcels['Removed'].notnull(), 'CondoList Removed'] = all_2019_parcels['Removed']    #this preserved the 'Removed' column by moving it to a new column 'CondoList Removed'
all_2019_parcels.loc[all_2019_parcels['Unit #'].notnull(), 'CondoList Unit #'] = all_2019_parcels['Unit #']       #this preserved the 'Unit #' column by moving it to a new column 'CondoList Unit #'
all_2019_parcels.loc[all_2019_parcels['Subdivsion'].notnull(), 'CondoList Subdivision'] = all_2019_parcels['Subdivsion']       #this preserved the 'Subdivsion' column by moving it to a new column 'CondoList Subdivision'

results2 = all_2019_parcels.loc[all_2019_parcels['Parcel ID'].notnull()]                          #612 unique results             

#now drop all unneeded columns

columns_to_drop = ['Parcel ID','Last Name','First Name','Mailing #','Mailing Address','Mailing City','Removed','Property #','Property Address',
                   'Unit #','Subdivsion','Property City','Property State','Property Zipcode','Mailing State','Mailing Zipcode','Returned',
                   'Bad Address','Section','Zone','Mad Children','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26',
                   'Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32','Unnamed: 33','Unnamed: 34','Unnamed: 35',
                   'Unnamed: 36','Unnamed: 37','Unnamed: 38', 'Parcel ID Stripped']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)


#Now try to merge just the first 12 characters of condos 'Parcel ID' and compare to 'parno'
original_condo_list['Parcel ID Shortened'] = original_condo_list['Parcel ID'].str[:12]
all_2019_parcels = all_2019_parcels.merge(original_condo_list, how='left', left_on='parno', right_on='Parcel ID Shortened')
all_2019_parcels.loc[all_2019_parcels['Removed'].notnull(), 'CondoList Removed'] = all_2019_parcels['Removed']    #this preserved the 'Removed' column by moving it to a new column 'CondoList Removed'
all_2019_parcels.loc[all_2019_parcels['Unit #'].notnull(), 'CondoList Unit #'] = all_2019_parcels['Unit #']       #this preserved the 'Unit #' column by moving it to a new column 'CondoList Unit #'
all_2019_parcels.loc[all_2019_parcels['Subdivsion'].notnull(), 'CondoList Subdivision'] = all_2019_parcels['Subdivsion']       #this preserved the 'Subdivsion' column by moving it to a new column 'CondoList Subdivision'

results3 = all_2019_parcels.loc[all_2019_parcels['Parcel ID'].notnull()]                          #711 unique results             

#now drop all unneeded columns

columns_to_drop = ['Parcel ID','Last Name','First Name','Mailing #','Mailing Address','Mailing City','Removed','Property #','Property Address',
                   'Unit #','Subdivsion','Property City','Property State','Property Zipcode','Mailing State','Mailing Zipcode','Returned',
                   'Bad Address','Section','Zone','Mad Children','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26',
                   'Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32','Unnamed: 33','Unnamed: 34','Unnamed: 35',
                   'Unnamed: 36','Unnamed: 37','Unnamed: 38', 'Parcel ID Stripped', 'Parcel ID Shortened']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)



#NOT SURE IF THIS WILL WORK
#Some parcels match to a certain point (first 15 characters)
original_condo_list['Parcel ID 15'] = original_condo_list['Parcel ID'].str[:15]
all_2019_parcels = all_2019_parcels.merge(original_condo_list, how='left', left_on=all_2019_parcels['parno'].str[:15], right_on='Parcel ID 15')
all_2019_parcels.loc[all_2019_parcels['Removed'].notnull(), 'CondoList Removed'] = all_2019_parcels['Removed']    #this preserved the 'Removed' column by moving it to a new column 'CondoList Removed'
all_2019_parcels.loc[all_2019_parcels['Unit #'].notnull(), 'CondoList Unit #'] = all_2019_parcels['Unit #']       #this preserved the 'Unit #' column by moving it to a new column 'CondoList Unit #'
all_2019_parcels.loc[all_2019_parcels['Subdivsion'].notnull(), 'CondoList Subdivision'] = all_2019_parcels['Subdivsion']       #this preserved the 'Subdivsion' column by moving it to a new column 'CondoList Subdivision'

results4 = all_2019_parcels.loc[all_2019_parcels['Parcel ID'].notnull()]                          #1735 unique results             

columns_to_drop = ['Parcel ID','Last Name','First Name','Mailing #','Mailing Address','Mailing City','Removed','Property #','Property Address',
                   'Unit #','Subdivsion','Property City','Property State','Property Zipcode','Mailing State','Mailing Zipcode','Returned',
                   'Bad Address','Section','Zone','Mad Children','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26',
                   'Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32','Unnamed: 33','Unnamed: 34','Unnamed: 35',
                   'Unnamed: 36','Unnamed: 37','Unnamed: 38', 'Parcel ID Stripped', 'Parcel ID Shortened', 'Parcel ID 15']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)


####START HERE.  HAVE I MATCHED THE CONDOS UP TO ALL PARCELS AS MUCH AS POSSIBLE?


##create full address columns for both property address and mailing address in all_2019_parcels and original_mailing_list
##I cant make a full property address. All I have is the 'sideadd' column in all_2019_parcels which does not have a city!
#all_2019_parcels['FullMailingAddress_parcels'] = all_2019_parcels['mailadd'] + ' ' + all_2019_parcels['mcity'] + ' ' + all_2019_parcels['mstate']
#all_2019_parcels['FullMailingAddress_parcels'] = all_2019_parcels['FullMailingAddress_parcels'].str.replace(' ','')   #got rid of all spaces for simplicity
#
#all_2019_parcels['siteadd'] = all_2019_parcels['siteadd'].str.replace(' ','')
#
#original_mailing_list['FullMailingAddress_original'] = original_mailing_list['Mailing #'] + ' ' + original_mailing_list['Mailing Address'] + ' ' + original_mailing_list['Mailing City'] + ' ' + original_mailing_list['Mailing State']    
#original_mailing_list['FullMailingAddress_original'] = original_mailing_list['FullMailingAddress_original'].str.replace(' ','')   #got rid of all spaces for simplicity
###I am leaving off the state to attempt to match this to all_parcels_2019['siteadd'] column
#original_mailing_list['FullPropertyAddress'] = original_mailing_list['Property #'] + ' ' + original_mailing_list['Property ST']
#original_mailing_list['FullPropertyAddress'] = original_mailing_list['FullPropertyAddress'].str.replace(' ','')
#



#lastly, drop duplicate parcels
#all_2019_parcels.drop_duplicates(inplace=True)




