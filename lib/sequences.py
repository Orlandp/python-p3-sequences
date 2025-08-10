#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    if length == 1:
        print([0])
        return

    seq = [0, 1]
    for i in range(2, length):
        seq.append(seq[i - 1] + seq[i - 2])

    # Print the final sequence once
    print(seq)
