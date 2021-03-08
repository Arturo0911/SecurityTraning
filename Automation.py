#!/usr/bin/python3

import getopt
import sys
import os
import socket

"""
@author Arturo Negreiros 
@date 08/03/2021
"""



class Automation:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = None
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
            opt, args = getopt.getopt(sys.argv[1:], 'p:h:h',
                ['port=', 'host=', 'help',])
            #print(opt)
            for o,a in opt:
                # print(opt)
                #print(o)

                if o in ('-p', '--port'):
                    print(a)

                if o in ('-h', '--help'):
                    print(True)
        except getopt.GetoptError as e:
            print(e)
    
    

if __name__ == '__main__':

    automation = Automation()
    automation.initializr_arguments()

    
