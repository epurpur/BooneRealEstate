#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:14:07 2019

@author: ep9k
"""


import geopandas as gpd


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


####DROP UNNEEDED COLUMNS FROM DATAFRAME

columns_to_drop = ['id_0', 'id', 'gnisid', 'maddpref', 'maddrno',
       'maddstname', 'maddstr', 'maddstsuf', 'maddsttyp', 'mapref', 
       'munit', 'ownfrst', 'ownlast', 'owntype', 'parusedsc2', 'revdatetx',
       'saddpref', 'scity', 'structno', 'subowntype', 'subsurfown', 'sunit',
       'szip']

all_keepers_df.drop(columns_to_drop, inplace=True, axis=1)


#### READ HELPER GPKG FILE TO JOIN MATT'S COLUMNS

filepath = '/Users/ep9k/Desktop/BRE/BRE 2019/keepers_2019.gpkg'
helper_df = gpd.read_file(filepath, layer='keepers_2019')


#### START HERE. JOIN these columns to all_keepers_df: '2+ Removed', 'Excluded_Subdivisions', 'Owner_moved', 'sold_in_last_year', 'No_Change', 'VacantLand', 'VacantLandValue'

print(helper_df.columns)



