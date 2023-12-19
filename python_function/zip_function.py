# Example 1: Basic usage
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Using zip to combine the lists element-wise
result = zip(list1, list2)

# Converting the result to a list to visualize the tuples
result_list = list(result)
print(result_list)
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Example 2: Zip with three iterables
tuple1 = (10, 20, 30)
tuple2 = ['x', 'y', 'z']
list3 = [100, 200, 300]

# Combining three iterables using zip
result = zip(tuple1, tuple2, list3)
print(result)

# Converting the result to a list to visualize the tuples
result_list = list(result)
print(result_list)
# Output: [(10, 'x', 100), (20, 'y', 200), (30, 'z', 300)]


S1=input('enter the string: ')
L=list(filter(str.isalnum,S1))
print(L)
