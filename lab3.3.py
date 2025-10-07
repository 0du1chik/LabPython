z = str(input("Введіть речення: "))
words = z.split()
max_length = max(len(word) for word in words)
if max_length > 10:
    print("Твердження істинне: найдовше слово має більше 10 символів.")
else:
    print("Твердження хибне: найдовше слово має 10 або менше символів.")