import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access a specific element
print("Element at [1, 2]:", array[1, 2])

# Access a row
print("Row 1:", array[1, :])

# Access a column
print("Column 2:", array[:, 2])

# Slice a subarray
print("Subarray:\n", array[0:2, 1:3])

array1 = np.array([1,2,3,4,5,6])
reshaped_array1= array1.reshape(2,3)
print("Reshaped Array:\n", reshaped_array1)

#stacking arrays
array2= np.array([1,2,3])
array3= np.array([4,5,6])
stacked_array = np.stack((array2, array3))
print("Stacked Array:\n", stacked_array)

#splitting arrays
split_arrays = np.array_split(stacked_array, 3)
print("Split Arrays:", split_arrays)

