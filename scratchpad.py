from datasets import generate
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

import regression
import plotter

rate = 0.1
lim = 0.5
data_file = 'lrg_100_10i.csv'
thr = 15

r1 = 0.5
r2 = 0.7
r3 = 0.9
r4 = 1
r5 = 0.5
r6 = 1
r7 = 0.7
r8 = 0.8
r9 = 0.9


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

regression.load(data_file,75)
results7 = regression.train(lim,thr,r7)      
axis7 = range(0,len(results7),1)
regression.reset()

regression.load(data_file,75)
results8 = regression.train(lim,thr,r8)      
axis8 = range(0,len(results8),1)
regression.reset()

regression.load(data_file,75)
results9 = regression.train(lim,thr,r9)      
axis9 = range(0,len(results9),1)
regression.reset()

#plotter.plot_adaptive(regression._cost_array,lim)

#plt.semilogy(axis1,results1,"pink",axis2,results2,"purple",axis3,results3,"g",axis4,results4,"y",axis5,results5,"b",axis6,results6,"r")
plt.semilogy(axis1,results1,"pink",axis2,results2,"purple",axis3,results3,"g",axis4,results4,"y")
        
patch1 = mpatches.Patch(color='pink', label=r1)
patch2 = mpatches.Patch(color='purple', label=r2)
patch3 = mpatches.Patch(color='green', label=r3)
patch4 = mpatches.Patch(color='yellow', label=r4)
patch5 = mpatches.Patch(color='blue', label=r5)
patch6 = mpatches.Patch(color='red', label=r6)

tit = 'Change in Error with Time - Adaptive Factor Comparison at CIE limit : '+str(lim)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title(tit)
#plt.legend(handles=[patch1,patch2,patch3,patch4,patch5,patch6])
plt.legend(handles=[patch1,patch2,patch3,patch4])
plt.grid(True)
plt.show(block=True)

print 


