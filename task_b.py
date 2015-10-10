import numpy as np
import matplotlib.pyplot as plt

def z(nx, T):
	return np.exp(-nx**2/float(T))

plt.subplot(3,1,1)
n = 10
T = 10
nx = np.linspace(0.00001, n, 1000)
ind = np.linspace(0, n, n+1)
plt.bar(ind, z(ind, T), width=1, color='r')
plt.plot(nx, z(nx,T))

plt.subplot(3,1,2)
n = 40
T = 300
nx = np.linspace(0.00001, n, 1000)
ind = np.linspace(0, n, n+1)
plt.bar(ind, z(ind, T), width=1, color='r')
plt.plot(nx, z(nx,T))
plt.ylabel('$Z_{1,x}$')

plt.subplot(3,1,3)
n = 80
T = 1000
nx = np.linspace(0.00001, n, 1000)
ind = np.linspace(0, n, n+1)
plt.bar(ind, z(ind, T), width=1, color='r')
plt.plot(nx, z(nx,T))


plt.xlabel('$n_x$')
plt.savefig('task_a_illustration.pdf')
plt.show()