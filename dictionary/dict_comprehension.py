# Dictionary comprehension with a single for loop
# Generates a dictionary of n and its square for n in the range 1 to 9
result_dict = {n: n * n for n in range(1, 10)}
# print(result_dict)


# {(n, n+1): n*n for n in range(1,10)} - Valid
# Generates a dictionary with keys as tuples (n, n+1) and values as n*n for n in the range 1 to 9
result_dict_2 = {(n, n+1): n*n for n in range(1, 10)}
print(result_dict_2)

# {[n, n+1]: n*n for n in range(1,10)} - Invalid (Lists are not hashable)
# Generates a TypeError because lists are not hashable and cannot be used as dictionary keys

# {{n, n+1}: n*n for n in range(1,10)} - Invalid (Sets are not hashable)
# Generates a TypeError because sets are not hashable and cannot be used as dictionary keys
