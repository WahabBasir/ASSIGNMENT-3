#ASSIGNMENT 3
#EXAMPLE NO.1
#Saving and Writing a NumPy Array to a Text File:
import numpy as np

# Creating a sample array
arr = np.array([[1, 3, 5], [7, 9, 11]])

# Saving array to a text file
np.savetxt('array.txt', arr, delimiter=',')


#XAMPLE NO.2
#Saving and Writing a NumPy Array to a Binary File:

# Creating a sample array
arr = np.array([[2, 4, 6], [8, 10, 12]])

# Saving array to a binary file
np.save('array.npy', arr)


#EXAMPLE NO.3
#Saving and Writing Multiple Arrays to a Compressed (ZIP) File:
import zipfile

# Creating sample arrays
arr1 = np.array([9, -2, 11])
arr2 = np.array([3, 8, 10])

# Saving arrays to a compressed (ZIP) file
with zipfile.ZipFile('arrays.zip', 'w') as archive:
    np.save(archive, 'array1.npy', arr1)
    np.save(archive, 'array2.npy', arr2)
