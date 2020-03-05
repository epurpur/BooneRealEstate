#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:22:00 2020

@author: ep9k
"""

import re

pattern_text = []

#with open('/Users/ep9k/Desktop/SeleniumTest/regex_avery_practice_text.txt') as f:
#    
#    contents = f.read()
#    
#
#old pattern    pattern = re.compile(r'\d+ \w+ \w+!.+![A-Z][A-Z]!\d{5}-')
#    pattern = re.compile(r'\d+ \w+ ?\w+?!.+![A-Z][A-Z]!\d{5}-')
#    
#    matches = pattern.findall(contents)
#    
#    for match in matches:
#        match = match.replace("!", " ")    #removes '!' character from string
#        match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
#      
#        pattern_text.append(match)
      

  
    
#with open('/Users/ep9k/Desktop/SeleniumTest/regex_avery_practice_text2.txt') as f:
#    
#    contents = f.read()
#    
###old pattern    pattern = re.compile(r'\d+ \w+ \w+!.+![A-Z][A-Z]!\d{5}-')
#    pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+?!.+![A-Z][A-Z]!\d{5}-')
#    
#    matches = pattern.findall(contents)
#
#    for match in matches:
#
#        match = match.replace("!", " ")    #removes '!' character from string
#        match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
#      
#        pattern_text.append(match)


##7705 LAFAYETTE FOREST DR #13!ANNANDELE!VA!22003-
#with open('/Users/ep9k/Desktop/SeleniumTest/regex_avery_practice_text3.txt') as f:
#    
#    contents = f.read()
#    
##p1    pattern = re.compile(r'\d+ \w+ ?\w+? ?\w!.+![A-Z][A-Z]!\d{5}-')
##general pattern    pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+?!.+![A-Z][A-Z]!\d{5}-')
##specialty pattern  pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+? .?\d+?!.+![A-Z][A-Z]!\d{5}-')
#    pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+? .?\d+?!.+![A-Z][A-Z]!\d{5}-')
#    
#    matches = pattern.findall(contents)
#
#    for match in matches:
##        print(match)
#        match = match.replace("!", " ")    #removes '!' character from string
#        match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
#
#        pattern_text.append(match)
#
#print(pattern_text)


#P O BOX 369!BANNER ELK!NC!28604-
with open('/Users/ep9k/Desktop/SeleniumTest/regex_avery_practice_text4.txt') as f:
    
    contents = f.read()
    
#p1    pattern = re.compile(r'\d+ \w+ ?\w+? ?\w!.+![A-Z][A-Z]!\d{5}-')
#general pattern    pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+?!.+![A-Z][A-Z]!\d{5}-')
#specialty pattern  pattern = re.compile(r'\d+ \w+ ?\w+? ?\w+? .?\d+?!.+![A-Z][A-Z]!\d{5}-')
    pattern = re.compile(r'P O BOX \d+!.+![A-Z][A-Z]!\d{5}-')
    
    matches = pattern.findall(contents)

    for match in matches:
#        print(match)
        match = match.replace("!", " ")    #removes '!' character from string
        match = match.split("-", 1)[0]     #splits string on '-' character and takes first part

        pattern_text.append(match)

print(pattern_text)





