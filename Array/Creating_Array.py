#Creating an array in Python using the array module

import array
# Create an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])
# Print the array
print("Integer Array:", int_array)
# Create an array of floats
float_array = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
# Print the array
print("Float Array:", float_array)