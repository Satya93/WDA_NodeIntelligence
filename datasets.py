import random
import csv

def generate(size,lb,ub,filename):
    data = []
    ele = 0
    while ele < size:
        #value = pow(float(ele)/10,2)+random.randint(lb,ub)
        value = size-ele+random.randint(lb,ub)
        data.append(value)
        ele+=1
    myFile = open(filename, 'w') 
    with myFile:  
        writer = csv.writer(myFile)
        writer.writerows([data])
    print data

generate(100,0,10,"lrg_100_10i.csv")