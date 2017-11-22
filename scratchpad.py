from datasets import generate
import regression

regression.reset()
regression.load('lrg_100_10.csv',75)
#print regression._data
#print regression._test_data
print regression.train(0.0005,1,0.7)
regression.test()