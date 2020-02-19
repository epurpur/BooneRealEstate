

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
##cant use the data yet, Avery county condo parcels are messed up. Manually got data for a good parcel number
#
##parcel_numbers = ['18570005766100001', '18570015196400003', '18570006101700002', '18571046350100004', '18571047202900002', '18571047202900002',
##                  '18470095834600003']	
#avery_parcel_numbers = ['18570006500300002', '18570005766100001', '18571046350100004', '18571047304900000', '18571046350100001']
#
#cf.avery_tax_scraping(avery_parcel_numbers)







#START HERE
####FOR CALDWELL COUNTY##### WORK IN PROGRESS

#Land on Caldwell County GIS Page
driver.get('http://tax.caldwellcountync.org/RealEstate.aspx')

#parcel_numbers = ['2817.03 13 9685', '2817.03 13 9683', '2817.03 13 9507']
parcel_numbers = ['2817.03 13 8631']

#holds final address list
all_addresses = []

for parcel_number in parcel_numbers:

    #enter parcel information into "PIN" box. Clear box first
    pin_entry_field = driver.find_element_by_name('ctl00$contentplaceholderRealEstateSearch$usercontrolRealEstateSearch$ctrlAlternateIdentifier$txtPIN')
    pin_entry_field.clear()
    
    pin_entry_field.send_keys(parcel_number)
    
    #click "search" button
    driver.find_element_by_name('ctl00$contentplaceholderRealEstateSearch$usercontrolRealEstateSearch$buttonSearch').click()
    #click 'Parcel #' Hyperlink button
    driver.find_element_by_class_name('HyperLinkField').click()
    #click on 'Owners' tab
    driver.find_element_by_id('__tab_ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners').click()
    
    #Now scrape HTML results using BeautifulSoup and store in scraped_text
    scraped_text = []
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
            
    body_tags = soup.find_all('td', valign='bottom')
            
    for tag in body_tags:
        scraped_text.append(tag.text)
    
    scraped_text = "!".join(scraped_text)
    
    #now parse scraped_text and use regular expressions to find address in raw text
    
    #first pattern is for weird mailing address ex: 4765 ASTON GARDENS WAY BLDG 4 UNIT 311
    #I had to include this first because the above address example is an outlier which does
    #return a match with normal regex expression, but it is an incorrect address
    pattern = re.compile(r'\d+ \w+ \w+ \w+ \d+ \w+ \d+!\w+![A-Z][A-Z]!\d{5}-')
    
    matches = pattern.findall(scraped_text)
    
    if len(matches) != 0:
    
        address_text = []
        
        for match in matches:
            
            match = match.replace("!", " ")    #removes '!' character from string
            match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
            
            address_text.append(match)
        
        #I just want one address returned
        if len(address_text) > 1:
            all_addresses.append(address_text[0])
        else:
            all_addresses.append(address_text)

    #first elif statement is for normal address pattern            
    elif len(matches) == 0:
        pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+?!.+![A-Z][A-Z]!\d{5}-')
        matches = pattern.findall(scraped_text)
        
        if len(matches) != 0:
        
            for match in matches:
                match = match.replace("!", " ")    #removes '!' character from string
                match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
    
                all_addresses.append(match)
    
####START HERE. PO BOX LOGIC    
    #second elif statement is for mailing address that is a PO Box ex: P O BOX 369 BANNER ELK NC 28604    
        elif len(matches) == 0:
            pattern = re.compile(r'P O BOX \d+!.+![A-Z][A-Z]!\d{5}-')
            matches = pattern.findall(scraped_text)
                
            for match in matches:
                match = match.replace("!", " ")    #removes '!' character from string
                match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
    
                all_addresses.append(match)

            
    time.sleep(2)     #sleep so that we don't bombard the server
    
print(all_addresses)


