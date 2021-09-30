#!/usr/bin/python

import requests
from pprint import pprint
user = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
url = "http://natas5.natas.labs.overthewire.org/"



def main():
    s = requests.Session()
    s.auth = ("natas5", "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq")
    r = s.get(url="http://natas5.natas.labs.overthewire.org/")
    print(r.headers)


if __name__ == "__maim__":
    main()
