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
