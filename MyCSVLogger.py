#!/usr/bin/env python
#
# Bener Suay
# January 2013
# benersuay@wpi.edu
#
# This class saves and reads data to / from a CSV file.

import time
import os
import sys
from datetime import datetime

class MyCSVLogger():

    def __init__(self, argNote='', argName=None):
        if(argNote != ''):
            argNote = '_'+argNote

        if(argName != None):
            self.fname = argName + argNote + '.csv'
        else:
            timestamp = str(datetime.now())
            self.fname = timestamp[0:10]+'_'+timestamp[11:19]+argNote+'.csv'
            
    def open(self,mode='a'):
        # opens the file for appending; any data written to the file is automatically added to the end
        # 'w' is for only writing (an existing file with the same name will be erased)
        self.file = open(self.fname, mode)

    def save(self, entry): # entry should be a list
        for e in range(len(entry)):
            self.file.write(str(entry[e]))
            if(e == len(entry)-1):
                self.file.write('\n')
            else:
                self.file.write(',')

    def close(self):
        self.file.close()

    def header(self, labels): # this function is actually redundant but the name makes the purpose easy to understand
        # In the future, even if the file has a lot of data in it, this function should just change / replace the first line.
        self.save(labels)

    def read(self, entryNum):
        # This method is supposed to return the entry_numth entry in the file, to be implemented later.
        pass
