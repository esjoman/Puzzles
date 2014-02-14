#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe9.py

problem = ('9. There exists exactly one Pythagorean triplet '
           '(a^2 + b^2 = c^2) for which a+b+c=1000. Find the '
           'product abc.')

def find_pyth(n):
    """Finds Pythagorean triplet for a+b+c=n if it exists, else None"""
    for a in range(n//2):
        for b in range(a, n//2):
            c = (a**2 + b**2) ** 0.5
            if a + b + c == n:
                return (a, b, int(c))
    return None

def solution(n=1000):
    """Returns product of Pythagorean triplet for a+b+c=n"""
    return reduce(lambda x,y: x*y, find_pyth(n))

if __name__ == '__main__':
    print problem
    print solution() # 31875000 (200, 375, 425)
