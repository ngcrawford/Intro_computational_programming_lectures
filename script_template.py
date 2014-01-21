#!/usr/bin/env python
# encoding: utf-8


"""
[script name]..py
Created by [your name] on [date].

The author may be contacted at [your email]

[ It's traditional to write a bit about what the 
script does ]

# Licensing:

[ Note that for publication you have to make your code 
open source. There are a couple of open source licenses 
to choose from and http://choosealicense.com/ has a 
really nice break down of the standard options.]
"""

def get_args():
    """Parse sys.argv"""
    pass

def worker_fuction_1():
    """Doc string...."""
    pass

def work_fuction_2():
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
    main(args)

