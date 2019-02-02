#!/usr/bin/env python3

import sys

def make_chunk_set():
    

def covariance(i, j):
    

with open(sys.argv[1]) as sequence_file:
    sequence = sequence_file.read()

chunks = [] #every chunk is a set of fragments
chunk_len = 10000
fragment_len = 30
n = len(sequence) // chunk_len

for i in range(n):
    chunk_sequence = sequence[i*chunk_len : (i+1)*chunk_len]
    chunk_set = make_chunk_set(chunk_sequence)
    chunks.append(chunk_set)

#covariance(i, j)

for i in range(n):
    print(covariance(i, 0))
