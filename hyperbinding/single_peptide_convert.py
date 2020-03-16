def peptide_converter(sequence):
    index = int(len(sequence)/2)
    num_X = 12 - int(len(sequence))
    str_X = 'X'*num_X
    res_str = sequence[:index] + str_X + sequence[index:]
    return res_str
