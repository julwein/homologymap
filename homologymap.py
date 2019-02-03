#!/usr/bin/env python3

import sys
import math

def read_sequence(sequence_file): 
    return ''.join([line.strip() for line in sequence_file.readlines()])  #multiline; remove \n 

def make_chunk_set(chunk_sequence, chunk_len, fragment_len):
    return {chunk_sequence[i : (i+fragment_len)] for i    #{} - set generator. Nothing to do with dictionaries.
             in range(chunk_len - fragment_len + 1)}

def covariance(chunks, i, j):
    return math.pow(len(chunks[i].intersection(chunks[j])), 2) / 
                (len(chunks[i]) * len(chunks[j]))

with open(sys.argv[1]) as sequence_file:
    sequence = read_sequence(sequence_file)

chunks = [] #each chunk is a set of fragments
chunk_len = 10000
fragment_len = 30
n = len(sequence) // chunk_len

for i in range(n):
    chunk_sequence = sequence[i*chunk_len : (i+1)*chunk_len]
    chunk_set = make_chunk_set(chunk_sequence, chunk_len, fragment_len)
    chunks.append(chunk_set)

for i in range(n):
    print(covariance(chunks, i, 0))
