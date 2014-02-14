#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Puzzles.py
#
#  This file serves as a demonstration which runs a batch of my 
#  solutions to various puzzles and problems organized into 
#  subdirectories.
#
#  TODO: user interface to select different problems, timed or untimed


import os, time

root_dir = '.'

def main():
    dirs = [d for d in os.walk(root_dir).next()[1] if not d[0] == '.']
    for d in dirs:
        path = os.path.join(root_dir, d)
        files = [f for f in os.walk(path).next()[2] if f[-3:] == '.py']
        files.sort(key=lambda f: int(filter(lambda c: c.isdigit(), f)))
        print '\nExecuting... %s/%s\n' % (d, ' '.join(files))
        for f in files:
            var = dict(locals(), **globals())
            start = time.time()
            execfile(os.path.join(path, f), var, var)
            print '(Solved in: %fs)\n' % (time.time() - start)

if __name__ == '__main__':
    main()
