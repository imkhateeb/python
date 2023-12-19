from pandas import DataFrame as DF
dict1 = {'name': "Khateeb", 'roll': '2022ug3006', 'salary': '200000'}


data1 = DF(dict1, index=[1])
print(data1)