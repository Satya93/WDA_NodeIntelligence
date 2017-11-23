from datasets import generate
import regression
import plotter

rate = 0.1
lim = 0.00005



regression.reset()
regression.load('lrg_100_10.csv',75)
results = regression.train(lim,1,rate)
#print "Slope : ",results[0]," Intercept : ",results[1]
print "Rate : ",rate
regression.test()
#plotter.plot_adaptive(regression._cost_array,rate)
print 


