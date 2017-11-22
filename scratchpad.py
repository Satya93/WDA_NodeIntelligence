from datasets import generate
import regression

regression.reset()
regression.load('lrg_100_10.csv',80)
print regression._data
