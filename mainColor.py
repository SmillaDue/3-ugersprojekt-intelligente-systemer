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

"""
BY SELECTING PALETTE, THE 5 CLUSTERS SHOWS

TO see plots:
import matplotlib.pyplot as plt

avg_patch = np.ones(shape=img.shape, dtype=np.uint8)*np.uint8(average)

indices = np.argsort(counts)[::-1]   
freqs = np.cumsum(np.hstack([[0], counts[indices]/float(counts.sum())]))
rows = np.int_(img.shape[0]*freqs)

dom_patch = np.zeros(shape=img.shape, dtype=np.uint8)
for i in range(len(rows) - 1):
    dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(palette[indices[i]])
    
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12,6))
ax0.imshow(avg_patch)
ax0.set_title('Average color')
ax0.axis('off')
ax1.imshow(dom_patch)
ax1.set_title('Dominant colors')
ax1.axis('off')
plt.show(fig)

"""



