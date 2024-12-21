import numpy as np

#set the seed
np.random.seed(42)

#generate random numbers
random_numbers = np.random.rand(5)

print("Random numbers with seed 42:", random_numbers)
print("Random numbers with seed 42:", random_numbers)
print("Re-generated numbers with seed 42:", np.random.rand(5))

#Using Random Generators Without a Global Seed
rng= np.random.default_rng(42)
print("Random numbers with default_rng:", rng.random(5))