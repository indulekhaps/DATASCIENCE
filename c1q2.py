print("SJC23MCA031 : INDULEKHA P S")
import numpy as np
# Create a 2D array (2x3) with complex data type
array_2d = np.array([ [1 + 2j, 3 + 4j, 5 + 6j], [7 + 8j, 9 + 10j,
11 + 12j] ], dtype=complex)
# Print the 2D array
print("2D Array:")
print(array_2d)
# Display the number of rows and columns
rows, columns = array_2d.shape
print("\nNumber of Rows:", rows)
print("Number of Columns:", columns)
# Display the dimensions of the array
dimensions = array_2d.ndim
print("\nDimensions of the Array:", dimensions)
# Reshape the array to 3x2
reshaped_array = array_2d.reshape(3, 2)
# Print the reshaped array
print("\nReshaped Array (3x2):")
print(reshaped_array)