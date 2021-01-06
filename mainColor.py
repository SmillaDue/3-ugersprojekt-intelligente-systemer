#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:52:00 2021

@author: smilladue
"""



import numpy as np
import cv2 
import dlib
from find_iris_data import find_iris_data

"""

img = dlib.load_rgb_image("Face1.jpg")

pixels=np.float32(img.reshape(-1, 3))

n_colors = 5
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
flags = cv2.KMEANS_RANDOM_CENTERS

_, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
_, counts = np.unique(labels, return_counts=True)

https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv

"""

def mainColor(method,picture):
    img = find_iris_data(picture)
    
    if method == "average":
        dominantColor=img.mean(axis=0).mean(axis=0)
    
    if method == "kmeans":
        #converts to numpy array 
        pixels=np.float32(img.reshape(-1, 3))
        
        #defines the different aspects in cluster analysis
        n_colors = 5
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv2.KMEANS_RANDOM_CENTERS
        
        #kmeans analysis
        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)
        
        #Dominant color in the kmeans analysis
        dominantColor=palette[np.argmax(counts)]
    
    return method, dominantColor