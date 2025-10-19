n = 7
a = [[1 if j % 2 == 0 else 0 for j in range(n)] for _ in range(n)]

for r in a:
    print(*r)