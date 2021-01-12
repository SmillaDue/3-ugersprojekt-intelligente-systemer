#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:32:12 2021

@author: smilladue
"""
import numpy as np
from get_result import get_result
from correct_dataset import correct_dataset 
from bath_processing import batch_processing
import pandas as pd 


def get_multiple_result(img_path, file):
    get_result(img_path+'/Brown', file)
    get_result(img_path+'/Blue', file)
    get_result(img_path+'/Green', file)


#'/Users/smilladue/Desktop/Documents/DTU/Intelligente_systemer/Projekt/Faces/Test'
#'labels_utf8.csv'
#get_multiple_result('/Users/smilladue/Desktop/Documents/DTU/Intelligente_systemer/Projekt/Faces/Test', 'labels_utf8.csv')