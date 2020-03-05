#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:19:23 2020

@author: ep9k
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import re

######NEW AVERY SCRAPING
#parcel_numbers = ['18670277376400000', '18570006101700002', '1856006778670001201', '18570005970300004', '1869030325590000604', '18571046169200002']	
#
##parcel_numbers = ['1856006778670001201','18570005970300004']
#
#driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")
#
#driver.get('http://webtax.averycountync.gov/')
#
#address_data = []
#
#for parcel_number in parcel_numbers:
#    try:
#    
#        parcel_number_split = []
#                    
#        p1 = parcel_number[0:4]
#        parcel_number_split.append(p1)
#        p2 = parcel_number[4:6]
#        parcel_number_split.append(p2)
#        p3 = parcel_number[6:8]
#        parcel_number_split.append(p3)
#        p4 = parcel_number[8:12]
#        parcel_number_split.append(p4)
#        p5 = parcel_number[12:19]
#        parcel_number_split.append(p5)
#                    
#        #Clear input fields
#        map_ = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtMAP')
#        map_.clear()
#        sub = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtSUB')
#        sub.clear()
#        blk = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtBLK')
#        blk.clear()
#        lot = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtLOT')
#        lot.clear()
#        ext = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtEXT')
#        ext.clear()    
#        box_a = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtA')
#        box_a.clear()
#        box_b = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtB')            
#        box_b.clear()
#        
#        #Enter Parcel # into input boxes (Map, Sub, Blk, Lot, Ext)
#        map_.send_keys(parcel_number_split[0])
#        sub.send_keys(parcel_number_split[1])
#        blk.send_keys(parcel_number_split[2])
#        lot.send_keys(parcel_number_split[3])
#        ext.send_keys(parcel_number_split[4])
#                    
#        #Click buttons to get results
#        driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_buttonSearch').click()
#                    
#        driver.find_element_by_class_name('HyperLinkField').click()
#                    
#        driver.find_element_by_id('__tab_ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners').click()
#        
#        
#        
#        #scrape HTML
#        soup = BeautifulSoup(driver.page_source, 'html.parser')
#        
#        owner_name1 = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelAccountName1Value'})
#        owner_name2 = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelAccountName2Value'})
#        street_address = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddress'})
#        city_name = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddressCityValue'})
#        state_name = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddressStateValue'})
#        zip_code = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddressZipCodeValue'})
#    
#        #edit elements
#        owner_name = owner_name1.text + " " + owner_name2.text     #add owner names together (if more than one owner)
#        zip_code = zip_code.text
#        zip_code = zip_code.split('-')
#        zip_code = zip_code[0]
#        full_mailing_address = street_address.text + " " + city_name.text + ", " + state_name.text + " " + zip_code
#        
#        address_data.append((owner_name, full_mailing_address))
#
#    except Exception:
#        address_data.append("missing data")
#
#    time.sleep(1)
#
#driver.quit()   
#
#print(address_data)



#####NEW WATAUGA SCRAPING
#
#parcel_numbers = ['2807-96-1821-028', '2900-35-3309-000', '1899-02-5855-005', '1889-40-5220-022', '2829-29-6141-006', '2920-00-5392-049']
#
#driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")
#
#driver.get('http://tax.watgov.org/WataugaNC/search/commonsearch.aspx?mode=address')
#driver.find_element_by_name('btAgree').click()                                                  #clicks 'Agree' button to agree to site's terms
#
#for parcel_number in parcel_numbers:
#
#    
#    try:
#        element_to_hover_over = driver.find_element_by_id('pd_Parent')                             #hover over 'property records' drop down menu
#        hover = ActionChains(driver).move_to_element(element_to_hover_over)
#        hover.perform()
#            
#        menu_options = driver.find_elements_by_class_name('PullDownMenuItem')
#        parcel_id_button = menu_options[5]                                                #choose this menu option, which is 'Parcel ID'
#        parcel_id_button.click()
#            
#        #Enter parcel ID values into input boxes
#        driver.find_element_by_name('inpParid').send_keys(parcel_number)
#        driver.find_element_by_name('btSearch').click()
#            
#        results = driver.find_element_by_class_name('SearchResults')                      #There will only be 1 result when searching by Parcel ID
#        results.click()
#        
#        soup = BeautifulSoup(driver.page_source, 'html.parser')
#        
#        labels = soup.find_all('td', class_='DataletSideHeading')
#            
#        values = soup.find_all('td', class_='DataletData')
#           
#        owner_name = values[24].text
#        mailing_address = [values[26].text, values[28].text]      #26th and 28th item in results are street address
#        mailing_address = ' '.join(mailing_address)                #concatenate these into one mailing address string
#        
#        print(owner_name)
#        print(mailing_address)
#
#
#    except Exception:
#            
#        print('no match')
#
#    time.sleep(1)
#
#        
#driver.quit()        



#####NEW CALDWELL SCRAPING

parcel_numbers = ['2817.03 13 8631', '2817.03 13 9516', '2817.03 03 7595', '2817.03 13 7694']

driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")

driver.get('http://tax.caldwellcountync.org/RealEstate.aspx')

all_addresses = {}
all_owner_names = {}


for parcel_number in parcel_numbers:

    try:
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
    
    
        #scrape HTML
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        owner_name1 = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelAccountName1Value'})
        owner_name2 = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelAccountName2Value'})
        street_address = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddress'})
        city_name = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddressCityValue'})
        state_name = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddressStateValue'})
        zip_code = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddressZipCodeValue'})
        
        owner_name = owner_name1.text + " " + owner_name2.text
        zip_code = zip_code.text
        zip_code = zip_code.split('-')
        zip_code = zip_code[0]
        full_mailing_address = street_address.text + " " + city_name.text + ", " + state_name.text + " " + zip_code

        all_addresses.update({parcel_number: full_mailing_address})
        all_owner_names.update({parcel_number: owner_name})
    
    except Exception:
        pass
    

