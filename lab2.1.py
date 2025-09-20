import math
def funkcia1(x:float)->float:
    if x>45:
        return -math.sqrt(x)
    else:
        return math.sin(2*x)
def funkcia2(p:int)->int:
    a,b=0,1
    while b<=p:
        a,b=b,a+b
    return b
x=float(input("Введіть x:"))
print("Результат функції 1:",funkcia1(x))
p=int(input("Введіть p:"))  
print("Перше число Фібоначчі, більше за p:",funkcia2(p))