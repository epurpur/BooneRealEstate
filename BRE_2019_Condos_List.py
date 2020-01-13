#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:57:29 2019

@author: ep9k
"""

"""I'm going to compare Matt's Condo address list (with valid parcel numbers) to the global list in order to see how many condos are
matching and then remove them from the list."""


import geopandas as gpd
import pandas as pd

condos_df = pd.read_excel('/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList.xlsx')

final_mailing_2019 = gpd.read_file('/Users/ep9k/Desktop/Final_Mailing_List_2019.gpkg')


#Start with Final_mailing_list_2019 to compare to. This is final 'all keepers' from BRE_2019_Workflow file
global_df = gpd.read_file('/Users/ep9k/Desktop/All_res.gpkg')


####COMPARE CONDOS TO GLOBAL DATAFRAME (2019 keepers)

#first, add 'condos' at property type
condos_df['Property Type'] = 'Condo'

#compare based on parno field
global_df = global_df.merge(condos_df, how='left', left_on='parno', right_on='Parcel ID')  
global_df.loc[global_df['Parcel ID'].notnull(), 'Added Condo'] = 'Yes'
results1 = condos_df[condos_df['Parcel ID'].isin(global_df['Parcel ID'])]                     #626 matches (unique)

##compare based on altparno field. First must strip dashes from 'Parcel ID' field
condos_df['Parcel ID Stripped'] = condos_df['Parcel ID'].str.replace('-','')
global_df = global_df.merge(condos_df, how='left', left_on='altparno', right_on='Parcel ID Stripped') 
global_df.loc[global_df['Parcel ID_x'].notnull(), 'Added Condo'] = 'Yes'                                       
results2 = condos_df[condos_df['Parcel ID Stripped'].isin(global_df['Parcel ID_x'])]         #23 matches (unique)       

#take first 12 characters of condos 'Parcel ID' from Matt's parcel numbers and compare to 'parno'
condos_df['Parcel ID Shortened'] = condos_df['Parcel ID'].str[:12]
global_df = global_df.merge(condos_df, how='left', left_on='parno', right_on='Parcel ID Shortened')
global_df.loc[global_df['Parcel ID Shortened'].notnull(), 'Added Condo'] = 'Yes'                                
results3 = condos_df[condos_df['Parcel ID Shortened'].isin(global_df['Parcel ID Shortened'])]              #705 matches (unique)

##Some Watauga County parcels match to a certain point (first 15 characters of global_df parcel number')
condos_df['Parcel ID 15'] = condos_df['Parcel ID'].str[:15]
global_df['Parcel ID 15'] = global_df['parno'].str[:15]
results4 = condos_df[condos_df['Parcel ID 15'].isin(global_df['Parcel ID 15'])]                          #1660 matches (unique)

global_df = global_df.merge(condos_df, how='left', left_on='Parcel ID 15', right_on='Parcel ID 15')
#global_df.loc[global_df['Parcel ID 15'].notnull(), 'Added Condo'] = 'Yes'

##renaming some columns because we have duplicate column names
##this is the easiest way I could figure out to do it. I only renamed the 'Parcel ID' and 'Property Type' columns
global_df.columns = ['id_0','id','altparno','cntyfips','cntyname','gisacres','gnisid','improvval','landval','legdecfull','maddpref','maddrno','maddstname',
 'maddstr','maddstsuf','maddsttyp','mailadd','mapref','mcity','mstate','multistruc','munit','mzip','nparno','ownfrst','ownlast','ownname','ownname2',
 'owntype','parno','parusecd2','parusecode','parusedesc','parusedsc2','parval','parvaltype','presentval','recareano','recareatx','revdatetx','revisedate',
 'reviseyear','saddno','saddpref','saddstname','saddstr','saddstsuf','saddsttyp','saledate','saledatetx','scity','siteadd','sourceagnt','sourcedate',
 'sourcedatx','sourceref','sstate','stcntyfips','stfips','stname','struct','structno','structyear','subdivisio','subowntype','subsurfown','sunit',
 'szip','transfdate','layer','path','geometry','Parcel ID 1','Last Name_x','First Name_x','Mailing #_x','Mailing Address_x','Mailing City_x','Removed_x',
 'Property #_x','Property Address_x','Unit #_x','Subdivsion_x','Property City_x','Property State_x','Property Zipcode_x','Mailing State_x','Mailing Zipcode_x',
 'Returned_x','Bad Address_x','Section_x','Zone_x','Mad Children_x','Property Type 1','Added Condo','Parcel ID 2','Last Name_y','First Name_y',
 'Mailing #_y','Mailing Address_y','Mailing City_y','Removed_y','Property #_y','Property Address_y','Unit #_y','Subdivsion_y','Property City_y','Property State_y',
 'Property Zipcode_y','Mailing State_y','Mailing Zipcode_y','Returned_y','Bad Address_y','Section_y','Zone_y','Mad Children_y','Property Type 2','Parcel ID Stripped_x',
 'Parcel ID 3','Last Name_x','First Name_x','Mailing #_x','Mailing Address_x','Mailing City_x','Removed_x','Property #_x','Property Address_x','Unit #_x','Subdivsion_x',
 'Property City_x','Property State_x','Property Zipcode_x','Mailing State_x','Mailing Zipcode_x','Returned_x','Bad Address_x','Section_x','Zone_x','Mad Children_x',
 'Property Type 3','Parcel ID Stripped_y','Parcel ID Shortened_x','Parcel ID 15','Parcel ID 4','Last Name_y','First Name_y','Mailing #_y','Mailing Address_y',
 'Mailing City_y','Removed_y','Property #_y','Property Address_y','Unit #_y','Subdivsion_y','Property City_y','Property State_y','Property Zipcode_y',
 'Mailing State_y','Mailing Zipcode_y','Returned_y','Bad Address_y','Section_y','Zone_y','Mad Children_y','Property Type 4','Parcel ID Stripped','Parcel ID Shortened_y']

####START HERE
##add them together
#global_df['parcel ids added'] = global_df['Parcel ID 1'] + global_df['Parcel ID 2'] + global_df['Parcel ID 3'] + global_df['Parcel ID 4']
#
#
###concatenate all these results together into one dataframe
##condos_matches = pd.concat([results1, results2, results3, results4])
##
##
###remove duplicates
##condos_matches.drop_duplicates(subset = 'Parcel ID', inplace=True)






##compare based on parno field
#condos_df_parcel_ids = condos_df['Parcel ID'].tolist()
#
#results = global_df[global_df['parno'].isin(condos_df_parcel_ids)]
#results.drop(results[results['parusedesc'] == 'EXCLUSIONS (COMMONE AREAS)'])
#results.drop(results[results['parusedesc'] == 'CONDOMINIUM (COMMON AREA)'])
#results.to_file('/Users/ep9k/Desktop/parcel_matches1.gpkg', driver='GPKG')
#
#
##strip dashes from parcel IDs and then compare to altparno
#
#condos_df_parcel_ids = [i.replace('-','') for i in condos_df_parcel_ids]
#results2 = global_df[global_df['altparno'].isin(condos_df_parcel_ids)]
#results2.drop(results2[results2['parusedesc'] == 'EXCLUSIONS (COMMONE AREAS)'])
#results2.drop(results2[results2['parusedesc'] == 'CONDOMINIUM (COMMON AREA)'])
#results2.to_file('/Users/ep9k/Desktop/parcel_matches2.gpkg', driver='GPKG')
#
#
#
##take first 12 characters of condos parcel id from Matt's parcel numbers(for avery county only)
##condos_df_parcel_ids = [i[:12] for i in condos_df_parcel_ids]
#
#results3 = global_df[global_df['parno'].isin(condos_df_parcel_ids)]
#results3.drop(results3[results3['parusedesc'] == 'EXCLUSIONS (COMMONE AREAS)'])
#results3.drop(results3[results3['parusedesc'] == 'CONDOMINIUM (COMMON AREA)'])
#results3.to_file('/Users/ep9k/Desktop/parcel_matches3.gpkg', driver='GPKG')   #(236 matches)
#
#
#    
##Watauga county parcels seem to be matching up to a certain point...
#
#condos_df_parcel_ids = [i[:15] for i in condos_df_parcel_ids]
#
#results4 = global_df[global_df['parno'].str[:15].isin(condos_df_parcel_ids)]
#results4.drop(results4[results4['parusedesc'] == 'EXCLUSIONS (COMMONE AREAS)'])
#results4.drop(results4[results4['parusedesc'] == 'CONDOMINIUM (COMMON AREA)'])
#results4.to_file('/Users/ep9k/Desktop/parcel_matches4.gpkg', driver='GPKG')   #(784 matches)
#
#
##Had a few outliers in Watauga County where 'parusedesc' is 'Townhouse', but was not selected in other ways
#results5 = global_df[global_df['parusedesc'] == 'TOWNHOUSE']
#results5.to_file('/Users/ep9k/Desktop/parcel_matches5.gpkg', driver='GPKG')   #(435 matches)
#
#
##next I need to merge all of these into one dataframe, then merge that with the existing 2019 keepers dataframe

"""
1889-92-7894-001  #point parcel number
188999227894000  #altparno
1889-92-7894-000  #parno



1889-92-8592-001 #point parcel number
1889928592000  #altparno
1889-92-8592-000 #parno
"""

