"""
This module is responsible for processing the data.  It will largely contain functions that will receive the overall dataset and
perform necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""


import csv

# Defining load_data function

def load_data(filename):

    data = []
    file = open(filename, "r", encoding="utf-8")
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)
    file.close()
    return data

