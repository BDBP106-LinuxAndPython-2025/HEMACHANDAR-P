#!/usr/bin/python3

# (1) Write a list comprehension to extract all even gene lengths from a list of genes. For
# example, gene_lengths=[450,300,725,1024,512,815].

gene_length=[450,300,725,1024,512,815]

# for i in range(gene_length):
#     if i % 2 == 0:
#         print(i)

a=[i for i in gene_length if i % 2 == 0]
print(a)

