list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
result = list1 + list2
# print("Concatenation:", result)

list1 = [1, 2, 3]

# Replication
replicated_list = list1 * 3
# print("Replication:", replicated_list)

# Aliasing
aliased_list = list1
# print("Original List:", list1)
# print("Aliased List:", aliased_list)

list1 = [1, 2, 3]

# Cloning using slice
cloned_list = list1[:]
# print("Original List:", list1)
# print("Cloned List:", cloned_list)

list1 = [1, 2, 3, 4, 5]

# Searching
element_to_search = 100
if element_to_search in list1:
    print(f"{element_to_search} found in the list.")
else:
    print(f"{element_to_search} not found in the list.");


list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Identity
if list1 is list3:
    print("Lists are identical.")
else:
    print("Lists are not identical.");

# Comparison
if list1 == list2:
    print("Lists are equal.")
else:
    print("Lists are not equal.")

S1='India is my country'
type(S1)
L1=S1.split()
# print(L1)
# print(type(L1))
L2=L1[::-1]
S2=' '.join(L2)
# print(S2)

empty_list = [1]

# Emptiness
if not empty_list:
    print("List is empty.")
else:
    print("List is not empty.");

List1 = ['s', 'e', 'a', 'r', 'c', 'h', 'i', 'n', 'g']
Bool1 = 'a' in List1
Bool2 = 'b' in List1
Bool3 = 'z' not in List1

print("Bool1:", Bool1)
print("Bool2:", Bool2)
print("Bool3:", Bool3)

A=[1,2,3,9,5]
B=[1,2,2,7,8]
Res1= A<B
print(Res1)




