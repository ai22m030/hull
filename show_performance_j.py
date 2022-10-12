import numpy as np
import matplotlib.pyplot as plt

matrix = np.loadtxt('o_notation_data.txt')

plt.plot(matrix[:,0],matrix[:,1])
plt.xlabel('Points (n)')
plt.ylabel('Time (s)')
plt.suptitle('Jarvis March O(n)')

#Show the data points divided by n*log(n)
plt.figure()
plt.plot(matrix[:,0],np.divide(matrix[:,1],np.multiply(np.log(matrix[:,0]),matrix[:,0])))
plt.xlabel('Points (n)')
plt.ylabel('Time Ratio (s/s)')
plt.suptitle('Divide & Conquer O(n)/(nlogn)')

plt.show()