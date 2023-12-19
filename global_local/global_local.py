# Example demonstrating the use of the global keyword

global_variable = "I am global"

def example_function():
    global global_variable
    global_variable = "I am modified inside the function"
    print("Inside Function:", global_variable)

# Call the function
example_function()

# The global variable is modified outside the function due to the use of the global keyword
print("Outside Function:", global_variable)
