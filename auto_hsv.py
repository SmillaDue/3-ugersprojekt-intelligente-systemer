# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:28:05 2021

@author: rune7
"""
import numpy as np
import os
from auto import get_result


s = [-6,-3,-1,0,1,3,6]

#first 3 values are the lower bound for blue HSV values, the next 3 the upper bound, then likewise for the green range and finally brown
v = [105, 40, 40, 150, 255, 255, 6, 0, 50, 100, 55, 162, 0, 80, 0, 25, 255, 255]


            
def singleRun(path,v):
    i = -1
    for value in v:
        i = i+1
        score = []
        Q = []
        for step in s:
            if value+step>=0 and value+step<=255:
                q = value+step
            else:
                q = value
            v[i]=q    
            Q.append(q)
            
            score.append(get_result(path, v))
        
        best = np.where(np.array(score)==max(score))[0]
        if len(best)==1:
            v[i] = Q[best[0]]
        elif Q[best[0]] <= value:
            v[i] = Q[best[0]]
        elif Q[best[0]] > value:
            v[i] = Q[best[-1]]
    
        print(score)    
    return v


def multipleRuns(path,v,int):
    for runs in range(int):
        #looping over 10 minibatches of 500 randomly selected images before updating on the entire set
        #this imitates SGD, which speeds up the processes as well as potentially avoiding local minimums 
        v = singleRun(path+'/sub0',v)
        v = singleRun(path+'/sub1',v)
        v = singleRun(path+'/sub2',v)
        v = singleRun(path+'/sub3',v)
        v = singleRun(path+'/sub4',v)
        v = singleRun(path+'/sub5',v)
        v = singleRun(path+'/sub6',v)
        v = singleRun(path+'/sub7',v)
        v = singleRun(path+'/sub8',v)
        v = singleRun(path+'/sub9',v)
    for runs in range(int):
        v = singleRun(path,v)
    return v