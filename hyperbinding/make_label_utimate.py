
"""
================================
Make_label_ultimate is used for selecting two datagroups with the
same size and label them by N/P 
================================
We have 12120 Rows of original data for training and testing.
Binding constant larger than 500nM are regarded as non-binding('N').
Binding constant smaller than 500nM are regarded as binding('P').
4475 with meas < 500 (positive)
7645 with meas > 500 (negative)
This file use random undersampling method to balance data.
We randomly choose 4475 rows from 7645 rows with negative peptides. 
The goal for this file is to get a balanced dataset: 
4475 positive and 4475 negative

Author: BOWEI ZHANG(1971135)
"""

def label_marker(file_name):
    import pandas as pd
    import numpy as np
    import random
    df = pd.read_csv(file_name)
    full_list = []
    binding_list = []
    # Get the full list of binders     
    for i in range(len(df)):
        full_list.append(i)
        if df.loc[i,'meas'] < 500:
            binding_list.append(i)
       
    # Get the full list of non-binders     
    rest_list = [x for x in full_list if x not in binding_list]
    non_binding_list = random.sample(rest_list, len(binding_list))
    label_list = binding_list+non_binding_list
    non_label_list = [x for x in full_list if x not in label_list]
    
    # Randomly drop extra rows for non-binders
    df_drop = df.drop(index=non_label_list)
    label_only = []
    df_drop = df_drop.reset_index()
    for i in range(len(df_drop)):
        if df_drop.loc[i,'meas'] < 500:
            label_only.append('P')
        else:
            label_only.append('N')
    # Generate a new file containing same number of binders and non-binders.
    df_drop['label'] = label_only
    df_drop.to_csv('Labeled-HLA-A-0201.csv')
