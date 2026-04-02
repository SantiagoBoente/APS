import numpy as np
import matplotlib.pyplot as plt


N = 8

n = np.arange(0, N, 1)

def x(n):
    return 4 + 3*np.sin(np.pi/2*n)

x1 = x(n) 

plt.figure()
plt.stem(x1)
plt.title('x[n]')
plt.show()

x2 = np.fft.fft(x1)

xabs = np.abs(x2)**2 *(1/N**2)

plt.figure()
plt.stem(xabs)
plt.title('Valor absoluto de X[k]')
plt.show()

xfase = np.angle(x2)

plt.figure()
plt.stem(xfase)
plt.title('Fase de X[k]')
plt.show()


