fruitsPrice = {'Apple': 30, 'Banana': 40, 'Mango': 10}
vegsPrice = {'Brinjal': 10, 'Carrot': 30, 'Pumpkin': 40}
print(fruitsPrice)

print([*fruitsPrice])
print({*fruitsPrice})
# print((*fruitsPrice)) # cannot use starred expression in tuple

print({**fruitsPrice, **vegsPrice})