def Asum():
    A=list(map(int,input("Введіть елементи списку через пробіл: ").split()))
    print("Список:", A)
    S=sum(A)
    print("Сума елементів списку:", S)
Asum()
