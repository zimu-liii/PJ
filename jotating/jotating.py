# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 10:08:07 2022

@author: muzi
"""

'''
	This module is the jotationg (jump-rotating) algorithm, 
	which is modified from the rotating algorithm 
	and is aimed to obtain qualified DNA sequences with less restrictions.
	
	It would turn a 9bit information unit into a 5nt DNA unit.
'''

import math

#9bits to 5mixed
def hro_9to5(s):
    
    if len(s) < 9:
        while len(s)<9:
            s = s + '0'
    
    num = int(s,2)
    a1=math.floor(num/144)
    a2=math.floor((num-144*a1)/48)
    a3=math.floor((num-144*a1-48*a2)/12)
    a4=math.floor((num-144*a1-48*a2-12*a3)/3)
    a5=num-144*a1-48*a2-12*a3-3*a4
    s5 = str(a1)+str(a2)+str(a3)+str(a4)+str(a5)
    return s5

#single-base rotating
def s_rotating(b0,c):
    if b0 == 'A':
        if c == '0':
            b = 'C'
        if c == '1':
            b = 'G'
        if c == '2':
            b = 'T'
    if b0 == 'C':
        if c == '0':
            b = 'G'
        if c == '1':
            b = 'T'
        if c == '2':
            b = 'A'
    if b0 == 'G':
        if c == '0':
            b = 'T'
        if c == '1':
            b = 'A'
        if c == '2':
            b = 'C'
    if b0 == 'T':
        if c == '0':
            b = 'A'
        if c == '1':
            b = 'C'
        if c == '2':
            b = 'G'
    return b

#5mixed to 5nt
def m5todna(s5):
    d = {'0':'A','1':'C','2':'G','3':'T'}
    s1 = d[s5[0]]
    s2 = s_rotating(s1,s5[1])
    s3 = d[s5[2]]
    s4 = d[s5[3]]
    s5 = s_rotating(s4,s5[4])
    seq = s1+s2+s3+s4+s5
    return seq

def main(s):
    s5 = hro_9to5(s)
    seq = m5todna(s5)
    return seq