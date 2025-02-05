import random

def generate_matrix_and_compute_sums(rows, cols):
    # Generate a 5x5 matrix of random integers between 1 and 100
    matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    
    # Compute the row-wise sums
    row_sums = [sum(row) for row in matrix]
    
    return matrix, row_sums

# Example usage
rows, cols = 5, 5
matrix, row_sums = generate_matrix_and_compute_sums(rows, cols)

print("Matrix:")
for row in matrix:
    print(row)

print("\nRow-wise sums:")
print(row_sums)