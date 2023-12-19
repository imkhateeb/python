# Importing the entire module
# import arithmetics

# # Using functions from the module
# result_add = arithmetics.add(5, 3)
# result_subtract = arithmetics.subtract(8, 2)

# print(result_add)       # Output: 8
# print(result_subtract)  # Output: 6

# Importing the module with an alias
# import arithmetics as arit

# # Using functions from the module using the alias
# result_multiply = arit.multiply(4, 6)
# result_divide = arit.divide(9, 3)

# print(result_multiply)  # Output: 24
# print(result_divide)    # Output: 3.0


# main_script_specific.py

# Importing specific functions from the module
from arithmetics import add, subtract

# Using the imported functions directly
result_add = add(7, 2)
result_subtract = subtract(10, 4)

print(result_add)       # Output: 9
print(result_subtract)  # Output: 6
