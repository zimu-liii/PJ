# -*- coding: utf-8 -*-
"""
Created on Thu May 22 16:36:12 2025

@author: muzi
"""

import matplotlib.pyplot as plt


'''Input'''

def read_image(img_path):
    
    img = plt.imread(img_path)
    
    if len(img.shape) !=2:
        img = img[:,:,0]
    
    return img

def read_seq(seq_path):
    
    with open(seq_path,'r') as f:
        seq_list = [i[:-1] for i in f.readlines()]
        
    return seq_list


'''Processing'''

def add_adaptor(seq_100_list):
    
    adaptor1 = 'ACACGACGCTCTTCCGATCT' #20nt
    adaptor2 = 'AGATCGGAAGAGCACACGTCT' #21nt
    
    seq_141_list = [adaptor1+i+adaptor2 for i in seq_100_list] 
    
    return seq_141_list

def remove_adaptor(seq_141_list):
    
    seq_100_list = [i[20:-21] for i in seq_141_list]
    
    return seq_100_list


'''Output'''

def show_image(img):
    
    plt.imshow(img,cmap='gray')
    
    return

def save_image(img,img_name):
    
    plt.save(img,img_name,cmap='gray')
    
    return

def save_sequence(seq,seq_name):
    
    with open(seq_name,'w') as f:
        f.writelines([i+'\n' for i in seq])
    
    return