#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:33:02 2019

@author: ep9k
"""
import pandas as pd
import geopandas as gpd

filepath = '/Users/ep9k/Desktop/BRE/BRE 2019/AllKeeperAddresses_2019_geopandas.shp'

keeper_2019_df = gpd.read_file(filepath)


#### DROP UNNEEDED COLUMNS FROM DATAFRAME ####


columns_to_drop = ['id_1', 'fid', 'id_0', 'id', 'GNISID', 'MAPREF', 'MUNIT', 'PARUSEDSC2', 'SCITY', 'SOURCEREF', 'STRUCTNO', 'SUBOWNTYPE',
                   'SUBSURFOWN', 'SUNIT', 'SZIP', 'FCODE', 'PIN', 'LEGAL_DESC', 'BOOK_PAGE', 'DEED_DATE', 'ACREAGE', 'ACCT_NO', 'ADDRESS',
                   'ADDR_1', 'ADDR_2', 'CITY', 'STATE', 'ZIP', 'HOUSE_NUMB', 'STREET_NM', 'STREET_SUF', 'STREET_TYP', 'BUILD_VALU', 'XFOB_VALUE',
                   'LAND_VALU', 'TOTAL_VALU', 'APPR_BY', 'APPR_DATE', 'AYB', 'FIRE_CODE', 'CITY_CODE', 'TOWNSHIP_C', 'MNBH_NO', 'FARMLAND_C',
                   'DEEDDATE', 'SALEPRICE', 'VACANTORIM', 'CODE', 'SALEYEAR', 'USECODE', 'SHAPE_Leng', 'SHAPE_Area','2018Decama', '2018Deca_1',
                   '2018Deca_4', '2018Deca_5', '2018Deca_6', '2018Deca_7', '2018Deca_8', '2018Deca_9', '2018Deca10', '2018Deca11', '2018Deca12',
                   '2018Deca13', '2018Deca14', '2018Deca15', '2018Deca16', '2018Deca17', '2018Deca18', '2018Deca19', '2018Deca20', '2018Deca21',
                   '2018Deca22', '2018Deca23', '2018Deca24', '2018Deca25', '2018Deca26', '2019AllK_1', '2019AllK_2', '2019AllK_3', '2019AllK_4',
                   '2019AllK_5', '2019AllK_6', '2019AllK_7', '2019AllK_8', '2019AllK_9', '2019AllK10', '2019AllK11', '2019AllK12', '2019AllK13', '2019AllK14',
                   '2019AllK15', '2019AllK16', '2019AllK17', '2019AllK18', '2019AllK19', '2019AllK20', '2019AllK21', '2019AllK22', '2019AllK23', '2019AllK24',
                   '2019AllK25', '2019AllK26', '2019AllK27', '2019AllK28', '2019AllK29', '2019AllK30', '2019AllK31', '2019AllK32', '2019AllK33', '2019AllK34',
                   '2019AllK35', '2019AllK36', '2019AllK39', '2019AllK40', '2019AllK46', '2019AllK47', '2019AllK48', '2019AllK49',
                   '2019AllK50', '2019AllK51', '2019AllK52', '2019AllK53', '2019AllK54', '2019AllK55', '2019AllK56', '2019AllK57', '2019AllK58',
                   '2018Deca_2', '2019AllK37', '2019AllK41', '2018Deca_3', '2019AllK38', '2019AllK42']

keeper_2019_df.drop(columns_to_drop, inplace=True, axis=1)

#rename columns so I can tell what is what
keeper_2019_df.rename(columns = {'2019AllK43':'Owner_Moved', 
                       '2019AllK44':'Sold_In_Last_Year', 
                       '2019AllK45':'No_Change',
                       '2018Keeper':'2+_Removed',
                       '2018Keep_1':'Excluded_Subdivisions'}, inplace=True)


#### EXTRACT VACANT LAND FROM LIST or MAKE 'VACANT LAND' COLUMN   ####

#First, create 'VacantLand' column and populate it with vacant land parcels (1262 parcels)
keeper_2019_df.loc[(keeper_2019_df['PARUSEDESC'] == 'RESIDENTIAL VACANT'), 'VacantLand'] = 'Yes'     #For Watauga County only
keeper_2019_df.loc[(keeper_2019_df['LANDVAL'] == keeper_2019_df['PARVAL']), 'VacantLand'] = 'Yes'                # If Parcel Value = Land Value, we assume there is no structure and its vacant land


#Now create 'VacantLandValue' column for parcels > $100k and >$200k
keeper_2019_df.loc[(keeper_2019_df['VacantLand'] == 'Yes') & (keeper_2019_df['PARVAL'] > 100000), 'VacantLandValue'] = '> 100k'  #936 rows
keeper_2019_df.loc[(keeper_2019_df['VacantLand'] == 'Yes') & (keeper_2019_df['PARVAL'] > 200000), 'VacantLandValue'] = '> 200k'  #180 rows


#now drop 'Yes' rows from the VacantLand column  #DOES THIS NEED TO HAPPEN?
#df.drop(df.loc[df['VacantLand'] == 'Yes'].index, inplace=True)



#### EXTRACT CONDOS FROM 2019 KEEPERS ####

condos_dataset_path = '/Users/ep9k/Desktop/BRE/MattCondoAddressList.xlsx'

condos_df = pd.read_excel(condos_dataset_path)
condo_parcel_ids = condos_df['Parcel ID (PIN)'].tolist()

print(keeper_2019_df['ALTPARNO'])
#match_count = 0
#
#for i in condo_parcel_ids:
#    if keeper_2019_df['NPARNO'].isin(i):
#        match_count += 1
#print(match_count)

 

















