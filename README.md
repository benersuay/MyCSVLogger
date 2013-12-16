MyCSVLogger
=============

This class helps saving your experiment data in a CSV file. It generates a file name from timestamp, or you can pass in your desired file name and notes. It keeps the file name, so you can append to it later on without having to remember it.

## Usage ##

Import the class

    from MyCSVLogger import *

Get an instance, add data, and close when you're done:

    anotherLogger = MyCSVLogger("my_important_experiment_notes","my_log_file")
    anotherLogger.open()
    anotherLogger.header(["feature_1", "feature_2", "feature_3"])
    anotherLogger.save([1,2,3])
    anotherLogger.close()

demo.py script shows the usage, and outputs 2 CSV files in the folder it is run:

    python demo.py