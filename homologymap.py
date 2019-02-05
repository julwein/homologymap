#!/usr/bin/env python3

import sys
import math
import numpy
import matplotlib.pyplot

def read_sequence(sequence_file): 
    return ''.join([line.strip() for line in sequence_file.readlines()]).lower()  #multiline; remove \n 

def make_chunk_set(chunk_sequence, chunk_len, fragment_len):
    return frozenset({chunk_sequence[i : (i+fragment_len)] for i    #{} - set generator. Nothing to do with dictionaries.
             in range(chunk_len - fragment_len + 1)})

def covariance(chunks, i, j):
    return math.pow(len(chunks[i].intersection(chunks[j])), 2) / (len(chunks[i]) * len(chunks[j]))

with open(sys.argv[1]) as sequence_file:
    sequence = read_sequence(sequence_file)

chunks = [] #each chunk is a set of fragments
chunk_len = 50000
fragment_len = 30
n = len(sequence) // chunk_len

for i in range(n):
    chunk_sequence = sequence[i*chunk_len : (i+1)*chunk_len]
    chunk_set = make_chunk_set(chunk_sequence, chunk_len, fragment_len)
    chunks.append(chunk_set)
    if i - (i//100)*100 == 99:
        print('chunk ', i, ' of ', n-1, ' done')

homology_map = numpy.zeros((n,n))

# for i in range(n):
    # homology_map[i,i] = 1


for i in range(n):
    for j in range(i+1, n):
        homology_map[i,j] = covariance(chunks,i,j)
    if i - (i//100)*100 == 99:
        print('covariance for line ', i, ' of ', n-1, ' done')

#print(homology_map)

matplotlib.pyplot.imshow(numpy.log(homology_map + 1), cmap='hot', interpolation='none')
matplotlib.pyplot.show()
