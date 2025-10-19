def delete():
    A=list(map(int, input("Введіть елементи списку через пробіл: ").split()))
    A = [A[i] for i in range(len(A)) if i % 2 == 0]
    print("Список після видалення елементів з непарним порядковим номером:", A)
delete()    