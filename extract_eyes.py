# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:34:27 2021

@author: rune7
"""

import dlib
import numpy as np
import cv2
from shape_to_np import shape_to_np
import os
from find_iris_data import find_iris_data
import glob


#img_path = 'C:\\Users\\rune7\\Documents\\AI'
#out_path = 'C:\\Users\\rune7\\Documents\\AI\\Output'






def extract_eyes(img_path,out_path):
    for f in glob.glob(os.path.join(img_path, "*.jpg")):        
        
        filename = os.path.basename(f)
        #udføre beskæring
        iris = find_iris_data(filename)
        
        img = cv2.cvtColor(iris, cv2.COLOR_BGR2RGB)


        width = int(50)
        height = int(img.shape[0] / img.shape[1] * width)
        dim = (width, height)
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
               
        #gemme beskåret del til ny mappe, med samme navn
        
        
        cv2.imwrite(out_path+'/'+filename,resized)
        
    
        
        
        
        