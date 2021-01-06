#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:45:08 2021

@author: smilladue
"""

import numpy as np
import cv2 
import dlib
from find_iris_data import find_iris_data
import colorsys
from mainColor import mainColor

#checks if a hsv belongs to a specific color
def check_color(hsv, color):
    if (hsv[0] >= color[0][0]) and (hsv[0] <= color[1][0]) and (hsv[1] >= color[0][1]) and \
    hsv[1] <= color[1][1] and (hsv[2] >= color[0][2]) and (hsv[2] <= color[1][2]):
        return True
    else:
        return False


def mainColor_category(method,image):
    class_name = ("Blue", "Blue Gray", "Brown", "Brown Gray", "Brown Black", "Green", "Green Gray", "Other")
    EyeColor = {
        class_name[0] : ((166, 21, 50), (240, 100, 85)),
        class_name[1] : ((166, 2, 25), (300, 20, 75)),
        class_name[2] : ((2, 20, 20), (40, 100, 60)),
        class_name[3] : ((20, 3, 30), (65, 60, 60)),
        class_name[4] : ((0, 10, 5), (40, 40, 25)),
        class_name[5] : ((60, 21, 50), (165, 100, 85)),
        class_name[6] : ((60, 2, 25), (165, 20, 65))}
    
    if method == "average":
        average=mainColor("average", image)
        #converts rgb value to hsv
        hsv=colorsys.rgb_to_hsv(average[0],average[1],average[2])
    
    if method == "kmeans":
        kmeans=mainColor("kmeans", image)
        hsv=colorsys.rgb_to_hsv(kmeans[0],kmeans[1],kmeans[2])
    
    color_id = 7
    for i in range(len(class_name)-1):
        #checks all color categorys to see in wich one the given hsv belongs 
        if check_color(hsv, EyeColor[class_name[i]]) == True:
            color_id = i
    category=class_name[color_id]
            
    return category
            
            
            
            
            
            
            
            
            
            
            
            