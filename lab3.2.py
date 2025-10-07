t = str(input("Введіть слово: "))
if any(ch.isdigit() for ch in t):
    print("У цьому рядку є цифри.")
else:
    print("У цьому рядку немає цифр.")