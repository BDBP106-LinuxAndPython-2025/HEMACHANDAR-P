#!/usr/bin/python3

#(9) A DNA sequence encodes each amino acid making up a protein as a three-nucleotide
#sequence called a codon. For example, the sequence fragment AGTCTTATATCT contains
# the codons AGT, CTT, ATA, TCT if read from the first position. If read from
#the second position, it yields the codons GTC, TTA, TAT and if read from the third
#position we get TCT, TAT, ATC. Write a function to extract the codons into a list of
#3-letter strings given a sequence and from what position (input as an integer) the sequence
#should be read. As an example, output the 3-letter strings from the sequence
#GTTTCGATTATAACG read from the (i) 1st position and (ii) 3rd position.


def extract_codons(sequence, frame):
#sequence : DNA string (e.g. 'GTTTCGATTATAACG')
#frame    : 1, 2, or 3 (reading frame)
    codons = []
    start = frame - 1   # convert frame to 0-based index
    for i in range(start, len(sequence), 3):
        codon = sequence[i:i+3]
        #print("Codon:", codon)
        if len(codon) == 3:   # only complete codons
            codons.append(codon)
    return codons


# Example usage
seq = "GTTTCGATTATAACG"

print("Reading frame 1:", extract_codons(seq, 1))
print("Reading frame 2:", extract_codons(seq, 2))
print("Reading frame 3:", extract_codons(seq, 3))
print("Reading frame 4:", extract_codons(seq, 4))
print("Reading frame 5:", extract_codons(seq, 5))
print("Reading frame 6:", extract_codons(seq, 6))
print("Reading frame 7:", extract_codons(seq, 7))
print("Reading frame 8:", extract_codons(seq, 8))
print("Reading frame 9:", extract_codons(seq, 9))
print("Reading frame 10:", extract_codons(seq, 10))
print("Reading frame 11:", extract_codons(seq, 11))
print("Reading frame 12:", extract_codons(seq, 12))



