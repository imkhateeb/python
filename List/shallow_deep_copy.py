import copy

original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)

# Modify the original list
original_list[1][0] = 99

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)


# Modify the original list
original_list = [10, [20, 30], 40]
deep_copy = copy.deepcopy(original_list)
original_list[1][0] = 90
# print("Original List:", original_list)
# print("Deep Copy:", deep_copy)
