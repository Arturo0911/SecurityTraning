#!/usr/bin/python3

import getopt
import sys
import os


class Automation:

    def __init__(self):
        pass




if __name__ == '__main__':

    automation = Automation()
    

    arg = sys.argv[1:]
    opt, args = getopt.getopt(arg, 'd:s:i:v:r:hb',
        ['domain=','source=','info=','breach','verbose=','help','report='])
    print(args)
