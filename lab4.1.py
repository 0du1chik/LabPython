n=int(input("Введіть кількість елементів масиву N: "))
print(f"Введіть {n} цілих чисел:")
array=[int(input()) for _ in range(n)]
sumdodat = sum(x for x in array if x > 0 and x % 2 == 0)
print("Сума додатніх парних елементів масиву:", sumdodat) 
