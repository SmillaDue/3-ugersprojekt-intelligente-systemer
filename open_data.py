#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:18:25 2021

@author: smilladue
"""
import numpy as np
import pandas as pd

def open_data(filename):
    #filename="labels_utf8.csv"
    #Load the input file into a DataFrame 
    file=pd.read_csv(filename,sep=",",header=0)
    #Turn the DataFrame into a np.array matrix
    data=np.array(file)
    dataset=np.array((data[:,0],data[:,5])).T
    return dataset




