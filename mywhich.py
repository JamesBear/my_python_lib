#!/usr/bin/python
# coding: utf-8


#Originally written in python 2.7
# 20141210
# author: James Bear

import os
#import shutil
import sys

intro = 'This is an alternative of POSIX.which'
usage = 'Usage: mywhich PROGRAM_NAME'

def debug(item):
    #print(item)
    pass

if len(sys.argv) < 2:
    print(usage)
    exit(0)

if sys.argv[1] == '--help' or sys.argv[1] == '-h':
    print(intro)
    print(usage)
    exit(0)


def find(paths, program_name):
    for p in paths:
        if os.path.isdir(p):
            if p.endswith(os.sep):
                fpath = p + program_name
            else:
                fpath = p + os.sep + program_name
            if (os.path.isfile(fpath)):
                return fpath
    return None

path = os.popen('echo "$PATH"', 'r').read()
debug(path)
debug(path.split(':'))
debug(sys.argv)
paths = path.split(':')
program_path = find(paths, sys.argv[1])
if program_path != None:
    print (program_path)
