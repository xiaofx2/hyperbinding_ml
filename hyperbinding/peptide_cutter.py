def cutter(sequence, length):
    frag = []
    for i in range(len(sequence)-length+1):
        piece = sequence[i:(i+length)]
        frag.append(piece)
    return frag