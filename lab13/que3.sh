#!/bin/bash

gawk '!/^>/' fasta.txt

sed 's/T/U/g' fasta.txt

sed 's/seq1/human_gene/g' fasta.txt


