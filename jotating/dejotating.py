# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:32:10 2022

@author: muzi
"""

'''
	This module is the decoding process of jotating, 
	which returns a fragment of 5nt into a number (equal to the value of 9bit).
'''

def de_rotating(b0,b):
    
    #skipping of illegal errors to ensure the recovery of images
    if b0 == b:
        c = '0'
    
    if b0 == 'A':
        if b == 'C':
            c = '0'
        if b == 'G':
            c = '1'
        if b == 'T':
            c = '2'
    if b0 == 'C':
        if b == 'G':
            c = '0'
        if b == 'T':
            c = '1'
        if b == 'A':
            c = '2'
    if b0 == 'G':
        if b == 'T':
            c = '0'
        if b == 'A':
            c = '1'
        if b == 'C':
            c = '2'
    if b0 == 'T':
        if b == 'A':
            c = '0'
        if b == 'C':
            c = '1'
        if b == 'G':
            c = '2'
    return c

def dnatom5(seq):
    re_d = {'A':'0','C':'1','G':'2','T':'3'}
    s1 = re_d[seq[0]]
    s2 = de_rotating(seq[0],seq[1])
    s3 = re_d[seq[2]]
    s4 = re_d[seq[3]]
    s5 = de_rotating(seq[3],seq[4])
    return s1+s2+s3+s4+s5

def m5ton(s):
    return int(s[0])*144+int(s[1])*48+int(s[2])*12+int(s[3])*3+int(s[4])

def nto9(n):
    b = bin(n)[2:]
    while len(b) < 9:
        b = '0' + b
    return b

def main1(seq):
    return m5ton(dnatom5(seq))

def main2(seq):
    return nto9(m5ton(dnatom5(seq)))