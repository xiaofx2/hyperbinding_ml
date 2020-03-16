#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[2]:


def normalize_input_matrix(data):
    for i in range(data.shape[1]):
        data[0][i] = (data[0][i])/20*255
        data[1][i] = (data[1][i]+4.5)/9*255
        data[2][i] = (data[2][i])/227.8*255
        data[3][i] = (data[3][i])/4*255
        data[4][i] = (data[4][i]-8)/4*255
    return data

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




# In[4]:


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


# In[5]:


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


# In[6]:


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


# In[7]:


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


# In[8]:


def length(sequence):
    length_sum = 12
    for i in range(len(sequence)):
        if sequence[i] == 'X' or sequence[i] == 'x':
            length_sum = length_sum - 1
    return length_sum


# In[ ]:




