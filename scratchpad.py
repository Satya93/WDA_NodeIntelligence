from datasets import generate
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

import regression
import plotter

rate = 0.1
lim = 0.00005
data_file = '100_deg2.csv'
thr = 15

r1 = 0.2
r2 = 0.3
r3 = 0.9
r4 = 0.93
r5 = 0.95
r6 = 0.98

regression.reset()
regression.load(data_file,75)
results1 = regression.train(lim,thr,r1)
axis1 = range(0,len(results1),1)
regression.reset()

regression.load(data_file,75)
results2 = regression.train(lim,thr,r2)  
axis2 = range(0,len(results2),1)
regression.reset()

regression.load(data_file,75)
results3 = regression.train(lim,thr,r3)  
axis3 = range(0,len(results3),1)
regression.reset()

regression.load(data_file,75)
results4 = regression.train(lim,thr,r4)  
axis4 = range(0,len(results4),1)
regression.reset()

regression.load(data_file,75)
results5 = regression.train(lim,thr,r5)
axis5 = range(0,len(results5),1)
regression.reset()

regression.load(data_file,75)
results6 = regression.train(lim,thr,r6)      
axis6 = range(0,len(results6),1)
regression.reset()
    #plotter.plot_adaptive(regression._cost_array,lim)

plt.semilogy(axis3,results3,"g",axis4,results4,"y",axis5,results5,"b",axis6,results6,"r")
        
patch1 = mpatches.Patch(color='red', label=r1)
patch2 = mpatches.Patch(color='red', label=r2)
patch3 = mpatches.Patch(color='green', label=r3)
patch4 = mpatches.Patch(color='yellow', label=r4)
patch5 = mpatches.Patch(color='blue', label=r5)
patch6 = mpatches.Patch(color='red', label=r6)

tit = 'Change in Error with Time - Adaptive Factor Comparison at CIE limit : '+str(lim)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title(tit)
plt.legend(handles=[patch3,patch4,patch5,patch6])
plt.grid(True)
plt.show(block=True)

print 


