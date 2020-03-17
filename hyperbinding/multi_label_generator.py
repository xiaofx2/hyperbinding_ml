"""
================================
Generate multi-label for the peptides to set binding affinity into five categories.
================================
Hyperbinding contains tools for analyzing the peptide sequence and predicting 
the binding afiinity with HLA-A02:01. 
"""



###############################################################################
# label 0: binding affinity <= 30 nM
# label 1: 30 nM < binding affinity <= 500 nM
# label 2: 500 nM < binding affinity <= 10000 nM
# label 3: 10000 nM < binding affinity <= 20000 nM
# label 4: 20000 nM < binding affinity 
# Add label information into the file to indicate the binding affinity
# -------------------


import pandas as pd


def multiple_lable_maker(data):
    label = []
    for i in range(len(data)):
        if data.loc[i,'meas']<=30:
            label.append(0)
        elif data.loc[i,'meas']>30 and data.loc[i,'meas']<=500:
            label.append(1)        
        elif data.loc[i,'meas']>500 and data.loc[i,'meas']<=10000:
            label.append(2)
        elif data.loc[i,'meas']>10000 and data.loc[i,'meas']<=20000:
            label.append(3)
        else:
            label.append(4)
    data['label'] = label
    data.to_csv('multi-Labeled-HLA-A-0201.csv')
