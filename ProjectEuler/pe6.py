#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe6.py

problem = ('6. Find the difference between the sum of the squares of '
           'the first one hundred natural numbers and the square of '
           'the sum.')

def solution(n=100):
    """Returns difference between the sum of the squares of the first n
    natural numbers and the square of the sum"""
    return abs(sum(range(1, n+1))**2 - sum(x**2 for x in range(1, n+1)))

if __name__ == '__main__':
    print problem
    print solution() # 25164150
