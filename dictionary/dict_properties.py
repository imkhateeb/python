# Concatenation
D1 = {'a': 10, 'b': 20}
D2 = {'c': 30, 'd': 40}

# Concatenation (Merging) using **
merged_dict = {**D1, **D2}
print("Merged Dictionary:", merged_dict)

Student1 = {'Name': 'John', 'RollNo': 101}
Student4 = Student1

print("ID of Student1:", id(Student1))
print("ID of Student4:", id(Student4))


# Aliasing
# Using copy() method
Student5 = Student1.copy()

# Using ** operator
Student6 = {**Student1}
print(Student5, Student6)


# Searching
D1 = {'a': 10, 'b': 20, 'c': 30}
Bool1 = 'a' in D1
Bool2 = 'b' in D1
Bool3 = 10 in D1  # Output will be False since 10 is not a key


# Identity
S1 = {'Name': 'John', 'RollNo': 101}
S3 = {'Name': 'John', 'RollNo': 101}
S2 = S1
Res1, Res2 = S1 is S2, S1 is S3
print("Are S1 and S2 the same object?", Res1, Res2)


# Exmptiness
D1 = {'a': 10, 'b': 20, 'c': 30}
bool_D1 = bool(D1)

D2 = {}
bool_D2 = bool(D2)

if not D1:
    print("D1 is an empty dictionary")

if not D2:
    print("D2 is an empty dictionary")
