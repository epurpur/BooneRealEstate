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
all_2019_parcels = gpd.read_file('/Users/ep9k/Desktop/BRE/BRE 2019/All_Parcels_2019.gpkg')                      #228,393 parcels


#2. Drop useless columns from all_2019_parcels to make data cleaner. Create Address columns to merge with original_mailing_list 
columns_to_drop = ['id_0', 'id', 'gnisid', 'maddpref', 'maddrno',
       'maddstname', 'maddstr', 'maddstsuf', 'maddsttyp', 'mapref', 
       'munit', 'ownfrst', 'ownlast', 'owntype', 'parusedsc2', 'revdatetx',
       'saddpref', 'scity', 'structno', 'subdivisio', 'subowntype', 'subsurfown', 'sunit',
       'szip', 'layer', 'path']

all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)

#create full address columns for both property address and mailing address in all_2019_parcels and original_mailing_list
#I cant make a full property address. All I have is the 'sideadd' column in all_2019_parcels which does not have a city!
all_2019_parcels['FullMailingAddress'] = all_2019_parcels['mailadd'] + ' ' + all_2019_parcels['mcity'] + ' ' + all_2019_parcels['mstate']
all_2019_parcels['FullMailingAddress'] = all_2019_parcels['FullMailingAddress'].str.replace(' ','')   #got rid of all spaces for simplicity

all_2019_parcels['siteadd'] = all_2019_parcels['siteadd'].str.replace(' ','')

original_mailing_list['FullMailingAddress'] = original_mailing_list['Mailing #'] + ' ' + original_mailing_list['Mailing Address'] + ' ' + original_mailing_list['Mailing City'] + ' ' + original_mailing_list['Mailing State']    
original_mailing_list['FullMailingAddress'] = original_mailing_list['FullMailingAddress'].str.replace(' ','')   #got rid of all spaces for simplicity
##I am leaving off the state to attempt to match this to all_parcels_2019['siteadd'] column
original_mailing_list['FullPropertyAddress'] = original_mailing_list['Property #'] + ' ' + original_mailing_list['Property ST']
original_mailing_list['FullPropertyAddress'] = original_mailing_list['FullPropertyAddress'].str.replace(' ','')

##3. Merge other lists to all_2019_parcels to create a master list
#start by merging original_mailing_list to all_2019_parcels. From this list we want to keep '2+ Removed' and 'Subdivision' columns

#first try merging by parno to 'PIN (Parcel Indentifier Number)'
all_2019_parcels = all_2019_parcels.merge(original_mailing_list, how='left', left_on='parno', right_on='PIN (Parcel Indentifier Number)')
all_2019_parcels.loc[all_2019_parcels['PIN (Parcel Indentifier Number)'].notnull(), '2+ Removed Final'] = all_2019_parcels['2+ Removed']       #keeping 2+ removed column
all_2019_parcels.loc[all_2019_parcels['PIN (Parcel Indentifier Number)'].notnull(), 'Subdivision Final'] = all_2019_parcels['SUBDIVISION']     #keeping SUBDIVISION column
results1 = all_2019_parcels.loc[all_2019_parcels['PIN (Parcel Indentifier Number)'].notnull()]                   #1155 matches

#drop columns I merged to make results cleaner
columns_to_drop = [ 'FullMailingAddress_x','Last Name','First Name','2+ Removed','SUBDIVISION','Property #','Property ST','Property City','Property State',
 'Property Zipcode','TEMP REMOVED','PIN (Parcel Indentifier Number)','Zone','Section','Mailing #','Mailing Address','Mailing City','Mailing State','Mailing Zipcode',
 '1 Returned','Corrected','ADDED','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','FullMailingAddress_y','FullPropertyAddress']
all_2019_parcels.drop(columns_to_drop, inplace=True, axis=1)


#next try by altparno to 'PIN (Parcel Indentifier Number)'
all_2019_parcels = all_2019_parcels.merge(original_mailing_list, how='left', left_on='altparno', right_on='PIN (Parcel Indentifier Number)')
all_2019_parcels.loc[all_2019_parcels['PIN (Parcel Indentifier Number)'].notnull(), '2+ Removed Final'] = all_2019_parcels['2+ Removed']       #keeping 2+ removed column
all_2019_parcels.loc[all_2019_parcels['PIN (Parcel Indentifier Number)'].notnull(), 'Subdivision Final'] = all_2019_parcels['SUBDIVISION']     #keeping SUBDIVISION column
results2 = all_2019_parcels.loc[all_2019_parcels['PIN (Parcel Indentifier Number)'].notnull()]                   



#all_2019_parcels = all_2019_parcels.merge(original_mailing_list, how='left', left_on='FullMailingAddress', right_on='FullMailingAddress')







