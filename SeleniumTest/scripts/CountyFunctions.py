#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:36:36 2020

@author: ep9k
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import pandas as pd
import re



def watauga_tax_scraping(parcel_numbers):
    """Goes to Watauga County Tax Page: http://tax.watgov.org/WataugaNC/search/commonsearch.aspx?mode=address
    and scrapes tax information about Watauga County condo parcels.
    
    Scraping is fairly straightforward. Selenium is used to click through buttons and enter text.
    Then BeautifulSoup is used to parse HTML information and return desired result."""
    
    
    #Land on Watauga County Tax page
    driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")

    
    driver.get('http://tax.watgov.org/WataugaNC/search/commonsearch.aspx?mode=address')
    driver.find_element_by_name('btAgree').click()                                                  #clicks 'Agree' button to agree to site's terms
    
    all_addresses = {}
    all_owner_names = {}
    
    for parcel_number in parcel_numbers:
        
        time.sleep(2)
        
        try: 
            #Under 'Property Records' Tab, click on 'Parcel ID' option
            element_to_hover_over = driver.find_element_by_id('pd_Parent')                             #hover over 'property records' drop down menu
            hover = ActionChains(driver).move_to_element(element_to_hover_over)
            hover.perform()
            
            menu_options = driver.find_elements_by_class_name('PullDownMenuItem')
            parcel_id_button = menu_options[5]                                                #choose this menu option, which is 'Parcel ID'
            parcel_id_button.click()
            
            #Enter parcel ID values into input boxes
            driver.find_element_by_name('inpParid').send_keys(parcel_number)
            driver.find_element_by_name('btSearch').click()
            
            results = driver.find_element_by_class_name('SearchResults')                      #There will only be 1 result when searching by Parcel ID
            results.click()
            
            #Now look through results on Parcel ID landing page using Beautiful Soup. This prints all elements on the page
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
#            labels = soup.find_all('td', class_='DataletSideHeading')
            
            values = soup.find_all('td', class_='DataletData')

            owner_name = values[24].text
            mailing_address = [values[26].text, values[28].text]      #26th and 28th item in results are street address
            mailing_address = ' '.join(mailing_address)                #concatenate these into one mailing address string
        
            #add parcel_number, mailing_address as key:value pairs to all_addresses dictionary
            #add parcel_number, owner name as key:value pairs to all_owner_names dictionary
            all_addresses.update({parcel_number: mailing_address})
            all_owner_names.update({parcel_number: owner_name})
            
        except Exception:
            
            #add id_number, "no match..." as key:value pairs to all_addresses dict if there is an error
            all_addresses.update({parcel_number: "No match for Parcel ID"})
            all_owner_names.update({parcel_number: "No match for Parcel ID"})
            
    driver.quit()        
            
    return all_addresses, all_owner_names


def watauga_subset_df_parcel_sample(watauga_df):
    """I've had to divide the Watauga County dataframe into pieces of 500 parcels because
    I keep getting booted by the Watauga County real estate site. This takes the section of the
    dataframe that I've chosen and returns a list of the Parcel IDs from the 'Updated Parcel ID' column"""
    
    return watauga_df['Updated Parcel ID'].tolist()



def avery_tax_scraping(parcel_numbers):
    """Goes to Avery County Tax page: http://webtax.averycountync.gov/RealEstate.aspx
    and scrapes tax information about Avery County condo parcels.
    
    Scraping is more difficult. Selenium is used to click through buttons and enter text.
    Text is presented in one big blob which I then have to parse through and use regular expressions
    to identify pattern of address."""
    
    driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")
    
    #Land on Avery county tax website (real estate search)
    driver.get('http://webtax.averycountync.gov/')

    #holds final address list
    all_addresses = {}
    all_owner_names = {}

    
    #iterate through each parcel number to scrape address from it
    for parcel_number in parcel_numbers:
       
        time.sleep(2)
    
        try:
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
            box_a = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtA')
            box_a.clear()
            box_b = driver.find_element_by_id('ctl00_contentplaceholderRealEstateSearch_usercontrolRealEstateSearch_ctrlParcelNumber_txtB')            
            box_b.clear()
            
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

            owner_name1 = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelAccountName1Value'})
            owner_name2 = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelAccountName2Value'})
            street_address = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddress'})
            city_name = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddressCityValue'})
            state_name = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddressStateValue'})
            zip_code = soup.find('span', {'id': 'ctl00_contentplaceholderRealEstateWorkplace_tabcontainerWorkSpace_tabpanelOwners_usercontrolRealEstateParcelOwnersData_labelMailingAddressZipCodeValue'})
        
            #edit elements
            owner_name = owner_name1.text + " " + owner_name2.text     #add owner names together (if more than one owner)
            zip_code = zip_code.text
            zip_code = zip_code.split('-')
            zip_code = zip_code[0]
            full_mailing_address = street_address.text + " " + city_name.text + ", " + state_name.text + " " + zip_code
            
            all_addresses.update({parcel_number: full_mailing_address})
            all_owner_names.update({parcel_number: owner_name})
    
        except Exception:
            
            all_addresses.update({parcel_number: "No match for Parcel ID"})
            all_owner_names.update({parcel_number: "No match for Parcel ID"})

    driver.quit()

    return all_addresses, all_owner_names     #returns these items in a tuple
    


def caldwell_tax_scraping(parcel_numbers):
    """Goes to Caldwell County Tax page: http://tax.caldwellcountync.org/RealEstate.aspx
    and scrapes tax information about Caldwell County condo parcels
    
    Scraping is similar to Avery County. Selenium is used to click through buttons and enter text.
    Text is presented in one big blob which I then have to parse through and use regular expressions
    to identify pattern of address."""
    
    driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")

    #Land on Caldwell County GIS Page
    driver.get('http://tax.caldwellcountync.org/RealEstate.aspx')
    
    
    #holds final address list
    all_addresses = {}
    all_owner_names = {}
    
    for parcel_number in parcel_numbers:
    
        time.sleep(2)
        
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
            
            #edit elements
            owner_name = owner_name1.text + " " + owner_name2.text
            zip_code = zip_code.text
            zip_code = zip_code.split('-')
            zip_code = zip_code[0]
            full_mailing_address = street_address.text + " " + city_name.text + ", " + state_name.text + " " + zip_code
    
    
            all_addresses.update({parcel_number: full_mailing_address})
            all_owner_names.update({parcel_number: owner_name})
        
        
        except Exception:
            
            all_addresses.update({parcel_number: "No match for Parcel ID"})
            all_owner_names.update({parcel_number: "No match for Parcel ID"})
                        
    driver.quit()        
        
    return all_addresses, all_owner_names
    
    
    
def map_function(addresses_dict, owner_names_dict, parcel_ids_df):
    """Uses map() function to map addresses to corresponding parcel ID
       Uses map() function to map owner names to corresponding parcel ID number
       Result is a dataframe with 2 added columns, 'UpdatedMailingAddress' and 'UpdatedOwnerName'
    """
    
    parcel_ids_df['UpdatedMailingAddress'] = parcel_ids_df['Updated Parcel ID'].map(addresses_dict)
    parcel_ids_df['UpdatedOwnerName'] = parcel_ids_df['Updated Parcel ID'].map(owner_names_dict)
    
    return parcel_ids_df
    
    
    
    