from pandas import DataFrame as DF

# tup_of_lists = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
# list_of_tups = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# list1 = [100, 200, 300, 400, 500]

# data1 = DF(tup_of_lists)
# data2 = DF(list_of_tups)
# data3 = DF(list1)

# print(tup_of_lists)
# print(data1)
# print(data2)

# print(data2.index)

# for i in data2.index:
#         print(i)

# print(data2.index.dtype)


# print(data3.values)
# print(data2.values)

dict1 = {"a": [10, 20, 30, 40, 50], "b": [16, 17, 18, 19, 20]}

students = {"Name": {"1": "Khateeb", "2": "Siva", "3":"Varad"}, "Roll": {"1": "2022UG3006", "2": "2022UG2030", "3": "2022UG3005"}, "Section": {"1": "B", "2": "B", "3": "C"}}

df1 = DF(dict1, columns=["a", "b"], index=["row-1", "row-2", "row-3", "row-4", "row-5"])
df1["sum"] = df1["a"] + df1["b"]
df1["diff"] = df1["a"] - df1["b"]
df1["mul"] = df1["a"] * df1["b"]
df1["div"] = df1["a"] / df1["b"]

df2 = DF(students)

# print(df1)
# print(df1.values)
print(df2)

# Creating CSV file of data

df2.to_csv("test1.csv", index=False, header=[1, 2, 3])
