

import pandas as pd

import CountyFunctions as cf


#Reading parcel IDs from the matt_condo_list file.  COME BACK TO THIS
matt_condo_list = pd.read_excel('/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList.xlsx')



#####FOR WATAUGA COUNTY#####

watauga_parcel_ids = matt_condo_list.loc[matt_condo_list['County'] == 'Watauga']            #2382 condos in Watauga County
#watauga_parcel_ids = watauga_parcel_ids.head(50)                                            #take first 5 just as a test

watauga_parcel_sample = watauga_parcel_ids['Updated Parcel ID'].tolist()

watauga_addresses = cf.watauga_tax_scraping(watauga_parcel_sample)
watauga_final = cf.watauga_map_function(watauga_addresses, watauga_parcel_ids)


########FOR AVERY COUNTY#####

avery_parcel_ids = matt_condo_list.loc[matt_condo_list['County'] == 'Avery']            #709 condos in Avery County
#avery_parcel_ids = avery_parcel_ids.head(50)                                     #take first 5 as test

avery_parcel_sample = avery_parcel_ids['Updated Parcel ID'].tolist()
avery_parcel_sample = [str(i) for i in avery_parcel_sample]     #convert list items to string
avery_parcel_sample = [i.replace(" ","") for i in avery_parcel_sample]     #remove spaces from strings


avery_addresses = cf.avery_tax_scraping(avery_parcel_sample)
avery_final = cf.avery_map_function(avery_addresses, avery_parcel_ids)



####FOR CALDWELL COUNTY##### Example

caldwell_parcel_ids = matt_condo_list.loc[matt_condo_list['County'] == 'Caldwell']

caldwell_parcel_sample = caldwell_parcel_ids['Updated Parcel ID'].tolist()

caldwell_addresses = cf.caldwell_tax_scraping(caldwell_parcel_sample)
caldwell_final = cf.caldwell_map_function(caldwell_addresses, caldwell_parcel_ids)


#Lastly, add dataframes together
condos_final = pd.concat([watauga_final, avery_final, caldwell_final], ignore_index=True)

#Lastly, fill erroneous NaN values in FullMailingAddress column
condos_final = condos_final['FullMailingAddress'].fillna('No match for Parcel ID', inplace=True)
