#!/usr/bin/python3


print(""""
########################################
#       Arturo Negreiros               #
#       Payload0911                    #
#                                      #
#                                      #
#                                      #
#                                      #
########################################
""")







from urllib.request import urlopen
import getopt
import sys
import os
from bs4 import BeautifulSoup



class Scrap:

    def __init__(self):
        self.args = sys.argv[1:]
        self.base = None

    def _usage(self):
        print("The tag -u or --url you must to include the url to scan <https://wherever.com>  ")


    def initializr(self):
        
        try:
            
            opt, args = getopt.getopt(self.args, "hu:",["help", "url="])
            #print(opt)

            for o,a in opt:

                if o in ('-u', '--url'):
                    
                    self.base = BeautifulSoup(urlopen(a), "html.parser")
                    print("[*]  ...captured url")
                    
                    print(self.base.find('a').get('value'))

                    print("[*]  ...Finished")

                if o in ('-h', '--help'):
                    self._usage()

        except getopt.error as e:
            print(str(e))






if __name__ == '__main__':

    scrap = Scrap()
    scrap.initializr()
