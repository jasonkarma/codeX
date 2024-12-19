import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nAddition:")
print(matrix_a + matrix_b)

print("\nSubtraction:")
print(matrix_a - matrix_b)

print("\nMultiplication:")
print(matrix_a * matrix_b)

print("\nDivision:")
print(matrix_a / matrix_b)

#transpose matrix
transpose= matrix_a.T
print("Transpose of Matrix A: \n" , transpose)

#Determinant of a Matrix
det=    np.linalg.det(matrix_a)
print("Determinant of Matrix A: \n" , det)
