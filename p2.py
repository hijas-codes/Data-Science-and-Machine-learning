import numpy as np
al=np.array([[2,5,8,10],[3,4,6,9]])
sum_all=np.sum(al)
sum_col=np.sum(al,axis=0)
sum_row=np.sum(al,axis=1)
print("Sum of all elements:",sum_all)
print("Sum of each coloumn:",sum_col)
print("Sum of each row:",sum_row)
