from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import regression

def plot_adaptive(data,labeld):
    legend = 'CIE Limit :' + str(labeld)
    axis = range(0,len(data),1)
    plt.semilogy(axis,data,"r")
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.title('Change in Error with Time - Exponential Adaptive Factor')
    red_patch = mpatches.Patch(color='red', label=legend)
    plt.legend(handles=[red_patch])
    plt.grid(True)
    plt.show(block=True)


