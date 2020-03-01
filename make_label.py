def label_marker(file_name):
    import pandas as pd
    import numpy as np
    import random
    df = pd.read_csv(file_name, index_col=0)
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
    
    label_list = []
    for i in range(len(df)):
        if df.loc[i,'meas'] < 500:
            label_list.append('P')
        else:
            label_list.append('N')
    df['label'] = label_list
    df.to_csv('Labeled-Filled-HLA-A_0201.csv')
