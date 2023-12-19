# Unpacking a string
S = "UNPACK"
S1 = [*S]
print(*S)
print(S1)

# Creating lists with unpacking
L1 = [1, 2, 5]
L2 = [7, 8, 9, L1, 10]
print(L2)
print(*L2)

# Using unpacking in a list directly
L3 = [7, 8, 9, *L1, 10]
print(L3)
