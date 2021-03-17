# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:09:23 2019

This program works with NOAA GOES - 16/17 satellite data

@author: Rick
"""

import glob
import re

pathin1 ='../GOES_16_data/data/*RadM*.nc'
pathin2 ='../GOES_16_data/data/*.nc'

for filename1 in sorted(glob.glob(pathin1)):
    searchstr = filename1[48:63]
    
    
    

    filelist = []
    count = 0
    for filename2 in sorted(glob.glob(pathin2)):
        if re.search(searchstr, filename2):
            count += 1
            filelist.append(filename2[0:110])

    if count < 3:
        print(searchstr)
        print(count)
        print(filelist)
