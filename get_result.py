#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:58:29 2021

@author: smilladue
"""

import numpy as np
from correct_data import correct_data
from correct_dataset import correct_dataset 
from bath_processing import batch_processing
import pandas as pd 

def get_result(img_path, file):
    data=batch_processing(img_path)
    #corrects the data(the one recieved from bath_processing function) 
    datasetCorrect=correct_dataset(data, file)
    dataCorrect=correct_data(data, datasetCorrect)
    #sorts the data
    dataSorted=np.array(sorted(dataCorrect, key=lambda tup: tup[0]))
    datasetSorted=np.array(sorted(datasetCorrect, key=lambda tup: tup[0]))
    #print(dataSorted)
    #print(len(dataSorted))
    #print(datasetSorted)
    #print(len(datasetSorted))
    value=np.zeros(len(dataSorted))
    #checks if eyecolor in data is the same as eyecolor in dataset
    
    
    for i in range(len(dataSorted)):
        if dataSorted[i,1]=="Bad lighting":
            value[i]=2
        elif dataSorted[i,1]==datasetSorted[i,1]:
            value[i]=1
            
    #combines picturename and either 1 for same result or 0 for different result
    colors=np.array((dataSorted[:,1],datasetSorted[:,1])).T
    points=np.array((dataSorted[:,0],value)).T
    result=np.hstack((points,colors))
    #counts numbers of same result
    correct=len(np.where(points=='1.0')[0])
    badLighting=len(np.where(points=='2.0')[0])
    length=len(dataSorted)
    pd.DataFrame(result).to_csv(img_path+'.csv')
    
    return result, correct, badLighting, length
        
