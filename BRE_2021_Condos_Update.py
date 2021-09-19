


import pandas as pd
import sys
sys.path.append('/Users/ep9k/Desktop/BRE/BRE 2019/BRE_Condos_List/scripts')
import CountyFunctions as cf
import re


# # 1. Read in 2021 parcels data
# parcels_df = pd.read_csv('/Users/ep9k/Desktop/old_parcels.csv')

# #  2. Select condos from larger dataset
# condos_df = parcels_df.loc[parcels_df['PBA__PROPERTYTYPE__C'] == 'Condo']


# # 3. Scrape data from real estate search sitesfor each county individually


# ######## WATAUGA COUNTY #########

# # A. select Watauga County condos
# watauga_parcel_ids = condos_df.loc[condos_df['COUNTY__C'] == 'Watauga']           #2401 condos in Watauga County

# # B. I need to split these up in order to avoid too many requests to Watauga county server
# watauga_df1 = watauga_parcel_ids.iloc[0:500]
# watauga_df2 = watauga_parcel_ids.iloc[500:1000]
# watauga_df3 = watauga_parcel_ids.iloc[1000:1500]
# watauga_df4 = watauga_parcel_ids.iloc[1500:2000]
# watauga_df5 = watauga_parcel_ids.iloc[2000:] 

# # watauga_parcel_sample = cf.watauga_subset_df_parcel_sample(watauga_df1)


# # C. Input list of parcel IDs into watauga_tax_scraping() which actually does the scraping
# watauga_addresses = cf.watauga_tax_scraping(watauga_df5['PIN__C'])   #INPUT HERE IS WHAT WILL BE SCRAPED

# # D. Result is a dictionary of {Parcel ID: Address} (ex: {1889-31-6308-000 : 565 ECHOTA PKWY 20B BOONE NC 28607})
# watauga_address_dict = watauga_addresses[0]

# # E. Result is a dictionary of {Parcel ID: Owner Name} (ex: {1889-31-6308-000 : HINES, BARBARA H})
# watauga_owners_dict = watauga_addresses[1]

# # F. Takes watauga_address_dict and watauga_owners dict and makes new columns in watauga_parcel_ids dataframe with the update address and updated owner name
# watauga_final = cf.map_function(watauga_address_dict, watauga_owners_dict, watauga_parcel_ids)

# # G. Export final result
# # remember to change name of output to reflect which df I'm using (watauga_df1, watauga_df2, etc)
# watauga_final.to_excel(r'/Users/ep9k/Desktop/BRE_Condo_Outputs/watauga_df5.xlsx')




######## AVERY COUNTY #########

# A. Read in old condos dataset, this is because we keep losing avery county condos ids to e+ notation (why???)
# condos_2019 = pd.read_excel('/Users/ep9k/Desktop/BRE/BRE 2021/MattCondoAddressList2019.xlsx')

# # B. select Avery County condos
# avery_parcel_ids = condos_2019.loc[condos_2019['County'] == 'Avery']               #710 condos in Avery County

# # # C. Formats pin numbers into list
# avery_parcel_sample = avery_parcel_ids['Updated Parcel ID'].tolist()
# avery_parcel_sample = [str(i) for i in avery_parcel_sample]  #convert list items to string
# avery_parcel_sample = [i.replace(" ","") for i in avery_parcel_sample]
 


# # D. Input list of parcel IDs into watauga_tax_scraping() which actually does the scraping
# avery_addresses = cf.avery_tax_scraping(avery_parcel_sample)

# # E. Result is a dictionary of {Parcel ID: Address} (ex: {18470095961400003 : 10150 S LAKE VISTA CIR DAVIE, FL 33328})
# avery_address_dict = avery_addresses[0]

# # F. Result is a dictionary of {Parcel ID: Owner Name} (ex: {18470095961400003 : DAVIS, STEVEN })
# avery_owners_dict = avery_addresses[1]

# # G. Takes avery_address_dict and avery_owners dict and makes new columns in avery_parcel_ids dataframe with the update address and updated owner name
# avery_final = cf.map_function(avery_address_dict, avery_owners_dict, avery_parcel_ids)

# # H. Exports final result to excel file (remember, needs to be excel in order to maintain avery county parcel ids)
# avery_final.to_excel(r'/Users/ep9k/Desktop/BRE_Condo_Outputs/avery_df.xlsx')



