# label_marker is used for selecting two datagroups with the
# same size and label them by N/P
# Author: BOWEI ZHANG(1971135)

def label_marker(file_name):
    import pandas as pd
    import numpy as np
    import random
    df = pd.read_csv(file_name)
    full_list = []
    binding_list = []
    for i in range(len(df)):
        full_list.append(i)
        if df.loc[i,'meas'] < 500:
            binding_list.append(i)
        
    rest_list = [x for x in full_list if x not in binding_list]
    non_binding_list = random.sample(rest_list, len(binding_list))
    label_list = binding_list+non_binding_list
    non_label_list = [x for x in full_list if x not in label_list]
    df_drop = df.drop(index=non_label_list)
    label_only = []
    df_drop = df_drop.reset_index()
    for i in range(len(df_drop)):
        if df_drop.loc[i,'meas'] < 500:
            label_only.append('P')
        else:
            label_only.append('N')
    df_drop['label'] = label_only
    df_drop.to_csv('Labeled-HLA-A-0201.csv')
