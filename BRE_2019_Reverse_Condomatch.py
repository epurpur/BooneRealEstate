#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:13:45 2020

@author: ep9k
"""

"""
What I want to do here is a reverse condo matching for Matt. Those condos that I
have gotten to match up from the Master list, I want to match those back to Matt's condo
list so he knows which matched and which didn't. Then, Matt is going to manually adjust the 
'Parcel Type' column in the master list to 'Condo'
"""

import pandas as pd
import geopandas as gpd


#read 2019 master list and matt's condo list
all_2019_parcels = gpd.read_file('/Users/ep9k/Desktop/BRE/BRE 2019/All_Parcels_2019.gpkg')
original_condo_list = pd.read_csv('/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList.csv')


#match those condos back to Matt's condo list
#first on parno
original_condo_list = original_condo_list.merge(all_2019_parcels, how='left', left_on='Parcel ID', right_on='parno')

#all_2019_parcels.loc[all_2019_parcels['Removed'].notnull(), 'CondoList Removed'] = all_2019_parcels['Removed']    #this preserved the 'Removed' column by moving it to a new column 'CondoList Removed'
original_condo_list.loc[original_condo_list['parno'].notnull(), 'Condo Match'] = "Yes"

columns_to_drop = ['parno','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30',
 'Unnamed: 31','Unnamed: 32','Unnamed: 33','Unnamed: 34','Unnamed: 35','Unnamed: 36','Unnamed: 37','Unnamed: 38','id_0','id','altparno','cntyfips','cntyname',
 'gisacres','gnisid','improvval','landval','legdecfull','maddpref','maddrno','maddstname','maddstr','maddstsuf','maddsttyp','mailadd','mapref','mcity','mstate',
 'multistruc','munit','mzip','nparno','ownfrst','ownlast','ownname','ownname2','owntype','parusecd2','parusecode','parusedesc','parusedsc2','parval','parvaltype',
 'presentval','recareano','recareatx','revdatetx','revisedate','reviseyear','saddno','saddpref','saddstname','saddstr','saddstsuf','saddsttyp','saledate',
 'saledatetx','scity','siteadd','sourceagnt','sourcedate','sourcedatx','sourceref','sstate','stcntyfips','stfips','stname','struct','structno','structyear','subdivisio','subowntype',
 'subsurfown','sunit','szip','transfdate','layer','path','geometry']
        
original_condo_list.drop(columns_to_drop, inplace=True, axis=1)


#match based on columns without dashes
original_condo_list['Parcel ID Stripped'] = original_condo_list['Parcel ID'].str.replace('-','')
original_condo_list = original_condo_list.merge(all_2019_parcels, how='left', left_on='Parcel ID Stripped', right_on='altparno')
original_condo_list.loc[original_condo_list['parno'].notnull(), 'Condo Match'] = "Yes"


columns_to_drop = ['parno','id_0','id','altparno','cntyfips','cntyname',
 'gisacres','gnisid','improvval','landval','legdecfull','maddpref','maddrno','maddstname','maddstr','maddstsuf','maddsttyp','mailadd','mapref','mcity','mstate',
 'multistruc','munit','mzip','nparno','ownfrst','ownlast','ownname','ownname2','owntype','parusecd2','parusecode','parusedesc','parusedsc2','parval','parvaltype',
 'presentval','recareano','recareatx','revdatetx','revisedate','reviseyear','saddno','saddpref','saddstname','saddstr','saddstsuf','saddsttyp','saledate',
 'saledatetx','scity','siteadd','sourceagnt','sourcedate','sourcedatx','sourceref','sstate','stcntyfips','stfips','stname','struct','structno','structyear','subdivisio','subowntype',
 'subsurfown','sunit','szip','transfdate','layer','path','geometry']

original_condo_list.drop(columns_to_drop, inplace=True, axis=1)


#Now try to merge just the first 12 characters of condos 'Parcel ID' and compare to 'parno'
original_condo_list['Parcel ID Shortened'] = original_condo_list['Parcel ID'].str[:12]
#all_2019_parcels = all_2019_parcels.merge(original_condo_list, how='left', left_on='parno', right_on='Parcel ID Shortened')
original_condo_list = original_condo_list.merge(all_2019_parcels, how='left', left_on='Parcel ID Shortened', right_on='parno')
original_condo_list.loc[original_condo_list['parno'].notnull(), 'Condo Match'] = "Yes"

columns_to_drop = ['parno','id_0','id','altparno','cntyfips','cntyname',
 'gisacres','gnisid','improvval','landval','legdecfull','maddpref','maddrno','maddstname','maddstr','maddstsuf','maddsttyp','mailadd','mapref','mcity','mstate',
 'multistruc','munit','mzip','nparno','ownfrst','ownlast','ownname','ownname2','owntype','parusecd2','parusecode','parusedesc','parusedsc2','parval','parvaltype',
 'presentval','recareano','recareatx','revdatetx','revisedate','reviseyear','saddno','saddpref','saddstname','saddstr','saddstsuf','saddsttyp','saledate',
 'saledatetx','scity','siteadd','sourceagnt','sourcedate','sourcedatx','sourceref','sstate','stcntyfips','stfips','stname','struct','structno','structyear','subdivisio','subowntype',
 'subsurfown','sunit','szip','transfdate','layer','path','geometry']

original_condo_list.drop(columns_to_drop, inplace=True, axis=1)


#Some parcels match to a certain point (first 15 characters)
original_condo_list['Parcel ID 15'] = original_condo_list['Parcel ID'].str[:15]
original_condo_list = original_condo_list.merge(all_2019_parcels, how='left', left_on='Parcel ID 15', right_on=all_2019_parcels['parno'].str[:15])
original_condo_list.loc[original_condo_list['parno'].notnull(), 'Condo Match'] = "Yes"

columns_to_drop = ['parno','id_0','id','altparno','cntyfips','cntyname',
 'gisacres','gnisid','improvval','landval','legdecfull','maddpref','maddrno','maddstname','maddstr','maddstsuf','maddsttyp','mailadd','mapref','mcity','mstate',
 'multistruc','munit','mzip','nparno','ownfrst','ownlast','ownname','ownname2','owntype','parusecd2','parusecode','parusedesc','parusedsc2','parval','parvaltype',
 'presentval','recareano','recareatx','revdatetx','revisedate','reviseyear','saddno','saddpref','saddstname','saddstr','saddstsuf','saddsttyp','saledate',
 'saledatetx','scity','siteadd','sourceagnt','sourcedate','sourcedatx','sourceref','sstate','stcntyfips','stfips','stname','struct','structno','structyear','subdivisio','subowntype',
 'subsurfown','sunit','szip','transfdate','layer','path','geometry', 'Parcel ID Stripped','Parcel ID Shortened','Parcel ID 15']

original_condo_list.drop(columns_to_drop, inplace=True, axis=1)


#export condos list 
original_condo_list.to_csv(r'/Users/ep9k/Desktop/Matched_Condo_list.csv')

