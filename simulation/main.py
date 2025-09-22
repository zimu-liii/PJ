# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 09:39:10 2023

@author: muzi
"""

import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir('..')
from pj import PJ
from simulation.error.pollute import pollute
from simulation.error.missing import missing
from simulation.similarity import similarity

class SIMU(PJ):
    
    img_default = plt.imread('input/R-C.tif')
    
    def __init__(self, img=img_default):
        self.img = img
        self.seq = super().encode(self.img)
        
    def error_pollute(self, a1, a2):
        error_seq = pollute(self.seq, a1, a2)
        return super().decode(remove_adaptor(error_seq))

    def error_miss(self, a):
        error_seq = missing(self.seq, a)
        return super().decode(remove_adaptor(error_seq))
    
    def similarity(self, list_byte):
        error_img = np.array(list_byte)
        return similarity.img_sim(self.img, error_img)
    
def remove_adaptor(sequences):
    sequences_no_adaptor = [i[20:-21] for i in sequences]
    return sequences_no_adaptor
