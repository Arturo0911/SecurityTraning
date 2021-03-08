#!/usr/bin/python3

import getopt
import sys
import os
import socket

class Automation:

    def __init__(self):
        pass
    
    def presentation(self):
        print("***********************************************")
        print("***********************************************")
        print("***********************************************")
        print("***********************************************")
        print("***********************************************")
        print("***********************************************")

    def how_to_use(self):
        pass

    def initializr_arguments(self):
        try:
            arg = sys.argv[1:]
            opt, args = getopt.getopt(sys.argv[1:], 'd:s:i:v:r:hb',
                ['domain=', 'source=', 'info=', 'breach', 'verbose=', 'help', 'report='])
            print(opt)
            for o,a in opt:
                # print(opt)
                print(o)
                if o in ('-d', '--domain'):
                    print("domain is arturo.com")

                if o in ('-s', '--source'):
                    print("My home/directory")
                if o in ('-i', '--info'):
                    print("learning scripting")
                if o in ('-b', '--breach'):
                    print("breach")
                if o in ('-v', '--verbose'):
                    print("bla bla bla bla bla bla bla")
                if o in ('-h', '--help'):
                    print("see my blog about this one")
                if o in ('-r', '--report'):
                    print("reporting you")

        except getopt.GetoptError as e:
            print(e)
    
    

if __name__ == '__main__':

    automation = Automation()
    automation.initializr_arguments()

    
