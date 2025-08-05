import matplotlib.pyplot as plt
import numpy as np
a=[1, 2, 6, 18]
b=[3, 10, 12, 20]
x=np.array(a)
y=np.array(b)
plt.plot(x, y, marker='o', linestyle=':', color='red',mec='green',mfc='green')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("PLOTTED GRAPH")
plt.show()
