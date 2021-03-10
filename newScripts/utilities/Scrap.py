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
from urllib.error import HTTPError
import getopt
import sys
import os
from bs4 import BeautifulSoup


class Scrap:

    def __init__(self):
        self.args = sys.argv[1:]
        self.base = None
        self.dataParsed = None

    def _usage(self):
        print("The tag -u or --url you must to include the url to scan <https://wherever.com>  ")

    
    def find_into_url(self, url):

        with urlopen(url) as f:

            self.base = BeautifulSout(f,"html.parser")



    def initializr(self):
        
        try:
            
            opt, args = getopt.getopt(self.args, "hu:",["help", "url="])
            #print(opt)

            for o,a in opt:

                if o in ('-u', '--url'):
                    
                    html = urlopen(a)
                    base = BeautifulSoup(html, "html.parser")
                    print("[*]  ...captured url")
                    data = base.findAll('a')
                    #print(base.find('a'))
                    if data is None:
                        print("Data cannot be founded")
                    else:
                        print(data)
                        print("[*]  ...Finished")

                if o in ('-h', '--help'):
                    self._usage()

        except getopt.error as e:
            print(str(e))






if __name__ == '__main__':

    scrap = Scrap()
    scrap.initializr()
