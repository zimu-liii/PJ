# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:55:31 2022

@author: muzi
"""

from skimage.metrics import structural_similarity as ssim 
import numpy as np

def img_sim(img1,img2):
    
    if img1.shape != img2.shape:
        img2 = np.resize(img2,img1.shape)
        
    return ssim(img1,img2)
