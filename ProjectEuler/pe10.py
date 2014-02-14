#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pe10.py

problem = '10. Calculate the sum of all the primes below two million.'

def primes(n):
    """
    Utilizing the Sieve of Eratosthenes algorithm, which is a very quick
    method of getting a large sequence of prime numbers.
    """
    sieve = [True] * n
    for x in xrange(2, int(n**0.5) + 1):
        if sieve[x]:
            for i in xrange(x+x, n, x):
                sieve[i] = False
    return [p for p in xrange(2, n) if sieve[p]]

def solution(n=2000000):
    return sum(primes(n))

if __name__ == '__main__':
    print problem
    print solution() # 142913828922
