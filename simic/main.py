# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:51:40 2023

@author: muzi
"""

'''
    This is the main module defining SIMIC class.
    It assembles functions of encoding, decoding and some others.
    This module also gives the input processing part to ensure the correct execution of the program.
'''

import json
import matplotlib.pyplot as plt

from simic.encode import encode_no_adaptor,encode
from simic.decode import decode,decode_with_adaptor    

#StrandIndependentMatrixImageCoding
class SIMIC:
    
    #Img input is expected to be a 2D np array.
    #This fuction is to check if img is qualified.
    #If not, it will turn the img into a 2D format.
    def encode_input_check(self,img):
        if len(img.shape) !=2:
            img = img[:,:,0]
        return img
    
    #Input sequences is expected to be a list of strs, 
    #and every strs should be of the defaulted length, or the decoding process will go wrong.
    #This fuction is to check if every sequence in the sequence list is of qualified length.
    #If not, it will turn the length of every sequence qualified.
    def decode_input_check(self,sequences,adaptor=False):
        default_len = 100
        if adaptor==True:
            default_len = 141
        
        for i in range(len(sequences)):
            if len(sequences[i]) < default_len:
                sequences[i] = sequences[i] + (default_len-len(sequences[i]))*'A'
            if len(sequences[i]) > default_len:
                sequences[i] = sequences[i][:default_len]
        return sequences
     
    def encode(self,img,adaptor=False):
        img = self.encode_input_check(img)
        if adaptor==False:
            return encode_no_adaptor(img)
        if adaptor==True:
            return encode(img)
     
    def decode(self,sequences,adaptor=False):
        sequences = self.decode_input_check(sequences,adaptor)
        if adaptor==False:
            return decode(sequences)
        if adaptor==True:
            return decode_with_adaptor(sequences)
     
    #encode&decode function but receive input of a file
    def encode_file(self,file,adaptor=False):
        img = getdata(file,'encode')
        img = self.encode_input_check(img)
        if adaptor==False:
            return encode_no_adaptor(img)
        if adaptor==True:
            return encode(img)
      
    def decode_file(self,file,adaptor=False):
        sequences = getdata(file,'decode')
        sequences = self.decode_input_check(sequences,adaptor)
        if adaptor==False:
            return decode(sequences)
        if adaptor==True:
            return decode_with_adaptor(sequences)
     
    #show the decoded image
    def show(self,bytelist):
        plt.imshow(bytelist,cmap='gray')
        return
     
    #save the decoded image
    def save(self,bytelist,filename):
        plt.imsave(filename,bytelist,cmap='gray')
        return

#file-preprocessing: expecting option == 'encode' or 'decode'
def getdata(file_path,option):
        
    if option == 'encode':
        return plt.imread(file_path)
    
    if option == 'decode':
        if file_path[:-4] == 'json':
            with open(file_path,'r') as f:
                return json.load(f)
        if file_path[:-4] == '.txt':
            with open(file_path,'r') as f:
                return f.read().splitlines()
        else:
            raise Exception('Unsupported data format!')

    else:
        raise Exception('Illegal option: please choose encode or decode')
