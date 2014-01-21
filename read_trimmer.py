#!/usr/bin/env python
# encoding: utf-8

"""
read_trimmer.py
Created by Nick Crawford on 1/14/14.

The author may be contacted at ngcrawford@gmail.com

[ It's traditional to write a bit about what the 
script does ]

# Licensing:

[ Note that for publication you have to make your code 
open source. There are a couple of open source licenses 
to choose from and http://choosealicense.com/ has a 
really nice break down of the standard options.]
"""

import sys
import argparse

def get_args():
    """Parse sys.argv"""

    # INITIATE PARSER
    parser = argparse.ArgumentParser()

    # ADD COMMANDLINE ARGUMENTS
    parser.add_argument('-S','--start',
                        required=False,
                        type=int,
                        help='Trim X number of base from \
                              the start of each read')

    parser.add_argument('INPUT',
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        nargs='?',
                        help='Input fastq file.')

    parser.add_argument('OUTPUT',
                        type=argparse.FileType('w'),
                        default=sys.stdout,
                        nargs='?',
                        help='Output trimmed fastq file.')

    # PROCESS ARGUMENTS
    args = parser.parse_args()
    return args 


def worker_function_1():
    """Doc string...."""
    pass

def work_function_2():
    """Doc string...."""
    pass

# etc...

def main(args):
    """Main function.

    This code should be concise - typically a single loop that
    calls worker_fuctions that do most of the computation."""
    pass


if __name__ == '__main__':
    
    """This statement allows you have code in your program
    that is only executed if it is run as a command-line script.

    Explanation here:
    http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    """
    
    args = get_args()
    print args.start
    print args.INPUT
    main(args)

