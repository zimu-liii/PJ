# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:51:40 2023

@author: muzi
"""

'''
    This is the main module defining SIMIC class.
    It assembles functions of encoding, decoding and some others.
'''


from encode import encode
from decode import decode

#StrandIndependentMatrixImageCoding
class PJ:
     
    def encode(self,img):
        return encode(img)
     
    def decode(self,sequences):
        return decode(sequences)
    
        return
