# D1 = {'a': 20, 'b': 30, 'c': 40}
# D2 = {1: 20, 2: 30, 3: 40}

# keys = [ key for key in D1.keys()]
# values = [ key for key in D1.values()]

# print(keys)
# print(values)
# print(f"D2 is: ", D2)

# # Iterating through both keys and values
# for key, value in D1.items():
#     print(key, value)


# Student1 = dict(Name="Madhuri", RollNo=1001, Marks=75)
# Student2 = dict(Name="Ritik", RollNo=1074, Marks=80)
# Student3 = dict(Name="Devam", RollNo=3016, Marks=85)

# D1 = dict(I=Student1, II=Student2, III=Student3)

# print(D1)


D3 = {
    "name": "Md Khateebur Rab",
    "roll": "2022UG3006",
    "secction": "A"
}

print(D3)
for key in D3.keys():
    print(D3[key])