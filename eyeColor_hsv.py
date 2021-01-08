#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:19:45 2021

@author: smilladue
"""
import numpy as np
import cv2 
import dlib
from find_iris_data import find_iris_data
import colorsys
import matplotlib as plt



def eyeColor_hsv(image):
    #finds iris in image
    img=find_iris_data(image)
    
    #converts pixels of rgb to csv
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    numbers=[]
    
    #counts number of pixels in the different ranges of colors and appends to empty list
    
    Brown=(10, 70, 0), (22, 255, 206)
    numbers.append(np.count_nonzero(cv2.inRange(hsv, Brown[0], Brown[1])))

    Green=(20, 0, 42), (123, 232, 180)
    numbers.append(np.count_nonzero(cv2.inRange(hsv, Green[0], Green[1])))

    Blue=(120, 0, 0), (160, 100, 180)
    numbers.append(np.count_nonzero(cv2.inRange(hsv, Blue[0], Blue[1])))
    
    BLight1=(150, 60, 0), (179, 255, 170)
    Blight1=np.count_nonzero(cv2.inRange(hsv, BLight1[0], BLight1[1]))
    
    BLight2=(0, 100, 50), (6, 255, 110)
    numbers.append(Blight1+np.count_nonzero(cv2.inRange(hsv, BLight2[0], BLight2[1])))
    #print(np.count_nonzero(hsv))
    #print(numbers)
    
    colors=(["Brown","Green","Blue", "Bad lighting"])
    #combines the count of pixels in a category to the category
    count=np.array((numbers,colors))
    
    #finds the biggest number of pixels that fits with a range of color
    maxi=str(max(numbers))
    
    #finds the category, which has most pixels that fits
    dominantColor=colors[np.where(count==maxi)[1][0]]
    
    return dominantColor





"""
count=np.array((numbers,colors)).T
countsorted=sorted(count, key=lambda tup: tup[0])


for i in range(7):
    np.count_nonzero(cv2.inRange(hsv, ((166, 21, 50), (240, 100, 85))))
    
    
    
hsv=cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
img = cv2.inRange(hsv, ((166, 21, 50), (240, 100, 85)))
np.count_nonzero(blue)



#go from rgb to hsv
hsv=cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
#as a vector
pixelhsv=np.float32(hsv.reshape(-1, 3))


blue = cv2.inRange(hsv, ((166, 21, 50), (240, 100, 85)))

np.count_nonzero(blue)

"""
