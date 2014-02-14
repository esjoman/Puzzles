#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe7.py

problem = '7. Find the 10001st prime.'

def is_prime(n):
    """Checks if n is a prime number"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n=10001):
    """Returns the nth prime number"""
    if n < 1:
        return None
    i, p = 0, 0
    while p < n:
        i += 1
        if is_prime(i):
            p += 1
    return i

if __name__ == '__main__':
    print problem
    print solution() # 104743
