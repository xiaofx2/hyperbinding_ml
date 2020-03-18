"""
================================
For application purpose:
This file will take a protein sequence as input.
The protein sequence will be slice into short peptides with assigned lenth.
================================
T cells recognize fragments of protein antigens that have been partly degraded 
inside the antigen-presenting cell. The peptide fragments are then carried to 
the surface of the presenting cell on special molecules called MHC proteins, 
which present the fragments to T cells. For the Class I MHC, the binding groove 
is optimal for peptides with 8 to 12 amino acids. Using this tool, a long 
protein sequence can be sliced into short peptides for binding affinity prediction.
"""



###############################################################################
# The input is protein sequence and ideal length
# The output is a list of sliced peptides
# -------------------
def cutter(sequence, length):
    frag = []
    for i in range(len(sequence)-length+1):
        piece = sequence[i:(i+length)]
        frag.append(piece)
    return frag