# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 09:16:43 2022

@author: muzi
"""

'''
    This is the encoding module.
    
    Expecting input: a 2D np.array (which normally comes from a grayscale image opened by matplotlib)
                     or a 2D list
    Expecting output: a 1D list of strs (DNA sequences)
    
'''

from simic.jotating.jotating import main as segment

'''Step1: Regroup 8bit units into 9bit units'''

#part main
def regroup(img):
    bitlist = []
    for i in img:
        
        bits = ''
        for j in i:
            bit = bin(j)[2:]
            while len(bit) < 8:
                bit = '0' + bit
            bits = bits + bit
        if len(bits)%162 != 0:
            if bits[-1] == '1':
                while len(bits)%162 != 0:
                    bits = bits + '0'
            elif bits[-1] == '0':
                while len(bits)%162 != 0:
                    bits = bits + '1'
        
        bitl = [bits[i:i+9] for i in range(0,len(bits),9)]
        
        bitlist.append(bitl)
    return bitlist

'''Step2: Build 141nt DNA strands by merging 18×5nts, indexes and adaptors
       or build 100nt DNA strands by merging 18×5nts and indexes (no adaptors)''' 

#18×5nt=90nt
def merge_nt(seqlist5):
    
    seqlist30 = []
    for i in range(0,len(seqlist5),6):
        seqlist30.append(seqlist5[i]+seqlist5[i+1]+seqlist5[i+2]+seqlist5[i+3]+seqlist5[i+4]+seqlist5[i+5])
    
    seqlist90 = []
    for i in range(0,len(seqlist30),3):
        seqlist90.append(seqlist30[i]+seqlist30[i+1]+seqlist30[i+2])
    
    return seqlist90

#add index
def add_index(seqlist90,row):
    
    ##Index is composed of both row index and column index
    def index(i,j):
        
            i2 = bin(i)[2:]
            while len(i2) < 9:
                i2 = '0' + i2
            ri2 = segment(i2)
            
            j2 = bin(j)[2:]
            while len(j2) < 9:
                j2 = '0' + j2
            rj2 = segment(j2)
            
            return ri2+rj2
    
    seqlist100 = []
    for i in range(len(seqlist90)):
        seqlist100.append(seqlist90[i]+index(row,i))
  
    return seqlist100

#add adaptor
def add_adaptor(seqlist105):
    
    adaptor1 = 'ACACGACGCTCTTCCGATCT' #20nt
    adaptor2 = 'AGATCGGAAGAGCACACGTCT' #21nt
    
    seqlist141 = [adaptor1+i+adaptor2 for i in seqlist105] 
    return seqlist141

#part main
def merge_no_adaptor(seqlist5,row):
    seqlist90 = merge_nt(seqlist5)
    seqlist100 = add_index(seqlist90,row)
    return seqlist100

def merge(seqlist5,row):
    seqlist90 = merge_nt(seqlist5)
    seqlist100 = add_index(seqlist90,row)
    seqlist141 = add_adaptor(seqlist100)
    return seqlist141

'''Main function'''

def encode_no_adaptor(img):
    
    bitlist = regroup(img)
    
    ntlist = []
    for i in bitlist:
        ntlist.append([segment(j) for j in i])
    
    seqlist_whole = []
    for i in range(len(ntlist)):
        seqlist141 = merge_no_adaptor(ntlist[i],i)
        for j in seqlist141:
            seqlist_whole.append(j)
    
    return seqlist_whole

def encode(img):
    
    bitlist = regroup(img)
    
    ntlist = []
    for i in bitlist:
        ntlist.append([segment(j) for j in i])
    
    seqlist_whole = []
    for i in range(len(ntlist)):
        seqlist141 = merge(ntlist[i],i)
        for j in seqlist141:
            seqlist_whole.append(j)
    
    return seqlist_whole