import numpy as np
import cv2 
import dlib
import glob
from eyeColor_hsv import eyeColor_hsv
import os


data = []

def batch_processing(img_path):
    for f in glob.glob(os.path.join(img_path, "*.jpg")):
        
        filename = os.path.basename(f)
        
        guess = eyeColor_hsv(f)
        
        data.append((filename,guess))
        
        
        
        
        
        
        
        
        
        