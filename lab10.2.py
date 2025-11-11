import numpy as np
import matplotlib.pyplot as plt 
import sys
import os

x = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = [55095, 61404, 51117, 46745, 48033, 31781, 17059, 25123, 25436, 34341, 24047, 49857, 31356, 25345, 27953]
z = [136829, 130457, 121256, 118589, 123912, 129998, 144312, 166944, 182253, 199867, 279279, 297505, 306822, 318078, 311587]

np.array(x)
np.array(y)
np.array(z)
plt.plot(x, z, label='Ukraine', color = "blue")
plt.plot(x, y, label='Germany', color = "red")
plt.title('Children out of school, primary, 2005-2019 years, total', fontsize=15)
plt.ylabel('Indicator', fontsize=12, color='red')
plt.grid(True)
plt.show()

country_input = input("Введіть назву країни (Ukraine або Germany): ").strip()
if country_input.lower() == "ukraine":
    values = z
    color = 'blue'
elif country_input.lower() == "germany":
    values = y
    color = 'red'
else:
    print("Такої країни немає у даних!")
    exit()
plt.figure(figsize=(12,6))
plt.bar(x, values, color=color)
plt.title(f'Children out of school, primary ({country_input}, 2005-2019)', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of children', fontsize=12)
plt.grid(axis='y')
plt.show()
