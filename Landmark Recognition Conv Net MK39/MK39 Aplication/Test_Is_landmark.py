# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:00:35 2019

@author: Gabriel Carvalho
"""

def Is_landmark():
    real_data = []
    #CATEGORIES = ["GreenRed", "RedGreen"]
    REAL_DATADIR = "D:/Coisas/CANADA/Neural Networks Reasearch/Nova pasta/Landmark Recognition Conv Net MK39/MK39 Aplication/Conv Net MK39/Image_repository"
    IMG_SIZE = 64
    
    path = REAL_DATADIR
    
    for i in range(1,4):
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
    
    for i in range(0,3):
        if(model_out[i][0] > 0.7):
            predictions.append(1)
        else:
            predictions.append(0)
            
    if (predictions[0] == 1 and predictions[1] == 1 and predictions[2] == 1):
        # Landmark is RedGreen
        return True 
    else:
        # Not a landmark
        return False
    
Is_landmark()