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

#Start with Final_mailing_list_2019 to compare to. This is final 'all keepers' from BRE_2019_Workflow file
global_df = gpd.read_file('/Users/ep9k/Desktop/BRE/BRE 2019/keepers_2019.gpkg')

condos_df = pd.read_excel('/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList.xlsx')


####COMPARE CONDOS TO GLOBAL DATAFRAME (2019 keepers) BASED ON PARNO
condos_id_list = condos_df['Parcel ID'].tolist()
print(condos_id_list)
#print(condos_id_list)

global_df.drop(global_df[global_df['parno'].isin(condos_id_list)].index, inplace=True)  #116 matches


###testing. compare all counties residential addresses to condos id list

#all_parcels = gpd.read_file('/Users/ep9k/Desktop/All_res.gpkg')
#
##all_parcels.drop(all_parcels[all_parcels['parno'].isin(condos_id_list)].index, inplace=True)  #624 matches
#
#all_parcels.drop(all_parcels[all_parcels['parno'].isin(condos_id_list)].index, inplace=True)  #624 matches
#
#print(all_parcels['parno'])