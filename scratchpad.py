from datasets import generate
import regression
import plotter

rate = 0.6
lim = 0.5


while lim > 0.000005:
    regression.reset()
    regression.load('lrg_100_10.csv',75)
    results = regression.train(lim,1,rate)
    #print "Slope : ",results[0]," Intercept : ",results[1]
    regression.test()
    plotter.plot_adaptive(regression._cost_array,lim)
    print 
    lim = lim/10


