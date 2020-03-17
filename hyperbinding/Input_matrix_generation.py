#!/usr/bin/env python
# coding: utf-8

"""
================================
Convert a 12 mer peptide sequence into 5x12 imput matrix considering these properties: 'sequence','hydropathy','volume','polarity','length'
================================
Hyperbinding contains tools for analyzing the peptide sequence and predicting the binding afiinity with HLA-A02:01. The chemical properties of peptides have been reported to strongly affect the binding affinity. Since we consider that the order of the sequence, hydropathy index, volume, polarity and the length of the peptide could affect the binding affinity and the properties of these amino acids are key factors for their binding to MHC, we extracted these information from each peptide. 
"""



###############################################################################
# Create input matrix for CNN
# Add peptide sequence into the matrix
# -------------------


def create_input_matrix(data):
    '''
    Feature Order: 'sequence','hydropathy','volume','polarity','length'
    '''
    import pandas as pd
    import numpy as np
    input_matrix = []
    for i in data.iloc[:,0]:
        input_matrix.append(sequence_to_matrix(data['sequence'][i]))
    return input_matrix


###############################################################################
# Normalize the input matrx
# -------------------

def normalize_input_matrix(data):
    for i in range(data.shape[1]):
        data[0][i] = (data[0][i])/20*255
        data[1][i] = (data[1][i]+4.5)/9*255
        data[2][i] = (data[2][i])/227.8*255
        data[3][i] = (data[3][i])/4*255
        data[4][i] = (data[4][i]-8)/4*255
    return data


###############################################################################
# Expand each sequence into a 5x12 matrix, where five characters are peptide sequence, hydropathy, volume, polarity, length.
# -------------------

def sequence_to_matrix(sequence):
    import pandas as pd
    import numpy as np
    matrix = np.zeros((5,12))
    for i in range(len(sequence)):
        matrix[0,i] = sequence_to_num(sequence[i])
        matrix[1,i] = hydropathy(sequence[i])
        matrix[2,i] = volume(sequence[i])
        matrix[3,i] = polarity(sequence[i])
        matrix[4,i] = length(sequence)
    return matrix


###############################################################################
# Each amido acid will have a hydropathy index
# Reference for hydropathy index of each amino acids:
# http://www.imgt.org/IMGTeducation/Aide-memoire/_UK/aminoacids/abbreviation.html#refs
# -------------------


def hydropathy(letter):
    hydro = {
     'A': 1.8,
     'C': 2.5,
     'D': -3.5,
     'E': -3.5,
     'F': 2.8,
     'G': -0.4,
     'H': -3.2,
     'I': 4.5,
     'K': -3.9,
     'L': 3.8,
     'M': 1.9,
     'N': -3.5,
     'P': -1.6,
     'Q': -3.5,
     'R': -4.5,
     'S': -0.8,
     'T': -0.7,
     'V': 4.2,
     'W': -0.9,
     'Y': -1.3,
     'X': 0}
    return hydro.get(letter,"Invalid sequence")


###############################################################################
# Each amido acid will have a numeric index for CNN analyzing
# -------------------

def sequence_to_num(letter):
    num = {
     'A': 1,
     'C': 2,
     'D': 3,
     'E': 4,
     'F': 5,
     'G': 6,
     'H': 7,
     'I': 8,
     'K': 9,
     'L': 10,
     'M': 11,
     'N': 12,
     'P': 13,
     'Q': 14,
     'R': 15,
     'S': 16,
     'T': 17,
     'V': 18,
     'W': 19,
     'Y': 20,
     'X': 21  
    }
    return num.get(letter,"Invalid sequence")


###############################################################################
# Each amido acid will have a volume index
# Reference for volume index of each amino acids:
# http://www.imgt.org/IMGTeducation/Aide-memoire/_UK/aminoacids/abbreviation.html#refs
# -------------------

def volume(letter):
    vol = {
     'A': 88.6,
     'C': 108.5,
     'D': 111.1,
     'E': 138.4,
     'F': 189.9,
     'G': 60.1,
     'H': 153.2,
     'I': 166.7,
     'K': 168.6,
     'L': 166.7,
     'M': 162.9,
     'N': 114.1,
     'P': 112.7,
     'Q': 143.8,
     'R': 173.4,
     'S': 89.0,
     'T': 116.1,
     'V': 140.0,
     'W': 227.8,
     'Y': 193.6,
     'X': 0}
    return vol.get(letter,"Invalid sequence")


###############################################################################
# Each amido acid will have a polarity index
# Reference for polarity index of each amino acids:
# DOI: https://doi.org/10.3389/fgene.2019.01191
# -------------------



def polarity(letter):
    polar = {
     'A': 1,
     'C': 2,
     'D': 3,
     'E': 3,
     'F': 1,
     'G': 1,
     'H': 4,
     'I': 1,
     'K': 4,
     'L': 1,
     'M': 2,
     'N': 2,
     'P': 1,
     'Q': 2,
     'R': 4,
     'S': 2,
     'T': 2,
     'V': 1,
     'W': 2,
     'Y': 2,
     'X': 0}
    return polar.get(letter,"Invalid sequence")


###############################################################################
# Each peptide will have a length index
# ALthough we insert 'X' into every peptide to get uniform 12-mer sequences, the original peptide lenth is still important when considering binding affinity.
# -------------------

def length(sequence):
    length_sum = 12
    for i in range(len(sequence)):
        if sequence[i] == 'X' or sequence[i] == 'x':
            length_sum = length_sum - 1
    return length_sum

###############################################################################
# This file will convert a 12-mer peptide (with 'X' inserted) into a 5x12 matrix. 
# -------------------



