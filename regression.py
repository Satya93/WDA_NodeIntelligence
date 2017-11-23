from matplotlib import pyplot as plt
import time
import csv
import random
import math

#Global Scope
_slope = 0
_intercept = 0
_data = []
_train_data = []
_test_data = []
_estimate_data = []
_done = 0

def reset():
    global _slope, _intercept, _data, _train_data, _test_data, _estimate_data
    _slope = 0
    _intercept = 0
    _data = []
    _train_data = []
    _test_data = []
    _estimate_data = []

def load(filename, train):
    global _train_data,_test_data,_data
    with open(filename) as myFile:  
        reader = csv.reader(myFile, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            datas = row
    for x in datas:
        _data.append(int(x))
    _train_data.append(_data[:train])
    _train_data = _train_data[0]
    _test_data.append(_data[train:])
    _test_data = _test_data[0]

def train(lim, alp, gr):
    global _train_data,_slope,_mean,_axis,_cost_array

    # Metrics
    numel = len(_train_data)
    mean = sum(_train_data)/numel
    _axis = range(0,numel)
    maxel = max(_train_data)
    minel = min(_train_data)

    # Local variables
    alpha = alp
    _slope = (_train_data[numel-1]-_train_data[0])/numel
    _intercept = mean
    iterations = 0
    tot_err0 = 0
    tot_err1 = 0
    tot_cost = 0
    old_cost = 0
    mse = 0
    flag = 0
    _cost_array = []

    while abs(tot_cost-old_cost) > lim or flag == 0:
        # Reset aggregation variables
        estimates = []
        old_cost = tot_cost
        tot_err0 = 0
        tot_err1 = 0
        tot_cost = 0
        elno = 0

        # Begin iteration
        while elno < numel:
            # Calculate current estimate
            curr_estimate = _slope*(elno+1)+_intercept
            estimates.append(curr_estimate)

            # Calculate First derivatives and costs
            err0 = curr_estimate - _train_data[elno]
            err1 = (curr_estimate - _train_data[elno])*float(elno-minel)/float(maxel-minel)
            cost = err0*err0

            # Update total costs
            tot_err0 += err0
            tot_err1 += err1
            tot_cost += cost

            elno += 1
        
        # Append costs to cost array
        tot_cost = tot_cost/(2*numel)
        _cost_array.append(tot_cost)

        # Adaptive Step size Learning rate
        if (tot_cost < old_cost) :
            factor = 2.7183**(-1/(old_cost-tot_cost))
            #factor = gr
            #factor = gr
            #print "Factor is : ",factor
            alpha += alpha*factor/2
            #alpha += alpha*factor
            print "Increase Alpha to : ",alpha," by a factor of ",1+factor
        else : 
            factor = 2.7183**(-1/(tot_cost-old_cost))
            #print "Factor is : ",factor
            alpha -= alpha*factor
            print "Decrease Alpha to : ",alpha," by a factor of ",1-factor
        print 

        # Update values of slope and intercept
        del_0 = alpha*tot_err0/numel
        del_1 = alpha*tot_err1/numel
        _intercept = _intercept - del_0
        _slope = _slope - del_1

        # Prints and debugs
        #print "At slope = %.2f" %_slope, " and intercept = %.2f" %_intercept, " Total cost is : ", tot_cost

        flag = 1
        iterations+=1
        print "Error : ", tot_cost , " | Iterations = ", iterations
        #time.sleep(1)


    print "Error : ", tot_cost , " | Iterations = ", iterations
    return[_slope,_intercept]

def test():
    global _test_data, _slope, _intercept, _train_data

    # Metrics
    numel = len(_test_data)
    offset = len(_train_data)

    # Local variables
    iterations = 0
    tot_cost = 0

    while iterations < numel:
        error = _slope*(iterations+offset)+_intercept-_test_data[iterations]
        #print "Predicted Value : ",_slope*(iterations+offset)+_intercept," | Actual Value : ",_test_data[iterations]," | Error : ",error
        cost = error*error
        tot_cost += cost
        iterations += 1
    tot_cost = tot_cost/(2*numel)
    print "Total Cost after Testing : ", math.sqrt(tot_cost)




