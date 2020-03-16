def label_marker(file_name):
    import pandas as pd
    import numpy as np
    df = pd.read_csv(file_name, index_col=0)
    label_list = []
    for i in range(len(df)):
        if df.loc[i,'meas'] < 5:
            label_list.append('A')
        elif (df.loc[i,'meas'] < 50 and df.loc[i,'meas'] >= 5):
            label_list.append('B')
        else:
            label_list.append('C')
    df['label'] = label_list
    df.to_csv('Labeled-'+file_name)	
