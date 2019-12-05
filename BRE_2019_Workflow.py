#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:14:07 2019

@author: ep9k
"""


import geopandas as gpd


#### STARTING FROM THE TOP, READ THE 'AllResidential2019' FILE INTO DATAFRAME

filepath = '/Users/ep9k/Desktop/BRE/BRE 2019/AllResidential2019.shp'

all_residential_df = gpd.read_file(filepath)

print(all_residential_df)



