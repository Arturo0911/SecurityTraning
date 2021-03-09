#!/usr/bin/python3
from locale import getdefaultlocale
import os
from subprocess import call






language, encoding = getdefaultlocale()


print(language)


def initialize(value, **values):

    print(values)



initialize("arturo", last_name= "apellido", eded= 25)
