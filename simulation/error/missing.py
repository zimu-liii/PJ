# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 09:30:05 2022

@author: muzi
"""

import random

def missing(seqlist,a):
    
    #a: hoose how much (the percentage) of DNA strands to be missed
    def func(a):
        b = random.random()
        if b < a:
            return True
        else:
            return False
        
    seqlist_missing = []
    for i in seqlist:
        if_miss = func(a)
        if if_miss == True:
            continue
        if if_miss == False:
            seqlist_missing.append(i)
    
    return seqlist_missing
