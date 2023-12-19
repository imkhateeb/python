# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union using operator '|'
union_operator = set1 | set2
print("Union using operator:", union_operator)

# Union using method set.union()
union_method = set1.union(set2)
print("Union using method:", union_method)

# Intersection using operator '&'
intersection_operator = set1 & set2
print("Intersection using operator:", intersection_operator)

# Intersection using method set.intersection()
intersection_method = set1.intersection(set2)
print("Intersection using method:", intersection_method)

# Difference using operator '-'
difference_operator = set1 - set2
print("Difference using operator:", difference_operator)

# Difference using method set.difference()
difference_method = set1.difference(set2)
print("Difference using method:", difference_method)

# Symmetrical Difference using operator '^'
symmetric_difference_operator = set1 ^ set2
print("Symmetrical Difference using operator:", symmetric_difference_operator)

# Symmetrical Difference using method set.symmetric_difference()
symmetric_difference_method = set1.symmetric_difference(set2)
print("Symmetrical Difference using method:", symmetric_difference_method)


# Using set methods to modify the existing set
# Set1.update(Set2) - Union and update
set1.update(set2)
print("After update (union):", set1)

# Set1.intersection_update(Set2) - Intersection and update
set1 = {1, 2, 3, 4, 5}  # Reset set1
set1.intersection_update(set2)
print("After intersection update:", set1)

# Set1.difference_update(Set2) - Difference and update
set1 = {1, 2, 3, 4, 5}  # Reset set1
set1.difference_update(set2)
print("After difference update:", set1)

# Set1.symmetric_difference_update(Set2) - Symmetric Difference and update
set1 = {1, 2, 3, 4, 5}  # Reset set1
set1.symmetric_difference_update(set2)
print("After symmetric difference update:", set1)


# Using operators to modify the existing set
# Set1 |= Set2 - Union and update
set1 = {1, 2, 3, 4, 5}  # Reset set1
set1 |= set2
print("After union update using operator:", set1)

# Set1 &= Set2 - Intersection and update
set1 = {1, 2, 3, 4, 5}  # Reset set1
set1 &= set2
print("After intersection update using operator:", set1)

# Set1 -= Set2 - Difference and update
set1 = {1, 2, 3, 4, 5}  # Reset set1
set1 -= set2
print("After difference update using operator:", set1)

# Set1 ^= Set2 - Symmetric Difference and update
set1 = {1, 2, 3, 4, 5}  # Reset set1
set1 ^= set2
print("After symmetric difference update using operator:", set1)

# Example sets
set1 = {1, 2, 3, 4, 5, 6}
set2 = {2, 4}

# Set1.issuperset(Set2) - Returns True if Set1 is a superset of Set2
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)

# Set1.issubset(Set2) - Returns True if Set1 is a subset of Set2
is_subset = set2.issubset(set1)
print("Is set2 a subset of set1?", is_subset)

# Set1.isdisjoint(Set2) - Returns True if Set1 and Set2 are mutually exclusive
set3 = {7, 8, 9}

is_disjoint = set1.isdisjoint(set3)
print("Are set1 and set3 disjoint?", is_disjoint)
