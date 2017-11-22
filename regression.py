from matplotlib import pyplot as plt
import time
import csv

#Global Scope
_slope = 0
_intercept = 0
_data = []
_train_data = []
_test_data = []

def reset():
    _slope = 0
    _intercept = 0
    _data = []
    _train_data = []
    _test_data = []

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

def regression(lim, alp, gr):
    global _train_data,_slope,_mean

    #Metrics
    alpha = alp
    numel = len(_train_data)
    mean = sum(_train_data)/numel
    _slope = 5
    _intercept = mean
    print _intercept
    iterations = 0
    axis = range(0,numel)
    maxel = max(_train_data)
    minel = min(_train_data)
    tot_err0 = 0
    tot_err1 = 0
    tot_cost = 20
    old_cost = 10
    mse = 0
    cost_array = []

    while abs(tot_cost-old_cost) > lim:
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
        cost_array.append(tot_cost)

        # Adaptive Step size Learning rate
        if (tot_cost < old_cost) : alpha += alpha*gr
        else : alpha -= alpha*gr

        # Update values of slope and intercept
        del_0 = alpha*tot_err0/numel
        del_1 = alpha*tot_err1/numel
        _intercept = _intercept - del_0
        _slope = _slope - del_1

        # Prints and debugs
        #print "At slope = %.2f" %_slope, " and intercept = %.2f" %_intercept, " Total cost is : ", tot_cost
        print "Error : ", tot_cost , " | Iterations = ", iterations

        iterations+=1
    return[_slope,_intercept]





