

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import pandas as pd

import CountyFunctions as cf

#driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")


#####FOR WATAUGA COUNTY#####EXAMPLE
parcel_ids = ['2911911616001', '2911911616002']

matt_condo_list = pd.read_csv('/Users/ep9k/Desktop/BRE/BRE 2019/MattCondoAddressList.csv')

#START HERE. parse matt_condo_list for rows that have County=='Watauga', then get Parcel ID for those rows
watauga_parcel_ids = "empty"
#try:
#    cf.watauga_tax_scraping(parcel_ids)
#    
#except Exception:
#    
#    print(Exception)
#    time.sleep(5)
#    cf.watauga_tax_scraping(parcel_ids)
    



##Enter parcel ID values into input boxes
#driver.find_element_by_name('inpParid').send_keys('2911911616001')
#driver.find_element_by_name('btSearch').click()
#
#results = driver.find_element_by_class_name('SearchResults')                      #There will only be 1 result when searching by Parcel ID
#results.click()
#
##Now look through results on Parcel ID landing page using Beautiful Soup. This prints all elements on the page
#soup = BeautifulSoup(driver.page_source, 'html.parser')
#
#labels = soup.find_all('td', class_='DataletSideHeading')
#
#values = soup.find_all('td', class_='DataletData')
#
#mailing_address = [values[26].text, values[28].text]      #26th and 28th item in results are street address
#mailing_address = ' '.join(mailing_address)                #concatenate these into one mailing address string



#####FOR AVERY COUNTY#####
#cant do this yet, Avery county condo parcels are messed up



#####FOR CALDWELL COUNTY##### WORK IN PROGRESS
#Land on Caldwell County GIS Page
#driver.get('http://gis.caldwellcountync.org/maps/default.htm')

#Hover over 'enter serach string' and select 'Parcel ID'
#elements_to_hover_over = driver.find_elements_by_class_name('dijitTabInner dijitTabContent dijitTab dijitTabChecked dijitChecked dijitTabFocused dijitTabCheckedFocused dijitCheckedFocused dijitFocused')
#hover = ActionChains(driver).move_to_element(element_to_hover_over)
#hover.perform()




