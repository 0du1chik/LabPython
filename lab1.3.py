while True:
    N = int(input("Введіть N (1 < N < 9): "))
    if 1 < N < 9:
        break
for i in range(N, 0, -1):
    for j in range(i, N + 1):
        print(j, end=" ")
    print()