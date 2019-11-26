# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:30:25 2019

@author: Gabriel Carvalho
"""
import time
import tensorflow as tf
import numpy as np
import cv2
import os

model = tf.keras.models.load_model("Conv Net MK39")



# Decides if target is landmark by running the conv net on each repository picture
# At first let's suppose that the robot is GreenRed and watches for the RedGreen
# In that case Is_landmark detects if landmark is RedGreen
def Is_landmark():
    real_data = []
    #CATEGORIES = ["GreenRed", "RedGreen"]
    REAL_DATADIR = "D:/Coisas/CANADA/Neural Networks Reasearch/Nova pasta/Landmark Recognition Conv Net MK39/MK39 Aplication/Conv Net MK39/Image_repository"
    IMG_SIZE = 64
    
    path = REAL_DATADIR
    
    for i in range(1,6):
        img_array = cv2.imread(os.path.join(path, str(i)+".JPG"))
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        real_data.append([new_array])

    X_real = []
    for features in real_data:
        X_real.append(features)
    
    X_real = np.array(X_real).reshape(-1, IMG_SIZE, IMG_SIZE, 3)

    X_real = X_real/255.
    
    
    model_out = model.predict([X_real])
    
    predictions = []
    
    for i in range(0,5):
        if(model_out[i][0] > 0.98):
            predictions.append(1)
        else:
            predictions.append(0)
            
        print(predictions[i])
    # Discarding the first and last pictures we reduce the chance of error       
    if ((predictions[1] == 1) 
        and (predictions[2] == 1)
        and (predictions[3] == 1)):
        # Landmark is RedGreen
        return True 
    else:
        # Not a landmark
        return False
        
# Activates LiDAR to measure distance between landmarks
#def measure_distance():
    
    
    

    
    
# Send the distance data back to computer 
#def send_distance_data(): 
        
    
    
    
        
# Main function
def main():
    while(1):
        for i in range(1,6):
            # take_picture()
            # receive_picture()
            
            cam = cv2.VideoCapture(1)    # Capture the picture
            ret, image = cam.read()      # read the image from the camera
            if ret:                      # If there's data from the camera process and save the image
                path = 'D:/Coisas/CANADA/Neural Networks Reasearch/Nova pasta/Landmark Recognition Conv Net MK39/MK39 Aplication/Conv Net MK39/Image_repository'
                #img_array = cv2.imread(os.path.join(path, str(i)+".JPG"), cv2.IMREAD_COLOR)
                #new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                cv2.imwrite(os.path.join(path, str(i)+".JPG"), image)
            
            #process_picture()
        if(Is_landmark()):
            # It's a landmark
            print("It's the RedGreen landmark!")
            #measure_distance()
            #send_distance_data()
        else:
            print("Not a landmark!")
        
        time.sleep(15)
        
        
        # delete_pictures()
        
        for i in range(1,6):
            os.remove('D:/Coisas/CANADA/Neural Networks Reasearch/Nova pasta/Landmark Recognition Conv Net MK39/MK39 Aplication/Conv Net MK39/Image_repository/'+str(i)+'.JPG')
        
        time.sleep(10)
        
main()    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    