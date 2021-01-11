#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:24:54 2021

@author: smilladue
"""

from collections import Counter
import numpy as np
from open_data import open_data
import glob
import os

def correct_dataset(data, file):
    dataset=open_data(file)
    #data = []
    #for f in glob.glob(os.path.join(img_path, "*")):
        #filename = os.path.basename(f)
        #data.append(filename)
    datanp=np.array(data)
    lines=np.zeros(len(dataset),dtype=bool)
    counter=Counter(np.hstack((dataset[:,0],datanp[:,0])))
    result = [i for i, j in counter.items() if j > 1]
    for i in range(len(result)):
        #creates array with row-number of repeated pictures   
        correct=np.asarray(np.where(dataset[:,0]==result[i]))[0]
        lines[correct]=True
    Gray=np.where(dataset[:,1]=='Gray')[0]
    lines[Gray]=False
    Maroon=np.where(dataset[:,1]=='Maroon')[0]
    lines[Maroon]=False
    dataset=dataset[lines]
    Black=np.where(dataset[:,1]=='Black')[0]
    dataset[Black,1]='Brown'
    Hazel=np.where(dataset[:,1]=='Hazel')[0]
    dataset[Hazel,1]='Green'
    return dataset

#labels_utf8.csv
#'/Users/smilladue/Desktop/Documents/DTU/Intelligente_systemer/Projekt/front'
#correct_dataset("labels_utf8.csv",'/Users/smilladue/Desktop/Documents/DTU/Intelligente_systemer/Projekt/front')
