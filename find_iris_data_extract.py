import dlib
import numpy as np
import cv2
from shape_to_np import shape_to_np
import os

def find_iris_data(image):
    
    
    #renaming functions that finds the face and finds specific parts of face
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    
    #loading image
    img = cv2.imread(image)
    
    #detects the face in image
    dets = detector(img, 0)
    
    #detects the different face features in image
    shape = predictor(img, dets[0])
    
    #converts shape to a numpy array
    shape=shape_to_np(shape, dtype="int")
    
    #finds the koordinates to the right eye
    eyes=shape[43:48]
    bool=np.array([ True,  True, False,  True,  True])
    
    #finds the koordinates to the right iris
    iris=eyes[bool]
    
    #creates a square with the imagedata of the iris
    (x, y, w, h) = cv2.boundingRect(np.array([iris]))
    irisdata = img[y:y + h, x:x + w]
    
    return irisdata
    
"""
#shows the iris
cv2.imshow('hej',irisdata)
cv2.waitKey()
cv2.destroyAllWindows()

"""
