#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:33:02 2019

@author: ep9k
"""

import geopandas as gpd

filepath = '/Users/ep9k/Desktop/BRE/BRE 2019/AllKeeperAddresses_2019_geopandas.shp'

df = gpd.read_file(filepath)


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
                   '2019AllK50', '2019AllK51', '2019AllK52', '2019AllK53', '2019AllK54', '2019AllK55', '2019AllK56', '2019AllK57', '2019AllK58']

df.drop(columns_to_drop, inplace=True, axis=1)

#### EXTRACT VACANT LAND FROM LIST   ####

#first qualifier is that if PARUSEDESC = 'RESIDENTIAL VACANT', drop it     (578 parcels)
df.drop(df.loc[df['PARUSEDESC'] == 'RESIDENTIAL VACANT'].index, inplace=True)

#second qualifier is if 'PARVAL' = 'LANDVAL'    (684 parcels)
#not sure if I should drop this or not
df.drop(df.loc[df['LANDVAL'] == df['PARVAL']].index, inplace=True)







