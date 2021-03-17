# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:09:23 2019

This program works with NOAA GOES - 16/17 satellite data

@author: Rick
"""


from netCDF4 import Dataset
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


import glob
import re

def crop_center(img,cropx,cropy):
    y,x = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)
    return img[starty:starty+cropy,startx:startx+cropx]

pathinRadM15 = '../GOES_16_data/data/*RadM*M6C15*.nc'
pathinRadM13 = '../GOES_16_data/data/*RadM*M6C13*.nc'

pathinPhase ='../GOES_16_data/data/*ACTPM*.nc'

for filename15 in sorted(glob.glob(pathinRadM15)):
    searchstr = filename15[48:63]
    print(searchstr)
    
    # read GOES-16 channel 15 data
    g16nc = Dataset(filename15, 'r')
    radiance15 = g16nc.variables['Rad'][:]
    g16nc.close()
    g16nc = None
    
    for filename13 in sorted(glob.glob(pathinRadM13)):
        if re.search(searchstr, filename13):
            # read GOES-16 channel 15 data
            g16nc = Dataset(filename13, 'r')
            radiance13 = g16nc.variables['Rad'][:]
            g16nc.close()
            g16nc = None
            
            break
        
    radiance15 = crop_center(radiance15,224,224)
    #fig = plt.figure(figsize=(4,4),dpi=200)
    #im = plt.imshow(radiance15, cmap='Greys_r')
    #cb = fig.colorbar(im, orientation='horizontal')
    #cb.set_ticks([0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1])
    #cb.set_label('ch15 Radiance (W m-2 sr-1 um-1)')
    #plt.show()
    
    radiance13 = crop_center(radiance13,224,224)
        
    radiance15m13 = radiance15 - radiance13
#   print(radiance15m13.shape)
#   print(radiance15m13.min())
#   print(radiance15m13.max())
    
    #min = radiance15m13.min()
    #max = radiance15m13.max()
    img_mean = radiance15m13.mean()
    img_std = radiance15m13.std() 
    
    #X_train = (radiance15m13 - min) / (max - min)
    X_train = (radiance15m13 - img_mean) / (img_std)

    matplotlib.image.imsave(searchstr+'_i.png', X_train, cmap='gray',format='png')
     
     
    for filenamePhase in sorted(glob.glob(pathinPhase)):
        if re.search(searchstr, filenamePhase):
            # read GOES-16 channel 15 data
            g16nc = Dataset(filenamePhase, 'r')
            Phase = g16nc.variables['Phase'][:]
            g16nc.close()
            g16nc = None
            break
        
    Phase = crop_center(Phase,224,224)
    Phase[223,223] = 255
    matplotlib.image.imsave(searchstr+'_p.png', Phase, cmap='gray',format='png')
    
    print(X_train.max())
    print(X_train.min())

