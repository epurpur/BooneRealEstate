

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

import CountyFunctions as cf

driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")


#####FOR WATAUGA COUNTY#####EXAMPLE

#watauga_parcel_ids = ['1878-25-3746-006', '1878-36-3971-001', '1878-36-3971-022', '1889-31-8223-000', '1889-40-8346-000']
#
###Reading parcel IDs from the matt_condo_list file.  COME BACK TO THIS
##matt_condo_list = pd.read_csv('/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList.csv')
##
##watauga_parcel_ids = matt_condo_list.loc[matt_condo_list['County'] == 'Watauga']
##watauga_parcel_ids = watauga_parcel_ids['Parcel ID'].tolist()
##watauga_parcel_ids = watauga_parcel_ids[:5]    #taking just first 10 as test
#
#try:
#    cf.watauga_tax_scraping(watauga_parcel_ids)
#    
#except Exception:
#    
#    print(Exception)
#    time.sleep(3)
#    cf.watauga_tax_scraping(watauga_parcel_ids)
    



######FOR AVERY COUNTY#####Example
#cant use the data yet, Avery county condo parcels are messed up. Manually got data for a good parcel number

#parcel_numbers = ['18570005766100001', '18570015196400003', '18570006101700002', '18571046350100004', '18571047202900002', '18571047202900002',
#                  '18470095834600003']	
#avery_parcel_numbers = ['185700065003', '18570005766100001', ' csfdj;', '18571046350100004', '18571047304900000', '18571046350100001']
#
#cf.avery_tax_scraping(avery_parcel_numbers)






####FOR CALDWELL COUNTY##### Example

#parcel_numbers = ['2817.03 13 9685', '2817.03 13 9683', '2817.03 13 9507', '2817.03 13 8622']
parcel_numbers = ['2817.03 33 0099', '2817.03 13 8559', 'cdgds']

cf.caldwell_tax_scraping(parcel_numbers)

