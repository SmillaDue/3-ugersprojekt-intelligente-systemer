# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:00:01 2021

@author: rune7
"""

import numpy as np
import pandas as pd
from collections import Counter
import numpy as np
import glob
import os
import cv2


def open_data(filename):
    #filename="labels_utf8.csv"
    #Load the input file into a DataFrame 
    file=pd.read_csv(filename,sep=",",header=0)
    #Turn the DataFrame into a np.array matrix
    data=np.array(file)
    #creates dataset with only prisonername and eyecolor 
    dataset=np.array((data[:,0],data[:,5])).T
    
    #adds .jpg to prisonername, so that it is equal to filename
    for i in range(len(data[:,0])):
        dataset[i,0]=dataset[i,0]+".jpg"
        
    return dataset


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



def eyeColor_auto(path,v):
    
    v = v
    #filename=os.path.basename(path)
    
    img = cv2.imread(path)
    #converts pixels of rgb to csv
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    numbers=[]
    
    #counts number of pixels in the different ranges of colors and appends to empty list
    
    Blue=(v[0], v[1], v[2]), (v[3], v[4], v[5])
    numbers.append(np.count_nonzero(cv2.inRange(hsv, Blue[0], Blue[1])))
    
    Green=(v[6], v[7], v[8]), (v[9], v[10], v[11])
    numbers.append(np.count_nonzero(cv2.inRange(hsv, Green[0], Green[1])))
    
    Brown=(v[12], v[13], v[14]), (v[15], v[16], v[17])
    numbers.append(np.count_nonzero(cv2.inRange(hsv, Brown[0], Brown[1])))

    

    colors=(["Blue","Green","Brown"])
    #combines the count of pixels in a category to the category
    count=np.array((numbers,colors))
    
    #finds the biggest number of pixels that fits with a range of color
    maxi=str(max(numbers))
    
    #finds the category, which has most pixels that fits
    dominantColor=colors[np.where(count==maxi)[1][0]]
    
    return dominantColor



def batch_auto(img_path,v):
    data = []
    for f in glob.glob(os.path.join(img_path, "*jpg")):
        filename = os.path.basename(f)
        try:
            guess = eyeColor_auto(img_path+'/'+filename,v)
        except IndexError:
            pass
        data.append((filename,guess))
        
    return data
        
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


def get_result(img_path, v):
    file = 'labels_utf8.csv'
    data=batch_auto(img_path,v)
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
        if dataSorted[i,1]==datasetSorted[i,1]:
            value[i]=1
            
    #combines picturename and either 1 for same result or 0 for different result
    
    points=np.array((dataSorted[:,0],value)).T
    #counts numbers of same result
    correct=len(np.where(points=='1.0')[0])
    
    
    return correct


