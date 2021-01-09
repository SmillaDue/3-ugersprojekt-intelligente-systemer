# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:08:37 2021

@author: rune7
"""

import os
import glob
import shutil
from open_data import open_data


#HUSK: source skal indeholde filnavn, men destination skal bare være mappen

def copyFile(src, dest):
    try:
        shutil.copy(src,dest)
    except shutil.Error:
        print('Error1')
    except IOError:
        print('Error2')

        


def listFiles(imagefolder):
    #takes as input path to folder e.g. 'C:/Users/rune7/Documents/AI/Test/Green'
    files = os.listdir(imagefolder)
    return files
    

def sort_dataset(data,imagefolder,dest,eyecolor):
    #takes as input the name of csv data file stored in cwd as well as path to folder with files
    data = open_data(data)
    files = listFiles(imagefolder)
    
    for file in files:
        for i in range(len(data)):
            #copies the file if filename is found in data and it corresponds to the targeted eyecolor
            if data[i,0] == file and data[i,1] == eyecolor: 
                copyFile(imagefolder+'/'+file,dest)
                


                
  