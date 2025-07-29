import numpy as np
n = int(input("enter size of square matrix  (n x n): "))
print(f"Enter {n*n} elements (row-wise,space separted):")
elements = list(map(float, input().split()))
print(elements)
matrix = np.array(elements).reshape(n, n)
print("\nOrginal matrix")
print(matrix)
det = np.linalg.det(matrix)
print(det)
if det == 0:
	print("\n matrix is singular (det = 0),inverse does not exist.")
else:
	inverse = np.linalg.inv(matrix)
	print("\ninverse matrix:")
	print(inverse)
