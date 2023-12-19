import numpy as np

def create_array(*arr):
        i = 0
        A = np.zeros((len(arr), len(arr)), dtype='int32')
        for k in range(len(A)):
                for j in range(len(A)):
                        if k == j:
                                A[k][j] = arr[i]
                                i = i+1
        print(A)

create_array(10, 11, 12, 13)