import math
from funkcia3 import funkcia2
def funkcia1(x: float) -> float:
    if x > 45:
        return -math.sqrt(x)
    else:
        return math.sin(2 * x)
x = float(input("Введіть x: "))
print("Результат функції 1:", funkcia1(x))
p = int(input("Введіть p: "))
print("Перше число Фібоначчі, більше за p:", funkcia2(p))