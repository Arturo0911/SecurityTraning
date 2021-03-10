#!/usr/bin/python3

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
        self.data_parsed = None
        self.emails = list()

    def _usage(self):
        print("The tag -u or --url you must to include the url to scan <https://wherever.com>  ")

    def find_into_url(self, url):
        
        """
            Methods
            findAll(tag, attributes, recursive, text, limit, keywords)
            find(tag, attributes, recursive, text, keywords)
        """

        with urlopen(url) as f:

            self.base = BeautifulSoup(f,"html.parser")
            #print(self.base.findAll('a'))
            self.data_parsed = self.base.findAll('span')
            if self.data_parsed is None:
                return None
            else:
                for x in self.data_parsed:
                    print(x.get_text())


    def initializr(self):
        
        try:
            
            opt, args = getopt.getopt(self.args, "hu:",["help", "url="])
            #print(opt)

            for o,a in opt:

                if o in ('-u', '--url'):
                    
                    if self.find_into_url(a) is None:
                        print("Data cannot be founded")
                    else:
                        self.find_into_url(a)
                        print("[*]  ...Finished")

                if o in ('-h', '--help'):
                    self._usage()

        except getopt.error as e:
            print(str(e))






if __name__ == '__main__':

    scrap = Scrap()
    scrap.initializr()
