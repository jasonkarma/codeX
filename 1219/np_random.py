import numpy as np

#Generating random numbers
# Random float between 0 and 1
random_float= np.random.rand()
print("Random float:", random_float)
# Random array of floats (1D)
random_array= np.random.rand(5)
print("Random array:", random_array)

# Random 2D array
random_2d_array= np.random.rand(3, 3)
print("Random 2D array:\n", random_2d_array)

#Random Integers
# Random integer between 0 and 10
random_int= np.random.randint(0, 10)
print("Random integer:", random_int)
#Random 1D array of integers
random_int_array= np.random.randint(0, 10, 5)
print("Random 1D array of integers:", random_int_array)
## Random 2D array of integers
random_int_2d_array= np.random.randint(0, 10, (3, 3))
print("Random 2D array of integers:\n", random_int_2d_array)

#Random Distributions
normal_dist= np.random.normal(loc=0, scale=1, size=5)
print("Normal Distribution:\n", normal_dist)

#Uniform distributions

uniform_dist= np.random.uniform(low=0, high=10, size=5)
print("Uniform Distribution:\n", uniform_dist)
