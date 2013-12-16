#!/usr/bin/env python
#
# Bener Suay
# December 2013
# benersuay@wpi.edu
#
# A simple script that shows how to use
# an instance of MyCSVLogger class.

from MyCSVLogger import *

# Creates a csv file using the current time stamp as name.
myLogger = MyCSVLogger("myLogger")

# Opens the csv file to append.
myLogger.open()

# add header so we know what we save in each column
myLogger.header(["attribute_1", "attribute_2", "attribute_3"])

# save the data
myLogger.save([1,2,3])
myLogger.save([4,5,6])

# close the log file when we are done.
myLogger.close()

# Oops, we forgot to add one more line
myLogger.open() 
myLogger.save([7,8,9])
myLogger.close()

# We can also open a file with a given name
anotherLogger = MyCSVLogger("important_experiment_notes","my_second_log_file")

anotherLogger.open()
anotherLogger.header(["feature_1", "feature_2", "feature_3"])
anotherLogger.save([1,2,3])
anotherLogger.close()

