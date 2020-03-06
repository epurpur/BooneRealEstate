

import pandas as pd

import CountyFunctions as cf


#1. Reading parcel IDs from the matt_condo_list file.  
matt_condo_list = pd.read_excel('/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList2019.xlsx', index_col=False)




#2. Scrape data from real estate search sites for each county individually

#####FOR WATAUGA COUNTY#####

#watauga_parcel_ids = matt_condo_list.loc[matt_condo_list['County'] == 'Watauga']            #2382 condos in Watauga County
#
##I need to split these up in order to avoid too many requests to Watauga county server
##I will save them separately and then put them to
#watauga_df1 = watauga_parcel_ids.iloc[0:500]
#watauga_df2 = watauga_parcel_ids.iloc[500:1000]
#watauga_df3 = watauga_parcel_ids.iloc[1000:1500]
#watauga_df4 = watauga_parcel_ids.iloc[1500:2000]
#watauga_df5 = watauga_parcel_ids.iloc[2000:]                                        
#
#watauga_parcel_sample = cf.watauga_subset_df_parcel_sample(watauga_df1)
#
#
#watauga_addresses = cf.watauga_tax_scraping(watauga_parcel_sample)
#watauga_address_dict = watauga_addresses[0]
#watauga_owners_dict = watauga_addresses[1]
#
#watauga_final = cf.map_function(watauga_address_dict, watauga_owners_dict, watauga_parcel_ids)

##remember to change name of output to reflect which df I'm using (watauga_df1, watauga_df2, etc)
#watauga_final.to_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/watauga_df1.xlsx')


########FOR AVERY COUNTY#####

#avery_parcel_ids = matt_condo_list.loc[matt_condo_list['County'] == 'Avery']            #709 condos in Avery County
##avery_parcel_ids = avery_parcel_ids.head(5)                                     #take first 5 as test
#
#avery_parcel_sample = avery_parcel_ids['Updated Parcel ID'].tolist()
#avery_parcel_sample = [str(i) for i in avery_parcel_sample]     #convert list items to string
#avery_parcel_sample = [i.replace(" ","") for i in avery_parcel_sample]     #remove spaces from strings
#
#
#avery_addresses = cf.avery_tax_scraping(avery_parcel_sample)
#avery_address_dict = avery_addresses[0]
#avery_owners_dict = avery_addresses[1]
#
#avery_final = cf.map_function(avery_address_dict, avery_owners_dict, avery_parcel_ids)
##REMEMBER I NEED TO EXPORT TO XLSX BECAUSE THIS PRESERVES ALL 16 SIGNIFICANT DIGITS OF PARCEL ID
#avery_final.to_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/avery_final.xlsx')


#####FOR CALDWELL COUNTY#####

#caldwell_parcel_ids = matt_condo_list.loc[matt_condo_list['County'] == 'Caldwell']       #~40 condos in Caldwell County
##caldwell_parcel_ids = caldwell_parcel_ids.head(5)                                     #take first 5 as test
#
#
#caldwell_parcel_sample = caldwell_parcel_ids['Updated Parcel ID'].tolist()
#
#caldwell_addresses = cf.caldwell_tax_scraping(caldwell_parcel_sample)
#
#caldwell_address_dict = caldwell_addresses[0]
#caldwell_owners_dict = caldwell_addresses[1]
#
#caldwell_final = cf.map_function(caldwell_address_dict, caldwell_owners_dict, caldwell_parcel_ids)
#caldwell_final.to_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/caldwell_final.xlsx')




#3. ##MANUALLY UPDATE MISSING RESULTS (for all 3 counties)
#No better way to do this than fix some parts of it manually




#4. READ ALL 5 WATAUGA DFS BACK INTO SCRIP. REMOVE ROWS WITHOUT RESULTS
##(These are no data rows, not 'no match for parcel ID')
watauga_df_pt1 = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/watauga_df1.xlsx')
watauga_df_pt2 = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/watauga_df2.xlsx')
watauga_df_pt3 = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/watauga_df3.xlsx')
watauga_df_pt4 = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/watauga_df4.xlsx')
watauga_df_pt5 = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/watauga_df5.xlsx')

#remove rows with null values
watauga_df_pt1 = watauga_df_pt1[watauga_df_pt1['UpdatedOwnerName'].notnull()]
watauga_df_pt2 = watauga_df_pt2[watauga_df_pt2['UpdatedOwnerName'].notnull()]
watauga_df_pt3 = watauga_df_pt3[watauga_df_pt3['UpdatedOwnerName'].notnull()]
watauga_df_pt4 = watauga_df_pt4[watauga_df_pt4['UpdatedOwnerName'].notnull()]
watauga_df_pt5 = watauga_df_pt5[watauga_df_pt5['UpdatedOwnerName'].notnull()]




#5. COMBINE ALL FIVE WATAUGA DFS INTO ONE MASTER WATAUGA DF
dataframes = [watauga_df_pt1, watauga_df_pt2, watauga_df_pt3, watauga_df_pt4, watauga_df_pt5]
watauga_condos = pd.concat(dataframes)




#6. COMBINE ALL 3 COUNTIES TOGETHER TO GET A FINAL 'ALL CONDOS' DATAFRAME. EXPORT FINAL RESULT

#read Avery and Caldwell results first
avery_condos = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/avery_final.xlsx')
caldwell_condos = pd.read_excel(r'/Users/ep9k/Desktop/BRE/BRE 2019/County_Parcel_DFs/caldwell_final.xlsx')

dataframes = [watauga_condos, avery_condos, caldwell_condos]
all_condos = pd.concat(dataframes)

#drop unneeded columns
all_condos = all_condos.drop(['Unnamed: 0', 'Parcel ID'], axis=1)



#convert column 'Updated Parcel ID' to 'object' type
all_condos['Updated Parcel ID'] = all_condos['Updated Parcel ID'].astype(str)

##export all_condos to desktop
#all_condos.to_excel('/Users/ep9k/Desktop/all_condos.xlsx')
