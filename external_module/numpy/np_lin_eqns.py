import numpy as np

# Coefficients of the equations
# For example, equations are 2x + 3y = 8 and 5x - y = 9
a = np.array([[2, 3], [5, -1]])

# Constants on the right-hand side
b = np.array([8, 9])

# Calculating the inverse of matrix a
a_inv = np.linalg.inv(a)

# Solving for x and y using matmul
x = np.matmul(a_inv, b)

# print(x)  # This will print the values of x and y

A = np.array([[1, 2, 10], [3, 4, 20], [5, 6, 30]]);
A1 = A.copy()
A2 = A.view()
# A1[0,0] = 100
A2[0,0] = 100

B = np.array([[10, 20, 100], [30, 40, 200], [50, 60, 300]]);

# print(A[0, 0:2])
# print(A.shape)
# print(A.copy())

# print(A)
# print(A1)
# print(A2)

# print(A.shape[0])
# print(trace(A))
ans = np.matmul(A, B)
ans = np.hstack((A, B))
print(ans)
ans = np.vstack((A, B))
con = np.concatenate((A, B), axis=0)
# print(con)