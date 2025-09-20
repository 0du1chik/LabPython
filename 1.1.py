a=int(input("Введіть а:"))
while(a<1 or a>100):
    a=int(input("Введіть ще раз а:"))
b=int(input("Введіть b:"))
while(b<1 or b>100):
    b=int(input("Введіть ще раз b:"))
if a>b:
    x=2*a-b
elif a==b:
    x=-2
else:
    x=(a-5)/b
print("Результат обчислення: ",x)