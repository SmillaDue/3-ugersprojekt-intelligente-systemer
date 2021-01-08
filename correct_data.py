#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 13:03:11 2021

@author: smilladue
"""

from collections import Counter
import numpy as np

def correct_data(data, dataset):
    datanp=np.array(data)
    lines=np.zeros(len(data),dtype=bool)
    counter=Counter(np.hstack((dataset[:,0],datanp[:,0])))
    result = [i for i, j in counter.items() if j > 1]
    for i in range(len(result)):
        #creates array with row-number of repeated pictures   
        correct=np.asarray(np.where(datanp[:,0]==result[i]))[0]
        lines[correct]=True
    datanp=datanp[lines]
    return datanp