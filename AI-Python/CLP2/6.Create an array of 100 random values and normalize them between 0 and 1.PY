import numpy as np

# Generate 100 random values from a uniform distribution over [0, 100)
arr = np.random.uniform(0, 100, 100)

# Normalize the array between 0 and 1
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print(normalized_arr)