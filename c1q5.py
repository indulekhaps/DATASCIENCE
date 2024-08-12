print("SJC23MCA031 : INDULEKHA P S")
import numpy as np
# Create a 1D array containing the first 15 even numbers as elements
even_numbers = np.arange(2, 31, 2)
# Elements from index 2 to 8 with step 2 using slice notation
slice_result = even_numbers[2:9:2]
# Last 3 elements of the array using negative index
last_3_elements = even_numbers[-3:]
# Alternate elements of the array
alternate_elements = even_numbers[::2]
# Display the last 3 alternate elements
last_3_alternate_elements = alternate_elements[-3:]
print("Original array:", even_numbers)
print("Elements from index 2 to 8 with step 2:", slice_result)
print("Last 3 elements of the array using negative index:",
last_3_elements)
print("Alternate elements of the array:", alternate_elements)
print("Last 3 alternate elements:", last_3_alternate_elements)