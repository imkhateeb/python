my_set = { n for n in range(0, 100) if (n%5 == 0 and n%2 == 0) }
# print(my_set)

squares = lambda x: x*x
cubes = lambda x: x*x*x

my_set2 = { n for n in range(-10, 10) }
my_set3 = { squares(n) if n%2 == 0 else cubes(n) for n in range(-10, 10) }

print(my_set2)
print(my_set3)

# Case 3: Set comprehension with if-else condition
set_N = {n * n if n > 5 else n * n * n for n in range(-10, 10)}

print("Case 3 Set:", set_N)


# Case 3: Set comprehension with if-else condition
set_1 = {n ** 0.5 if n < 6 else n // 4 for n in range(0, 20)}

print("Case 3 Set (another example):", set_1)


# Case 4: Nested for loop
nested_for = {(i, j) for i in range(1, 4) for j in range(1, 4)}

print("Case 4 Nested For Set:", nested_for)


# Case 4: Nested for loop
nested_for_2 = {(i, j) for i in range(1, 3) for j in range(1, 3) if i != j}

print("Case 4 Nested For Set (another example):", nested_for_2)


# Case 5: Multiple Input
set_multiple_input = {(i, j) for i in range(1, 4) for j in range(1, 4) if i != j}

print("Case 5 Multiple Input Set:", set_multiple_input)


# Case 6: Nested comprehension not applicable to sets
# This is an example of nested list comprehensions, not applicable to sets
# set_nested_comprehension = {(i, j) for i in range(1, 4) for j in range(1, 4)}

# Uncommenting the line above would result in a syntax error
# Sets do not support nested comprehension in the same way as lists.