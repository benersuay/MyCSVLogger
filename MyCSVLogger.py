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
        try:
            self.file = open(self.fname, mode)
        except Exception, err:
            self.file = None
            print "Error opening CSV file: "+self.fname+" in "+mode+"."
            print err

    def save(self, entry): # entry should be a list
        try:
            for eIdx, e in enumerate(entry):
                self.file.write(str(e))
                if(eIdx == len(entry)-1):
                    self.file.write('\n')
                else:
                    self.file.write(',')
        except Exception, err:
            print "Error saving data in file: "+self.fname
            print err

    def close(self):
        try:
            self.file.close()
        except Exception, err: 
            print "Error closing file: "+self.fname
            print err
            return False

        return True

    def header(self, labels): # this function is actually redundant but the name makes the purpose easy to understand
        # In the future, even if the file has a lot of data in it, this function should just change / replace the first line.
        try:
            self.save(labels)
        except Exception, err: 
            print "Error adding data header."
            print err
