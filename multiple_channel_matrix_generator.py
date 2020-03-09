import numpy as np

def multiple_channel_generator(sequence):
    mutiple_channel = np.zeros((3,21,12))
    mutiple_channel[0] = hydropathy_channel_generator(sequence)
    mutiple_channel[1] = vol_channel_generator(sequence)
    mutiple_channel[2] = polar_channel_generator(sequence)
    return mutiple_channel

def basic_matrix_generator(sequence):
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
    matrix = np.zeros((21,12))
    col = 0
    for letter in sequence:
        matrix[num[letter]-1][col] = 1
        col += 1
    return matrix

def hydropathy_channel_generator(sequence):
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
    basic_matrix = basic_matrix_generator(sequence)
    hydro_vector = list(hydro.values())
    hydro_matrix = basic_matrix.transpose() * hydro_vector
    hydro_matrix = hydro_matrix.transpose()
    return hydro_matrix

def vol_channel_generator(sequence):
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
    basic_matrix = basic_matrix_generator(sequence)
    vol_vector = list(vol.values())
    vol_matrix = basic_matrix.transpose() * vol_vector
    vol_matrix = vol_matrix.transpose()
    return vol_matrix

def polar_channel_generator(sequence):
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
    basic_matrix = basic_matrix_generator(sequence)
    polar_vector = list(polar.values())
    polar_matrix = basic_matrix.transpose() * polar_vector
    polar_matrix = polar_matrix.transpose()
    return polar_matrix
