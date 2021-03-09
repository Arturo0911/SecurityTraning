#!/usr/bin/python3

import os
import sys
import shutil
import time
import threading
import webbrowser






class Browser(object):

    def __init__(self):
        pass





class Malware(object):

    def __init__(self):
                
        self.path_name = os.environ['HOME']
        self.user_name = os.environ['USER']
        self.directory_name = 'malware_dir'
        self.steps = 'instructions.txt'
        self.instructions = """Not worry, you already infected by my first trojan.\n 
        The only thing that you must to do is follow the instructions:\n
        1) Not call a police :)\n
        2) Go out for a beer.\n
        3) wait for my instructions.
        """
        self.root_directory = '/'
        self.root_name_file_storage = 'list_root.txt'
        # this instructions is to read store list about root path


    def initialize(self):
        
        if os.path.isdir(self.path_name+'/Escritorio/'+self.directory_name):

            print("[*] Deleting current directoy %s"%self.directory_name)
            shutil.rmtree(self.path_name+'/Escritorio/'+self.directory_name)
            print("[*] Creating a new directory.")
            os.mkdir(self.path_name+'/Escritorio/'+self.directory_name)

            time.sleep(0.5)

            print ("[*] Directory was created successfully.")
            return 
        
        else:

            print("[*] creating directory.")
            os.mkdir(self.path_name+'/Escritorio/'+self.directory_name)
            
            time.sleep(0.5)
            
            print("[*] Directory was created successfully")
            return
        
        return None

    def create_instructions(self):
        
        with open(self.path_name+'/Escritorio/'+self.directory_name+'/'+self.steps, 'w') as f:
            f.write(self.instructions)
            f.close()

        return

    def store_directories(self):

        #self.store_dir = str(os.listdir(self.root_directory))
        

        self.value = os.listdir(self.root_directory)
        #for i in self.value:
            #print(i)

        with open(self.path_name+'/Escritorio/'+self.directory_name+'/'+self.root_name_file_storage, 'w') as f:
            #for x in self.store_dir:
            #f.write(self.store_dir)

            for j in self.value:
                f.write(j+'\n')
                #f.write("\n")
            f.close()

        return None

    def read_storage(self):

        with open(self.path_name+'/Escritorio/'+self.directory_name+'/'+self.root_name_file_storage, 'r') as f:
            #f.read()
            #print(f)
            
            #list_value = list(f)
            #print(list_value[0])
            for x in f:
                print(x, end="")
            #print(type(list_value))
            #print(list_value[0])
            #for x in list_value:
                #print(x)
                #print(type(x))
            
        return

"""
class Email(object):

    def __init__(self):
"""

























if __name__ == "__main__":

    malware = Malware()
    malware.initialize()
    malware.create_instructions()
    malware.store_directories()
    malware.read_storage()
