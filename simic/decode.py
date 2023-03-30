# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:30:36 2022

@author: muzi
"""

'''
    This is the decoding module.
    
    Expecting input: a list of strs (DNA sequences)
    Expecting output: a 2D list (pixel matrix)
'''

from simic.jotating.dejotating import main as segment

'''Part1: Recover the order of sequences in the origin matrix.
          A single cell in the matrix contains a 90nt DNA 
          (removing adaptor and index from 141nt DNA)'''

#The adaptor-removing process is not necessary according to whether
#your sequencing results contains the adaptor part or not.
def remove_adaptor(seqlist141):
    dna = [i[20:-21] for i in seqlist141]
    return dna

#sort by the index
def index_parsing(seqlist100):
    dna = {}
    for i in seqlist100:
        index1 = segment(i[-10:-5])
        if index1 not in dna:
            dna[index1] = [i[:-10]+i[-5:]]
        if index1 in dna:
            dna[index1].append(i[:-10]+i[-5:])
    
    for j in dna:
        dna1 = {}
        for k in dna[j]:
            index2 = segment(k[-5:])
            dna1[index2] = k[:-5]   
        #fill the missing part to ensure the legality of the recovered matrix
        for n in range(max(dna1)+1):
            if n not in dna1:
                dna1[n] = 'ACAAC'*18
        dna[j] = dna1
    
    return dna

#dict to list
def to_list(dna):
    dna2 = sorted(dna.items(), key=lambda d: d[0])
    dna2list = [dna2[i][1] for i in range(len(dna2))]

    dnalist = []
    for j in dna2list:
        dna3 = sorted(j.items(), key=lambda d: d[0])
        dna3list = [dna3[k][1] for k in range(len(dna3))]
        dnalist.append(dna3list)

    return dnalist

#part main
def sort(seqlist100):
    dna2 = index_parsing(seqlist100)
    dnalist = to_list(dna2)
    return dnalist

def sort_with_adaptor(seqlist141):
    dna = remove_adaptor(seqlist141)
    dna2 = index_parsing(dna)
    dnalist = to_list(dna2)
    return dnalist

'''Part2: In-row operation, including
          spliting 90nt units into 5nt units
          turning 5nt units into 9bit units
          turning 9bit units into 8bit units'''

#90nt to 5nt
def to5(line):
    list30 = []
    for i in line:
        list30.append(i[0:30])
        list30.append(i[30:60])
        list30.append(i[60:90])
        
    list5 = []
    for i in list30:
        list5.append(i[0:5])
        list5.append(i[5:10])
        list5.append(i[10:15])
        list5.append(i[15:20])
        list5.append(i[20:25])
        list5.append(i[25:30])
    
    return list5

#5nt to 9bit: segment

#9bit to 8bit
def tobyte(bytelist9):
    
    listbit = []
    for i in bytelist9:
        b = bin(i)[2:]
        while len(b) < 9:
            b = '0' + b
        listbit.append(b)
    
    bit = ''
    for i in listbit:
        bit = bit + i 
    if bit[-1] == '0':
        if all([i == '0' for i in bit]):
            pass
        else:
            while bit[-1]=='0':
                bit = bit[:-1]
    elif bit[-1] == '1':
        if all([i == '1' for i in bit]):
            pass
        else:
            while bit[-1]=='1':
                bit = bit[:-1]
    while len(bit)%8!=0:
        bit = bit +'0'
    
    bitlist8 = []
    for i in range(0,len(bit),8):
        bitlist8.append(bit[i:i+8])
    
    bytelist = [int(i,2) for i in bitlist8]
    return bytelist

#part main
def line(dnalist):
    list5 = to5(dnalist)
    list9 = [segment(i) for i in list5]
    byteline = tobyte(list9)
    return byteline

'''Part3: Matrix operation: processing every row'''

def matrix(dnalist):
    bytelist = []
    for k in dnalist:
        bytelist.append(line(k))
    return bytelist

#check if list_decode is illegal
def matrix_check(bytelist):
    lenlist = []
    for i in bytelist:
        lenlist.append(len(i))
    lenmax = max(lenlist)
    for i in bytelist:
        while len(i) != lenmax:
            i.append(0)
    return

'''Main'''

def decode(seqlist100):
    dnalist = sort(seqlist100)
    bytelist = matrix(dnalist)
    matrix_check(bytelist)
    return bytelist

def decode_with_adaptor(seqlist141):
    seqlist100 = remove_adaptor(seqlist141)
    dnalist = sort(seqlist100)
    bytelist = matrix(dnalist)
    matrix_check(bytelist)
    return bytelist