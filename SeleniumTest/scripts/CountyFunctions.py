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


def watauga_tax_scraping(parcel_ids):

    
    #Land on Watauga County Tax page
    driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")

    
    driver.get('http://tax.watgov.org/WataugaNC/search/commonsearch.aspx?mode=address')
    driver.find_element_by_name('btAgree').click()                                                  #clicks 'Agree' button to agree to site's terms
    
    
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
        
            print(mailing_address)
                
            time.sleep(5)
            
        except Exception:
            
            print(Exception)
