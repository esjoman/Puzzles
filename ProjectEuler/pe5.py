#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe5.py

problem = ('5. What is the smallest number divisible by each of the '
           'numbers 1 to 20?')

def gcd(a, b):
    """Returns greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Returns lowest common multiple."""
    return a * b // gcd(a, b)

def solution(n=20):
    """Returns the lcm of numbers 1 through n"""
    return reduce(lcm, range(1, n+1))

if __name__ == '__main__':
    print problem
    print solution() # 232792560
