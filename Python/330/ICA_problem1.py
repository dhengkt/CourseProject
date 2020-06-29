import numpy as np

A = np.array([[1, 6, 8],
              [5, 6, 3],
              [1, 4, 9]])
              
x = np.array([[4],[2],[8]])

B = np.array([18, 28, 21])

check = np.linalg.solve(A, B)

print(A)
print(check)
