import numpy as np


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))


matrix = []

print("Enter the elements row by row:")


for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} elements (space-separated): ").split()))
    if len(row) != cols:
        print(f"Error: You must enter exactly {cols} elements.")
        exit()
    matrix.append(row)


np_matrix = np.array(matrix)


transpose = np_matrix.T

print("\nOriginal Matrix:")
print(np_matrix)

print("\nTransposed Matrix:")
print(transpose)

