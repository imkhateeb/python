set1 = {1, 2, 3}
alias_set = set1
# Aliasing
# print("Original Set:", set1)
# print("Aliased Set:", alias_set)
# print(id(set1))
# print(id(alias_set))


clone_set = set1.copy()
# Cloning using copy method
# print("Original Set:", set1)
# print("Cloned Set:", clone_set)
# print(id(set1))
# print(id(clone_set))


# set1 = {1, 2, 3, 4, 5}
# # Searching
# element_to_search = 3
# if element_to_search in set1:
#     print(f"{element_to_search} found in the set.")
# else:
#     print(f"{element_to_search} not found in the set.")


set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = set1
set4 = set1.copy()
print(id(set1))
print(id(set4))
set1.add(12)
del(set3)
# print(set3)
print(set4)
# Identity
if set1 is set2:
    print("Sets are identical.")
else:
    print("Sets are not identical.")


# set1 = {1, 2, 3}
# set2 = {4, 2, 1}
# # Comparison
# if set1 == set2:
#     print("Sets are equal.")
# else:
#     print("Sets are not equal.")


# empty_set = set()
# # Emptiness
# if not empty_set:
#     print("Set is empty.")
# else:
#     print("Set is not empty.");

# s1 = {1, 2, 3, 4}
# s2 = {5, 6, 7, 8}
# # s3 = s1 + s2 # will give an error
# # print(s3)

# Set1 = {'s', 'e', 'a', 'r', 'c', 'h', 'i', 'n', 'g'}
# Bool1 = 'a' in Set1
# Bool2 = 'b' in Set1
# Bool3 = 'c' not in Set1
# print("Bool1:", Bool1)
# print("Bool2:", Bool2)
# print("Bool3:", Bool3)

my_set = {1, 2, 3, 4, 5}

# Discard an item from the set (e.g., removing 3)
print("Set before discarding 3:", my_set)
my_set.discard(3)

print("Set after discarding 3:", my_set)
