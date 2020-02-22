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


# In[ ]:


np.array(dataframe['sequence'][1])


# In[ ]:


sequence_to_matrix(dataframe['sequence'][1])


# In[4]:


def hydropathy(letter):
    hydro = {
        'I': 4.5,
        'V': 4.2,
        'L': 3.8,
        'F': 2.8,
        'C': 2.5,
        'M': 1.9,
        'A': 1.8,
        'G': -0.4,
        'T': -0.7,
        'S': -0.8,
        'W': -0.9,
        'Y': -1.3,
        'P': -1.6,
        'H': -3.2,
        'E': -3.5,
        'Q': -3.5,
        'D': -3.5,
        'N': -3.5,
        'K': -3.9,
        'R': -4.5,
        'X': 0
    }
    return hydro.get(letter,"Invalid sequence")


# In[5]:


def sequence_to_num(letter):
    num = {
        'I': 8,
        'V': 18,
        'L': 10,
        'F': 5,
        'C': 2,
        'M': 11,
        'A': 1,
        'G': 6,
        'T': 17,
        'S': 16,
        'W': 19,
        'Y': 20,
        'P': 13,
        'H': 7,
        'E': 4,
        'Q': 14,
        'D': 3,
        'N': 12,
        'K': 9,
        'R': 15,
        'X': 0
    }
    return num.get(letter,"Invalid sequence")


# In[6]:


def volume(letter):
    vol = {
        'I': 166.7,
        'V': 140.0,
        'L': 166.7,
        'F': 189.9,
        'C': 108.5,
        'M': 162.9,
        'A': 88.6,
        'G': 60.1,
        'T': 116.1,
        'S': 89.0,
        'W': 227.8,
        'Y': 193.6,
        'P': 112.7,
        'H': 153.2,
        'E': 138.4,
        'Q': 143.8,
        'D': 111.1,
        'N': 114.1,
        'K': 168.6,
        'R': 173.4,
        'X': 0
    }
    return vol.get(letter,"Invalid sequence")


# In[7]:


def polarity(letter):
    polar = {
        'I': 1,
        'V': 1,
        'L': 1,
        'F': 1,
        'C': 2,
        'M': 2,
        'A': 1,
        'G': 1,
        'T': 2,
        'S': 2,
        'W': 2,
        'Y': 2,
        'P': 1,
        'H': 4,
        'E': 3,
        'Q': 2,
        'D': 3,
        'N': 2,
        'K': 4,
        'R': 4,
        'X': 0
    }
    return polar.get(letter,"Invalid sequence")


# In[8]:


def length(sequence):
    length_sum = 12
    for i in range(len(sequence)):
        if sequence[i] == 'X' or 'x':
            length_sum -= 1
    return length_sum


# In[ ]:




