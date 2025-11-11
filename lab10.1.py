import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 5, 500)

y = -5 * np.cos(10 * x) * np.sin(3 * x) / (x ** x)

plt.plot(x, y, color='blue', linewidth=2, label='Y(x) = -5*cos(10x)*sin(3x)/(x^x)')

plt.title('Графік функції Y(x)', fontsize=14)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.show()
