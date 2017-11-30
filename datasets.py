import random
import csv

def generate(size,lb,ub,filename):
    data = []
    ele = 0
    while ele < size:
        value = pow(ele,2)+random.randint(lb,ub)
        data.append(value)
        ele+=1
    myFile = open(filename, 'w') 
    with myFile:  
        writer = csv.writer(myFile)
        writer.writerows([data])
    print data

generate(100,0,10,"100_deg2.csv")