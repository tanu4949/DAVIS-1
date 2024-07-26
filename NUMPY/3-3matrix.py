#write a numpy program to create a 3*3 matrix with values ranging 2 to 10
import numpy as np

# Step 1: Generate values from 2 to 10 (inclusive)
values = np.arange(2, 11)  # 11 is exclusive, so this gives us [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 2: Reshape to a 3x3 matrix
matrix = values.reshape((3, 3))

# Display the matrix
print("3x3 Matrix with values ranging from 2 to 10:")
print(matrix)
