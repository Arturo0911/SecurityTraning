#!/usr/bin/python

import requests
from io import BytesIO
from lxml import etree


def main():
    url = 'https://nostarch.com'
    ress = requests.get(url)
    content = ress.content

    parser = etree.HTMLParser()
    content = etree.parse(BytesIO(content), parser=parser)

    for link in content.findall('\\a'):
        print(f"{link.get('href')} -> {link.text}")



if __name__ == "__main__":
    main()
