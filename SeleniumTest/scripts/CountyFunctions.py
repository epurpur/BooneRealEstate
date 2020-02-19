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



def watauga_tax_scraping(parcel_ids):
    """Goes to Watauga County Tax Page: http://tax.watgov.org/WataugaNC/search/commonsearch.aspx?mode=address
    and scrapes tax information about Watauga County condo parcels.
    
    Scraping is fairly straightforward. Selenium is used to click through buttons and enter text.
    Then BeautifulSoup is used to parse HTML information and return desired result."""
    
    
    #Land on Watauga County Tax page
    driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")

    
    driver.get('http://tax.watgov.org/WataugaNC/search/commonsearch.aspx?mode=address')
    driver.find_element_by_name('btAgree').click()                                                  #clicks 'Agree' button to agree to site's terms
    
    all_addresses = []
    
    for id_number in parcel_ids:
        
        try: 
            #Under 'Property Records' Tab, click on 'Parcel ID' option
            element_to_hover_over = driver.find_element_by_id('pd_Parent')                             #hover over 'property records' drop down menu
            hover = ActionChains(driver).move_to_element(element_to_hover_over)
            hover.perform()
            
            menu_options = driver.find_elements_by_class_name('PullDownMenuItem')
            parcel_id_button = menu_options[5]                                                #choose this menu option, which is 'Parcel ID'
            parcel_id_button.click()
            
            #Enter parcel ID values into input boxes
            driver.find_element_by_name('inpParid').send_keys(id_number)
            driver.find_element_by_name('btSearch').click()
            
            results = driver.find_element_by_class_name('SearchResults')                      #There will only be 1 result when searching by Parcel ID
            results.click()
            
            #Now look through results on Parcel ID landing page using Beautiful Soup. This prints all elements on the page
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            labels = soup.find_all('td', class_='DataletSideHeading')
            
            values = soup.find_all('td', class_='DataletData')
            
            mailing_address = [values[26].text, values[28].text]      #26th and 28th item in results are street address
            mailing_address = ' '.join(mailing_address)                #concatenate these into one mailing address string
        
            all_addresses.append(mailing_address)
                
            time.sleep(5)
            
        except Exception:
            
            print(Exception)
            
    print(all_addresses)



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
    all_addresses = []
    
    #iterate through each parcel number to scrape address from it
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
        
 
    #first if statement is for the normal pattern of addresses ex: 3957 SUSAN DR GREEN COVE SPRINGS FL 32043
        pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+?!.+![A-Z][A-Z]!\d{5}-')
        matches = pattern.findall(scraped_text)
                   
        if len(matches) != 0:

            for match in matches:
                match = match.replace("!", " ")    #removes '!' character from string
                match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
            
                all_addresses.append(match)
                
        #first elif statement is for address pattern with weird stuff on end ex: 7705 LAFAYETTE FOREST DR #13 ANNANDELE VA 22003      
        elif len(matches) == 0:
            pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+? .?\d+?!.+![A-Z][A-Z]!\d{5}-')
            matches = pattern.findall(scraped_text)
            
            
            if len(matches) != 0:
            
                for match in matches:
                    match = match.replace("!", " ")    #removes '!' character from string
                    match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
                
                    all_addresses.append(match)
                    
        #second elif statement is for mailing address that is a PO Box ex: P O BOX 369 BANNER ELK NC 28604    
            elif len(matches) == 0:
                pattern = re.compile(r'P O BOX \d+!.+![A-Z][A-Z]!\d{5}-')
                matches = pattern.findall(scraped_text)
                
                for match in matches:
                    match = match.replace("!", " ")    #removes '!' character from string
                    match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
    
                    all_addresses.append(match)
    
                
        time.sleep(2)    #sleep so that we don't bombard the server
        
    print(all_addresses)
    

