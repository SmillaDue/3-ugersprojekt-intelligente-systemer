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
    img=cv2.imread(image)
    
    #converts pixels of rgb to csv
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    numbers=[]
    
    #counts number of pixels in the different ranges of colors and appends to empty list

   
    Brown=(0, 80, 0), (25, 255, 130)
    numbers.append(np.count_nonzero(cv2.inRange(hsv, Brown[0], Brown[1])))

    Green=(6, 0, 50), (100, 55, 162)
    numbers.append(np.count_nonzero(cv2.inRange(hsv, Green[0], Green[1])))

    Blue=(105, 40, 40), (150, 255, 255)
    numbers.append(np.count_nonzero(cv2.inRange(hsv, Blue[0], Blue[1])))
    
    
    #BLight1=(170, 60, 0), (179, 255, 170)
    #Blight1=np.count_nonzero(cv2.inRange(hsv, BLight1[0], BLight1[1]))
    BLight2=(0, 115, 0), (10, 255, 255)
    BLight=np.count_nonzero(cv2.inRange(hsv, BLight2[0], BLight2[1]))
    White=(0,0,255),(179,255,255)
    whitePix=np.count_nonzero(cv2.inRange(hsv, White[0], White[1]))
    
    if whitePix>10:
        numbers[2]=numbers[2]*(1/2)
        numbers[1]=numbers[1]*(1/2)
    
    #print(image)    
    #print(np.count_nonzero(hsv))
    #print(numbers)
    #print(whitePix)
    #print(BLight)
    
    colors=(["Brown","Green","Blue"])
    #combines the count of pixels in a category to the category
    count=np.array((numbers,colors))
    
    #finds the biggest number of pixels that fits with a range of color
    maxi=str(max(numbers))
    
    #finds the category, which has most pixels that fits
    dominantColor=colors[np.where(count==maxi)[1][0]]
    print(dominantColor)
    
    #if (np.count_nonzero(hsv)/3)-40*numbers[2]<0:
       # dominantColor='Blue'
    
    if (np.count_nonzero(hsv)/3)-2*BLight<0:
        dominantColor='Bad lighting'
    
    return dominantColor

    #lower_blue = np.array([110,50,50])
    #upper_blue = np.array([130,255,255])
