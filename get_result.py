#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:58:29 2021

@author: smilladue
"""

import numpy as np

def get_result(data,dataset):
    #transforms data(the one recieved from bath_processing function) into ordered numpy
    data=np.array(sorted(data, key=lambda tup: tup[0]))
    value=np.zeros(len(data))
    #checks if eyecolor in data is the same as eyecolor in dataset
    
    for i in range(len(data)):
        if data[i,1]==dataset[i,1]:
            value[i]=1
            
    #combines picturename and either 1 for same result or 0 for different result
    result=np.array((data[:,0],value)).T
    #counts numbers of same result
    correct=len(np.where(result=="1.0")[0])
    length=len(data)
    
    return result, correct, length
        
        