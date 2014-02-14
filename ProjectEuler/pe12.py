#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe12.py

problem = ('12. What is the value of the first triangle number to have '
           'over five hundred divisors? The sequence of triangle '
           'numbers is generated by adding the natural numbers. So the '
           '7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28'
           '. The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, '
           '36, 45, 55, ...')

def factors(n):
    """returns set of factors"""
    return set(reduce(list.__add__, 
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def triangles():
    """Generates sequence of triangle numbers"""
    i, sum = 1, 0
    while True:
        sum += i
        yield sum
        i += 1

def solution(n=500):
    """Returns the first triangle number with over n divisors/factors"""
    for t in triangles():
        if len(factors(t)) > n:
            return t

if __name__ == '__main__':
    print problem
    print solution() # 76576500
