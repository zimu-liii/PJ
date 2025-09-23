# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:42:05 2022

@author: muzi
"""

import random

def pollute(seqlist,a1,a2): 
    #a1: choose how much (the percentage) of DNA strands to be polluted
    #a2: choose the error rate in a single strand
    
    def func1(a1):
        b1 = random.random()
        if b1 < a1:
            return True
        else:
            return False
        
    def func2(a2):
        b2 = random.random()
        if b2 < a2:
            return random.choice('AGCT')
        else:
            return ''
    
    def pollute_singlebase(base,a2):
        error = func2(a2)
        while error==base:
            error = func2(a2)
        if error=='':
            return base
        else:
            return error
    
    polluted_seqlist = []
    for i in seqlist:
        if_pollute = func1(a1)
        if if_pollute==True:
            polluted_seq = ''
            for j in i:
                polluted_seq = polluted_seq + pollute_singlebase(j,a2)
            polluted_seqlist.append(polluted_seq)
        if if_pollute==False:
            polluted_seqlist.append(i)
            
    return polluted_seqlist