####### CALDWELL COUNTY #########
##CALDWELL CONDO TAX PARCELS NO LONGER WORK

# A. select Caldwell County condos
# caldwell_parcel_ids = condos_df.loc[condos_df['COUNTY__C'] == 'Caldwell']            # 19 condos in caldwell county

# caldwell_parcel_sample = caldwell_parcel_ids['PIN__C'].tolist()

# test = caldwell_parcel_sample[:4]
# caldwell_addresses = cf.caldwell_tax_scraping(caldwell_parcel_sample)
# caldwell_address_dict = caldwell_addresses[0]
# caldwell_owners_dict = caldwell_addresses[1]
# caldwell_final = cf.map_function(caldwell_address_dict, caldwell_owners_dict, caldwell_parcel_ids)









#4. MANUALLY UPDATE MISSING RESULTS (for all 3 counties)
#No better way to do this than fix some parts of it manually










#5. READ ALL 5 WATAUGA DFS BACK INTO SCRIP. REMOVE ROWS WITHOUT RESULTS
#(These are no data rows, not 'no match for parcel ID')
watauga_df_pt1 = pd.read_excel(r'/Users/ep9k/Desktop/BRE_Condo_Outputs/watauga_df1.xlsx')
watauga_df_pt2 = pd.read_excel(r'/Users/ep9k/Desktop/BRE_Condo_Outputs/watauga_df2.xlsx')
watauga_df_pt3 = pd.read_excel(r'/Users/ep9k/Desktop/BRE_Condo_Outputs/watauga_df3.xlsx')
watauga_df_pt4 = pd.read_excel(r'/Users/ep9k/Desktop/BRE_Condo_Outputs/watauga_df4.xlsx')
watauga_df_pt5 = pd.read_excel(r'/Users/ep9k/Desktop/BRE_Condo_Outputs/watauga_df5.xlsx')

#remove rows with null values
watauga_df_pt1 = watauga_df_pt1[watauga_df_pt1['UpdatedOwnerName'].notnull()]
watauga_df_pt2 = watauga_df_pt2[watauga_df_pt2['UpdatedOwnerName'].notnull()]
watauga_df_pt3 = watauga_df_pt3[watauga_df_pt3['UpdatedOwnerName'].notnull()]
watauga_df_pt4 = watauga_df_pt4[watauga_df_pt4['UpdatedOwnerName'].notnull()]
watauga_df_pt5 = watauga_df_pt5[watauga_df_pt5['UpdatedOwnerName'].notnull()]










#6. COMBINE ALL FIVE WATAUGA DFS INTO ONE MASTER WATAUGA DF
dataframes = [watauga_df_pt1, watauga_df_pt2, watauga_df_pt3, watauga_df_pt4, watauga_df_pt5]
watauga_condos = pd.concat(dataframes)













#7. COMBINE ALL 3 COUNTIES TOGETHER TO GET A FINAL 'ALL CONDOS' DATAFRAME. EXPORT FINAL RESULT

# #read Avery and Caldwell results first
avery_condos = pd.read_excel(r'/Users/ep9k/Desktop/BRE_Condo_Outputs/avery_df.xlsx')
# caldwell_condos = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/caldwell_final.xlsx')

dataframes = [watauga_condos, avery_condos]
all_condos = pd.concat(dataframes)

#drop unneeded columns
# all_condos = all_condos.drop(['Unnamed: 0', 'Parcel ID'], axis=1)


#convert column 'Updated Parcel ID' to 'object' type
# all_condos['Updated Parcel ID'] = all_condos['Updated Parcel ID'].astype(str)

#export all_condos to desktop
# all_condos.to_excel('/Users/ep9k/Desktop/all_condos.xlsx')











##### REGEX MATCHING
test = watauga_condos.head(100)
test_condo_addresses = test['UpdatedMailingAddress'].tolist()

end_result = []

pattern = re.compile(r'([A-Z0-9 .-]+) (\w+) (\w{2}) (\d{5})')
# pattern = re.compile(r'(\d{5})')

for address in test_condo_addresses:
    matches = pattern.finditer(address)
    for match in matches:
        end_result.append(match)
        print(f'{match.group(1)}, {match.group(2)}, {match.group(3)}, {match.group(4)}')
    







