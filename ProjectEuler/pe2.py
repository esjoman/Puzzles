#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe2.py

problem = ('2. By considering the terms in the Fibonacci sequence '
           'whose values do not exceed four million, find the sum of '
           'the even-valued terms.')

def fib_to(n):
    """Generates Fibonacci sequence up to n"""
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a + b

def solution(n=4000000):
    """Returns sum of even-valued Fibonnaci terms that don't exceed n"""
    return sum(x for x in fib_to(n) if x % 2 == 0)

if __name__ == '__main__':
    print problem
    print solution() # 4613732
