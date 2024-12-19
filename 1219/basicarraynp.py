import numpy as np
print(np.__version__)
#create numpy 1d array
array1d= np.array([1,2,3,4,5])
print(array1d)
#create numpy 2d array
array2d= np.array([[1,2,3],[4,5,6]])
print(array2d)

print ("Type:" , type(array1d))

print ("Shape:" , array1d.shape)
print("Size:" , array1d.size)
print("Type:" , array1d.dtype)

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])


print("Addition:", array_a + array_b)
print("Subtraction:", array_a - array_b)
print("Multiplication:", array_a * array_b)
print("Division:", array_a / array_b)

print("Sum:", array_a.sum())
print("Mean:", array_a.mean())
print("Max:", array_a.max())
print("Min:", array_a.min())

array_c = np.array([[1, 2, 3], [4, 5, 6]])
scalar= 2
print("Array * Scalar:", array_c * scalar)