# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:48:27 2021

@author: rickd
"""

import cv2, os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob

import random

def give_color_to_seg_img(seg,n_classes):
    '''
    seg : (input_width,input_height,3)
    '''
    
    if len(seg.shape)==3:
        seg = seg[:,:,0]
    seg_img = np.zeros( (seg.shape[0],seg.shape[1],3) ).astype('float')
    colors = sns.color_palette("hls", n_classes)
    
    for c in range(n_classes):
        segc = (seg == c)
        seg_img[:,:,0] += (segc*( colors[c][0] ))
        seg_img[:,:,1] += (segc*( colors[c][1] ))
        seg_img[:,:,2] += (segc*( colors[c][2] ))

    return(seg_img)

dir_data = "../GOES_16_data/datasetpng"
dir_seg = dir_data + "/annotations_prepped_train/*.png"
dir_img = dir_data + "/images_prepped_train/"


n_classes = 5
input_height , input_width = 224 , 224
output_height , output_width = 224 , 224


# pickout three random files from image list
filenamelist = random.sample(sorted(glob.glob(dir_seg)), 3)

for filen in filenamelist:
    searchstr = filen[53:69]
    #print(searchstr)
    
# =============================================================================
    ## seaborn has white grid by default so I will get rid of this.
    sns.set_style("whitegrid", {'axes.grid' : False})
    
    ## read in the original image and segmentation labels
    seg = cv2.imread(filen)
    img_is = cv2.imread(dir_img+searchstr+'i.png')
    print("seg.shape={}, img_is.shape={}".format(seg.shape,img_is.shape))

    seg_img = give_color_to_seg_img(seg,n_classes)

    fig = plt.figure(figsize=(20,40))
    ax = fig.add_subplot(1,4,1)
    ax.imshow(seg_img)
    
    ax = fig.add_subplot(1,4,2)
    ax.imshow(img_is/255.0)
    ax.set_title("original image {}".format(img_is.shape[:2]))
    
    ax = fig.add_subplot(1,4,3)
    ax.imshow(cv2.resize(seg_img,(input_height , input_width)))
    
    ax = fig.add_subplot(1,4,4)
    ax.imshow(cv2.resize(img_is,(output_height , output_width))/255.0)
    ax.set_title("resized to {}".format((output_height , output_width)))
    plt.show()