from matplotlib import pyplot as plt
import time
import csv

#Global Scope
_slope = 0
_mean = 0
_data = []
_train_data = []
_test_data = []

def reset():
    _slope = 0
    _mean = 0
    _data = []
    _train_data = []
    _test_data = []

def load(filename, train):
    with open(filename) as myFile:  
        reader = csv.reader(myFile, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            datas = row
    for x in datas:
        _data.append(int(x))