D1 = {'a': 10, 'b': 20, 'c': 30}

print(D1)

# len()
length = len(D1)

# max()
maximum_value = max(D1.values())

# min()
minimum_value = min(D1.values())

# sum()
sum_of_values = sum(D1.values())

# any() and all()
any_true = any(value > 30 for value in D1.values())
all_true = all(value > 5 for value in D1.values())
print(any_true)
print(all_true)


# del() - deleting an item
del D1['a']
print(D1)

# sorted()
sorted_keys = sorted(D1.keys())
print(sorted_keys)