import numpy as np
import cv2 
import dlib
import glob
from eyeColor_hsv import eyeColor_hsv
import os


def batch_processing(img_path):
    data = []
    for f in glob.glob(os.path.join(img_path, "*")):
        filename = os.path.basename(f)
        try:
            guess = eyeColor_hsv(f)
        except IndexError:
            pass
        data.append((filename,guess))
        
    return data
        
        
        
        
        
        
        
        
        
        
