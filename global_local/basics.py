# Example demonstrating global and local variable scopes

global_variable = "I am global"

def example_function():
    # Local variable with the same name as the global variable
    global_variable = "I am local"
    print("Inside Function:", global_variable)

# Call the function
example_function()

# The global variable remains unchanged outside the function
print("Outside Function:", global_variable)