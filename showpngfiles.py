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


dir_data = "../GOES_16_data/datasetpng"
dir_seg = dir_data + "/annotations_prepped_train/*.png"
dir_img = dir_data + "/images_prepped_train/"

# pickout three random files from list
#filenamelist = random.sample(sorted(glob.glob(dir_seg)), 3)

# uncomment filenamelist below if you want to see
# all the images
filenamelist = sorted(glob.glob(dir_seg))

for filen in filenamelist:
    searchstr = filen[53:69]
    print(searchstr)
    
# =============================================================================
    ## seaborn has white grid by default so I will get rid of this.
    sns.set_style("whitegrid", {'axes.grid' : False})
# 
# 
# ldseg = np.array(os.listdir(dir_seg))
# ## pick the first image file
# fnm = ldseg[1]
# print(fnm)
# 
    ## read in the original image and segmentation labels
    seg = cv2.imread(filen)
    img_is = cv2.imread(dir_img+searchstr+'i.png')
    print("seg.shape={}, img_is.shape={}".format(seg.shape,img_is.shape))
 
    ## Check the number of labels
    mi, ma = 0,4
    n_classes = ma - mi + 1
    print("minimum seg = {}, maximum seg = {}, Total number of segmentation classes = {}".format(mi,ma, n_classes))
 
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(1,1,1)
    ax.imshow(img_is)
    ax.set_title("original image")
    plt.show()
 
    fig = plt.figure(figsize=(15,10))
    for k in range(mi,ma+1):
        ax = fig.add_subplot(1,n_classes,k+1)
        ax.imshow((seg == k)*1.0)
        ax.set_title("label = {}".format(k))

    plt.show()
    input("Press Enter to continue...")
