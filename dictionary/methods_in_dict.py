D1 = {'a': 10, 'b': 20, 'c': 30}
print(D1)

# copy() - deep copy
D2 = D1.copy()
print(D2)

# clear() - to clear the contents of a dictionary
D1.clear()
print(D1)

# update() - to update an existing dictionary with the contents of another dictionary
D3 = {'d': 40, 'e': 50}
D1.update(D3)
print(D1)

# popitem() - to remove the items in the dictionary following LIFO rule.
item_removed = D1.popitem()
print(item_removed)

D1 = {'a': 10, 'b': 20, 'c': 30}
# pop(key) - to remove an item specified by the key
value_removed = D1.pop('b')
print(value_removed)
