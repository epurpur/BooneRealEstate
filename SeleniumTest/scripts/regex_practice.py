#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:22:00 2020

@author: ep9k
"""

import re

pattern_text = []

with open('/Users/ep9k/Desktop/SeleniumTest/regex_avery_practice_text.txt') as f:
    
    contents = f.read()
    

#    pattern = re.compile(r'[A-Z]\w+!\d{5}')
    pattern = re.compile(r'\d+ \w+ \w+!.+![A-Z][A-Z]!\d{5}-')
    
    matches = pattern.findall(contents)
    
    for match in matches:
        match = match.replace("!", " ")    #removes '!' character from string
        match = match.split("-", 1)[0]     #splits string on '-' character and takes first part
        
        pattern_text.append(match)
        
    
