
"""
This is the second script in the series of updating the 2021 tax parcel data.

Steps:
    
1. Imports new 2021 parcels, which is generated from BRE_2021_workflow_pt1.

These new parcels need to have data added to them to create a complete record for the property object in Salesforce. Most of this is done in QGIS but some is done in python.

2. Creates Property Type column for these parcels by comparing parcel value to land value. If they are equal, it is assumed this is a land parcel and home exists on it. Make property types accordingly.

"""


import pandas as pd
import numpy as np


# import 2021 parcels
new_2021_parcels = pd.read_csv('/Users/ep9k/Desktop/new_2021_parcels.csv')

# separate out just those with 'false' in the comparison column
#this means they are found in the newly downloaded data but not the old data
new_2021_parcels = new_2021_parcels.loc[new_2021_parcels['comparison'] == False]


# create value for new PBA_PROPERTYTYPE_C column

# if parval == landval column, PBA_PROPERTYTYPE_C is determined to be 'land'. Else, it is determined to be 'Home'
#create 'Property Type' column and populate with true/false values
new_2021_parcels['Property Type'] = new_2021_parcels['landval'] == new_2021_parcels['parval']

#change true/false values to 'Vacant Land' or no value.
new_2021_parcels.loc[(new_2021_parcels['Property Type'] == True), 'Property Type'] = 'Land'
new_2021_parcels.loc[(new_2021_parcels['Property Type'] == False), 'Property Type'] = 'Home'



