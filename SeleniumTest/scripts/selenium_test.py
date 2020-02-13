

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import pandas as pd

import CountyFunctions as cf

driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")


######FOR WATAUGA COUNTY#####EXAMPLE
##Reading parcel IDs from the matt_condo_list file
#matt_condo_list = pd.read_csv('/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList.csv')
#
#watauga_parcel_ids = matt_condo_list.loc[matt_condo_list['County'] == 'Watauga']
#watauga_parcel_ids = watauga_parcel_ids['Parcel ID'].tolist()
#watauga_parcel_ids = watauga_parcel_ids[:15]    #taking just first 10 as test
#
#try:
#    cf.watauga_tax_scraping(watauga_parcel_ids)
#    
#except Exception:
#    
#    print(Exception)
#    time.sleep(3)
#    cf.watauga_tax_scraping(parcel_ids)
    



#####FOR AVERY COUNTY#####Example
#cant use the data yet, Avery county condo parcels are messed up. Manually got data for a good parcel number

#Land on Avery county tax website
driver.get('http://webtax.averycountync.gov/')

parcel_numbers = ['18570005766100001', '18570015196400003']	
#parcel_numbers = ['18570005766100001']

for parcel_number in parcel_numbers:
    
    parcel_number_split = []
    
    p1 = parcel_number[0:4]
    parcel_number_split.append(p1)
    p2 = parcel_number[4:6]
    parcel_number_split.append(p2)
    p3 = parcel_number[6:8]
    parcel_number_split.append(p3)
    p4 = parcel_number[8:12]
    parcel_number_split.append(p4)
    p5 = parcel_number[12:19]
    parcel_number_split.append(p5)
    
    #Clear input fields
    map_ = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtMAP')
    map_.clear()
    sub = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtSUB')
    sub.clear()
    blk = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtBLK')
    blk.clear()
    lot = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtLOT')
    lot.clear()
    ext = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtEXT')
    ext.clear()    
    
    #Enter Parcel # into input boxes (Map, Sub, Blk, Lot, Ext)
    map_.send_keys(parcel_number_split[0])
    sub.send_keys(parcel_number_split[1])
    blk.send_keys(parcel_number_split[2])
    lot.send_keys(parcel_number_split[3])
    ext.send_keys(parcel_number_split[4])
    
    #Click buttons to get results
    driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_buttonSearch').click()
    
    driver.find_element_by_class_name('HyperLinkField').click()
    
    driver.find_element_by_id('__tab_ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners').click()
    
    #Now scrape HTML results using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    body_tags = soup.find_all('td', valign='bottom')
    
    #output is printed in long table. Using indexing to find the address info
    ####START HERE. I will probably have to use regular expressions to find this address in the output text
    body_tags = body_tags[191:194]    
    body_tags = [tag.text for tag in body_tags]    #get just the text of each tag
    
    mailing_address = ' '.join(body_tags)
    
    print(mailing_address)
    
    time.sleep(5)






#####FOR CALDWELL COUNTY##### WORK IN PROGRESS
#Land on Caldwell County GIS Page
#driver.get('http://gis.caldwellcountync.org/maps/default.htm')

#Hover over 'enter serach string' and select 'Parcel ID'
#elements_to_hover_over = driver.find_elements_by_class_name('dijitTabInner dijitTabContent dijitTab dijitTabChecked dijitChecked dijitTabFocused dijitTabCheckedFocused dijitCheckedFocused dijitFocused')
#hover = ActionChains(driver).move_to_element(element_to_hover_over)
#hover.perform()




