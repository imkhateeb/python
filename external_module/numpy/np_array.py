import numpy as np
from numpy import *

arr1 = np.arange(1, 100, 3)
# print(type(arr1))

arr2 = np.arange(1, 100, 3, dtype="f")
# print(arr2)
# print(arr2[0])  # 1.0
# print(arr2[-1])  # 97.0

arr3 = np.zeros((3, 3), dtype="i8")
# print(arr3)

arr4 = np.ones((3, 3), dtype="f8")
# print(arr4)

arr5 = np.eye(3)
# print(arr5)
# print(arr5[0])
# print(arr5[-1])

arr6 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
])
# print(arr6)
# print(arr6[:, 0])
# print(arr6[1, 1])
# print(arr6[1][1])
# print(arr6[:, 0: 1])


list1 = [1, 4, 7, 11, 15, 20, 32]
arr7 = np.array(list1)
arr8 = arr7[arr7%4 == 0]
# print(arr8)

arr9 = arr7[np.logical_or(arr7%4 == 0, arr7%5 == 0)]
# print(arr9)

arr10 = np.array(list1, dtype='i4')

print(arr7)
arr11 = np.where(arr7%2 == 0, 10, 100)
print(arr11)

# arr12 = np.array([[1, 2], [3, 4]])
# arr13 = np.array([[5, 6], [7, 8]])
# result = np.matmul(arr1, arr2)
# print(result)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.matmul(a, b)
# print(result)  # Output: [[19 22]
               #          [43 50]]
# print(a@b)
# print(a.T)
print(a/b)

arr12 = [
        [1, 4, 5],
        [32, 23, 7],
        [12, 5, 7]
]

print(np.linalg.det(arr12))
print(np.linalg.inv(arr12))