import matplotlib.pyplot as plt

#Part 1
'''
import csv
x = []
y = []

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file!')
'''

# Numpy loading data
import numpy as np
x,y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph')
plt.legend()
plt.show()