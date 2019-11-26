# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:39:56 2019

@author: Gabriel Carvalho
"""
import cv2
import os
import time
import matplotlib.pyplot as plt

'''
cam = cv2.VideoCapture(0)

img = cam.read()

#cv2.namedWindow("camera")
#cv2.imshow("camera", img)
cv2.imshow(img)
cv2.waitKey(0)
cv2.destroyWindow("camera")

'''
#cam = cv2.VideoCapture(0)
    
#ret, image = cam.read()
    
#if ret:
    #cv2.imshow("snapshotTest", image)
    #cv2.waitKey(0)
    #path = 'D:/Coisas/CANADA/Neural Networks Reasearch/Nova pasta/Landmark Recognition Conv Net MK39/MK39 Aplication/Conv Net MK39/Image_repository'
    #cv2.imwrite(os.path.join(path, "snapshotTest.JPG"), image)
    
for i in range(1,4):
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()
    if ret:
        path = 'D:/Coisas/CANADA/Neural Networks Reasearch/Nova pasta/Landmark Recognition Conv Net MK39/MK39 Aplication/Conv Net MK39/Image_repository'
        cv2.imwrite(os.path.join(path, str(i)+".JPG"), image)


    '''
    for i in range(1,4):
        IMG_SIZE = 64
        path = 'D:/Coisas/CANADA/Neural Networks Reasearch/Nova pasta/Landmark Recognition Conv Net MK39/MK39 Aplication/Conv Net MK39/Image_repository'
        cam = cv2.VideoCapture(0)
        ret, image = cam.read()
        if ret:
            img_array = cv2.imread(os.path.join(path, str(i)+".JPG"), cv2.IMREAD_COLOR)
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            cv2.imwrite(os.path.join(path, str(i)+".JPG"), new_array)
        #plt.imshow(new_array, cmap = 'gray')
        #plt.show()
        #cv2.imshow("Image"+str(i),new_array)
        #cv2.waitKey(0)
    '''
    
    '''
    for i in range(1,4):
        os.remove('D:/Coisas/CANADA/Neural Networks Reasearch/Nova pasta/Landmark Recognition Conv Net MK39/MK39 Aplication/Conv Net MK39/Image_repository/'+str(i)+'.JPG')
        
        
#cv2.destroyWindow("snapshotTest")
        '''
    
