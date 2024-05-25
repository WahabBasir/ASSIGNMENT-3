#ASSIGNMENT 3 - LOADING
#EXAMPLE NO.1
#Loading CSV Data:
import numpy as np

# Assuming 'data.csv' contains comma-separated values
data = np.genfromtxt('data.csv', delimiter=',')

print(data)


#EXAMPLE NO.2
#Loading Text Data:

# Assuming 'data.txt' contains text data
data = np.loadtxt('data.txt')

print(data)


#EXAMPLE NO.3
#Loading Binary Data:

# Assuming 'data.bin' contains binary data
data = np.fromfile('data.bin', dtype=np.float64)

print(data)
