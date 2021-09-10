
"""
This is the fourth script in the series of updating the 2021 tax parcel data

This is a continuation of the 'old_parcels_upate' from BRE_2021_Workflow_pt1. I am taking the condos data which was scraped from the Watauga, Avery, Caldwell county tax sites
and merging it with old_parcels_update dataframe from BRE_2021_Workflow_pt1

Steps:
1. Import condos data and old_parcels_update data

2. Split off only condos from old_parcels_update

    
    
"""


import pandas as pd

#read in condos data
condos_df = pd.read_excel('/Users/ep9k/Desktop/BRE_Condo_Outputs/all_condos_df.xlsx')
#read in old_parcels_update
old_parcels_update = pd.read_excel('/Users/ep9k/Desktop/BRE_Condo_Outputs/old_parcels_update.xlsx')


#split off condos from all old parcels
old_parcels_condos = old_parcels_update.loc[old_parcels_update['PBA__PROPERTYTYPE__C'] == 'Condo']

#make small slice of all for testing
condos_test = condos_df.head(20)
old_parcels_test = old_parcels_update.head(20)


#now to compare existing_parcels to old_parcels
#Matt and Benedek have verified all the existing mailing addresses in Salesforce using some address matching API. I will take the first 10 characters olf the mailadd column of existing_parcels to see if they match with 'PBA__ADDRESS_PB__C' column of old_parcels
condos_df['mailaddslice'] = condos_df['PBA__ADDRESS_PB__C'].str[:10]
old_parcels_update['mailaddslice'] = old_parcels_update['PBA__ADDRESS_PB__C'].str[:10]

#for avery county, doesnt have 'PBA__ADDRESS_PB__C' column. Substitutes 'Updated Mailing Address into 'mailaddslice' column instead
condos_df.loc[(condos_df['COUNTY__C'] != 'Watauga'), 'mailaddslice'] = condos_df['UpdatedMailingAddress'].str[:10]

#make all text uppercase
condos_df['mailaddslice'] = condos_df['mailaddslice'].str.upper()
old_parcels_update['mailaddslice'] = old_parcels_update['mailaddslice'].str.upper()



#see if existing parcels mail address slice is in old_parcels mail address slice
condos_df['test_add_check'] = condos_df['mailaddslice'].isin(old_parcels_update['mailaddslice'])

    # RESULTS: 
    # True     2088
    # False    1074

#HERE we want to do somethinglike if ['test_add_check'] == true, then update mailing address with mailadd
#In this case, if the test_add_check is false, this means the mail address in exisiting parcels was not found in old parcels and should be updated
#however, I don't trust these results!
condos_df.loc[(condos_df['test_add_check'] == False), 'MAILING_ADDRESS__C'] = condos_df['UpdatedMailingAddress']




