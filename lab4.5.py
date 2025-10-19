def search():
    digits = list(map(int, input("Введіть набір цифр через пробіл: ").split()))
    counts = {d: digits.count(d) for d in range(10)}
    maxc = max(counts.values())
    naybilsche = {d for d, c in counts.items() if c == maxc and c > 0}
    print("Цифри, яких найбільше:", naybilsche)
search()