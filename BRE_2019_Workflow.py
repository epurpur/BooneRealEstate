#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:14:07 2019

@author: ep9k
"""


import geopandas as gpd
import pandas as pd

##### STARTING FROM THE TOP, READ THE 'AllResidential2019' FILE INTO DATAFRAME
##
##filepath = '/Users/ep9k/Desktop/BRE/BRE 2019/AllResidential2019.shp'
##
##all_residential_df = gpd.read_file(filepath)
##
##print(all_residential_df)
#
#
#try:
#    connection = psycopg2.connect(user = "postgres",                
#    #psycopg2.connect() creates connection to PostgreSQL database instance
#                              password = "battlebot",
#                              host = "127.0.0.1",
#                              port = "5432",
#                              database = "BRE_2019_Test")
#
#    cursor = connection.cursor()                                #creates a cursor object which allows us to execute PostgreSQL commands through python source
#
#    cursor.execute('SELECT * FROM "allkeepers_2019"')           #Executes a database operation or query. Execute method takes SQL query as a parameter. Returns list of result
#    
#    record = cursor.fetchall()
#
#    print(record)
#
#
#except (Exception, psycopg2.Error) as error:
#    print("Error while connecting to PostgreSQL: ", error)



#upgrade this to read from PostgreSQL table instead of from geopackage eventually

# AS OF 12/6/19 I MANUALLY SAVED THE 'allkeepers_2019' layer as a geopackage at this filepath

filepath = '/Users/ep9k/Desktop/BRE/BRE 2019/allkeepers_2019.gpkg'

all_keepers_df = gpd.read_file(filepath, layer='allkeepers_2019')
all_keepers_df.drop_duplicates(subset='nparno', keep='first', inplace=True)



#### READ HELPER GPKG FILE TO JOIN MATT'S COLUMNS

filepath = '/Users/ep9k/Desktop/BRE/BRE 2019/keepers_2019.gpkg'
helper_df = gpd.read_file(filepath, layer='keepers_2019')

####MERGE these columns from helper_df to all_keepers_df: '2+ Removed', 'Excluded_Subdivisions', 'Owner_moved', 'sold_in_last_year', 'No_Change', 'VacantLand', 'VacantLandValue'

all_keepers_df = all_keepers_df.merge(helper_df, left_on='nparno', right_on='NPARNO')

####DROP UNNEEDED COLUMNS FROM DATAFRAME

all_keepers_df['geometry'] = all_keepers_df['geometry_x']   #rename this column since I have duplicate geometry columns

columns_to_drop = ['id_0', 'id', 'gnisid', 'maddpref', 'maddrno',
       'maddstname', 'maddstr', 'maddstsuf', 'maddsttyp', 'mapref', 
       'munit', 'ownfrst', 'ownlast', 'owntype', 'parusedsc2', 'revdatetx',
       'saddpref', 'scity', 'structno', 'subowntype', 'subsurfown', 'sunit',
       'szip', 'ALTPARNO', 'CNTYFIPS', 'CNTYNAME', 'GISACRES', 
       'IMPROVVAL', 'LANDVAL', 'LEGDECFULL', 'MAILADD', 'MCITY', 'MSTATE', 
       'MULTISTRUC', 'MZIP', 'NPARNO', 'OWNNAME', 'OWNNAME2', 'OWNTYPE', 'PARNO', 
       'PARUSECD2', 'PARUSECODE', 'PARUSEDESC', 'PARVAL', 'PARVALTYPE', 
       'SADDSTNAME', 'SADDSTR', 'SADDSTSUF', 'SADDSTTYP', 'SALEDATE', 'SALEDATETX', 
       'SITEADD', 'SOURCEAGNT', 'SOURCEDATE', 'SOURCEDATX', 'SSTATE', 'STCNTYFIPS', 
       'STFIPS', 'STNAME', 'STRUCT', 'STRUCTYEAR', 'SUBDIVISIO', 'TRANSFDATE', 
       'OWNER_NAME', '2019AllKee', 'layer', 'path', 'geometry_x', 'geometry_y']

all_keepers_df.drop(columns_to_drop, inplace=True, axis=1)



#### EXTRACT MATCHING CONDOS FROM 2019 KEEPERS####
#APPARENTLY THERE AREN'T ANY MATCHING CONDOS??
condos_dataset_path = '/Users/ep9k/Desktop/BRE/MattCondoAddressList.xlsx'

condos_df = pd.read_excel(condos_dataset_path)

#check by Parcel ID (Parcel ID (PIN)/ALTPARNO)
condo_parcel_id_list = condos_df['Parcel ID (PIN)'].tolist()
all_keepers_df.drop(all_keepers_df[all_keepers_df['altparno'].isin(condo_parcel_id_list)].index, inplace=True)   #0 matches?

#check by Parcel ID (Parcel ID (PIN)/PARNO)
all_keepers_df.drop(all_keepers_df[all_keepers_df['parno'].isin(condo_parcel_id_list)].index, inplace=True)  #0 matches?

#check by address. (FullMailAdd_condo/FullAddress)
condo_mailing_address_list = condos_df['FullMailAdd_condo'].tolist()
all_keepers_df.drop(all_keepers_df[all_keepers_df['FullAddress'].isin(condo_mailing_address_list)].index, inplace=True)  #0 matches? 



####REMOVE NON-RESIDENTIAL PARCELS BY NPARNO
####THESE ARE PARCELS I MANUALLY SELECTED IN QGIS WHICH ARE NOT RESIDENTIAL. READ THE .GPKG IN AND DROP THEM BASED ON THEIR NPARNO
not_residential_parcels_filepath = '/Users/ep9k/Desktop/BRE/not_residential_removed_parcels.gpkg'
not_residential_parcels_df = gpd.read_file(not_residential_parcels_filepath, layer='not_residential_removed_parcels')

not_residential_ids_list = not_residential_parcels_df['nparno'].tolist()

#compare nparno to all_keepers_df['nparno']
all_keepers_df.drop(all_keepers_df[all_keepers_df['nparno'].isin(not_residential_ids_list)].index, inplace=True)



####CONVERT DATAFRAME BACK TO GEODATAFRAME

all_keepers_df = gpd.GeoDataFrame(all_keepers_df,
                                  crs={'init': 'epsg: 2264'},
                                  geometry = all_keepers_df['geometry'])


all_keepers_df.to_file('/Users/ep9k/Desktop/test_out2.gpkg', driver='GPKG')






