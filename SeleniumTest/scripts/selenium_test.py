

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

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

#parcel_numbers = ['18570005766100001', '18570015196400003', '18570006101700002', '18571046350100004', '18571047202900002', '18571047202900002',
#                  '18470095834600003']	
parcel_numbers = ['18570006500300002', '18570005766100001', '18571046350100004', '18571047304900000', '18571046350100001']

all_addresses = []

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
    
    #Now scrape HTML results using BeautifulSoup and store in scraped_text
    scraped_text = []
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    body_tags = soup.find_all('td', valign='bottom')
    
    for tag in body_tags:
        scraped_text.append(tag.text)
        
    scraped_text = "!".join(scraped_text)
    
    #now parse scraped_text and use regular expressions to find address in raw text
    
    address_text = []

    pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+?!.+![A-Z][A-Z]!\d{5}-')
    matches = pattern.findall(scraped_text)
    
    print("length = ", len(matches))
       
    #first if statement is for the normal pattern of addresses ex: 3957 SUSAN DR GREEN COVE SPRINGS FL 32043
    if len(matches) != 0:
        print("if loop")
        for match in matches:
            match = match.replace("!", " ")    #removes '!' character from string
            match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
        
            address_text.append(match)
            
    #first elif statement is for address pattern with weird stuff on end ex: 7705 LAFAYETTE FOREST DR #13 ANNANDELE VA 22003      
    elif len(matches) == 0:
        print("1st elif loop")
        pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+? .?\d+?!.+![A-Z][A-Z]!\d{5}-')
        matches = pattern.findall(scraped_text)
        
        print("length = ", len(matches))
        
        if len(matches) != 0:
        
            for match in matches:
                match = match.replace("!", " ")    #removes '!' character from string
                match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
            
                address_text.append(match)
                
    #second elif statement is for mailing address that is a PO Box ex: P O BOX 369 BANNER ELK NC 28604    
        elif len(matches) == 0:
            print("Nested elif loop")
            pattern = re.compile(r'P O BOX \d+!.+![A-Z][A-Z]!\d{5}-')
            matches = pattern.findall(scraped_text)
            
            for match in matches:
                match = match.replace("!", " ")    #removes '!' character from string
                match = match.split("-", 1)[0]     #splits string on '-' character and takes first part

                address_text.append(match)

    
    all_addresses.append(address_text)
    
    time.sleep(2)    #sleep so that we don't bombard the server
    
print(all_addresses)





#####FOR CALDWELL COUNTY##### WORK IN PROGRESS
#Land on Caldwell County GIS Page
#driver.get('http://gis.caldwellcountync.org/maps/default.htm')
#
#test = driver.find_element_by_xpath('//*[@id="toolMenu"]/table/tr/td[1]')





