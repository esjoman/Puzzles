#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe14.py

problem = ('14. Which starting number, under one million, produces the '
           'longest Collatz chain? Collatz sequence always gets to 1 by'
           ': n is even -> n/2, n is odd -> 3n + 1.')

def collatz(n, lookup={}):
    """
    Returns sequence of Collatz from starting number. Slower than just 
    getting the count, but getting the whole sequence is useful.
    """
    if n not in lookup:
        if n == 1:
            lookup[n] = [1]
        elif n % 2:
            lookup[n] = [n] + collatz(3*n + 1)
        else:
            lookup[n] = [n] + collatz(n/2) 
    return lookup[n]

def collatz_count(n, lookup={}):
    """
    Returns length of Collatz sequence. Faster and uses less memory than
    collatz().
    """
    if n not in lookup:
        if n == 1:
            lookup[n] = 1
        elif n % 2:
            lookup[n] = 1 + collatz_count(3*n + 1)
        else:
            lookup[n] = 1 + collatz_count(n/2)
    return lookup[n]

def solution(n=10**6):
    """
    Returns the starting number under n which produces the longest 
    Collatz chain
    """
    largest, starting_num = -1, -1
    for i in range(1, n):
        temp = collatz_count(i) # temp = len(collatz(i))
        if temp > largest:
            largest = temp
            starting_num = i
    return starting_num #, largest

if __name__ == '__main__':
    print problem
    print solution() # 837799
