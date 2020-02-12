#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:16:32 2020

@author: ep9k
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup


driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")


driver.get('https://www.virginia.edu/calendar')

test = driver.find_element_by_class_name('tabViewWrapper')


#driver.find_element_by_class_name('twContentCell')

#soup = BeautifulSoup(driver.page_source, 'html.parser')
#
#
#test = soup.find_all('td', class_='twContentCell')



