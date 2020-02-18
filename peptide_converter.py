def peptide_converter(file_name):
    import pandas as pd
    df = pd.read_csv(file_name)
    for i in range(len(df)):
        ori_str = df.loc[i, 'sequence']
        index = int(len(df.loc[i, 'sequence'])/2)
        num_X = 12 - int(df.loc[i, 'peptide_length'])
        str_X = 'X'*num_X
        res_str = ori_str[:index] + str_X + ori_str[index:]
        df.loc[i, 'sequence'] = res_str
    df.to_csv('Filled-'+file_name)
