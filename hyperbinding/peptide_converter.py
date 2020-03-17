"""
================================
This file will convert 8-12 mer peptides to uniform 12 mer peptides by 
inserting 'X' in the middle.
================================
For Class I MHC, the binding groove is optimal for peptides with 8 to 12 amino acids. 
Peptides presented by a Class I MHC molecule generally assume a central bulged 
conformation. Based on this theory, we proposed a novel method that can convert the 
8–12 mer peptide to uniform size of 12mer. Since the peptide residues on both sides
are much more important than the other locations, we try to ensure that the new 
‘amino acid’ (X) is only inserted into the middle position of the peptide. 
"""



###############################################################################
# Create new peptide sequence with 'X' in the middle
# All peptides will be converted to 12 mer.
# -------------------



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
