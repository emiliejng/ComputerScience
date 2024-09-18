import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0,2*np.pi,1000)
y=np.sin(x)

plt.plot(x,y)

plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.title('Sine Wave')

plt.grid()
plt.savefig('sinusoide.png')

