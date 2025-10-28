# Визначити середню вартість журналів, тираж яких менше 10 000 примірників.

def print_magazines(magazines):
    """Вивести всі журнали"""
    print("\nПоточний список журналів:")
    for name, data in magazines.items():
        print(f"Назва: {name}, Ціна: {data['ціна']} грн, Тираж: {data['тираж']} прим.")
    print()


def add_magazine(magazines):
    """Додати новий журнал"""
    try:
        name = input("Введіть назву журналу: ")
        if name in magazines:
            print("Такий журнал вже існує.")
            return
        price = float(input("Введіть ціну журналу (грн): "))
        circulation = int(input("Введіть тираж журналу (примірників): "))
        magazines[name] = {"ціна": price, "тираж": circulation}
        print(f"Журнал '{name}' успішно додано!\n")
    except ValueError:
        print("Помилка: введено некоректні дані.\n")


def delete_magazine(magazines):
    """Видалити журнал за назвою"""
    try:
        name = input("Введіть назву журналу для видалення: ")
        del magazines[name]
        print(f"Журнал '{name}' видалено.\n")
    except KeyError:
        print("Помилка: журнал із такою назвою не знайдено.\n")


def print_sorted(magazines):
    """Вивести журнали за відсортованими ключами"""
    print("\nЖурнали у відсортованому порядку:")
    for name in sorted(magazines.keys()):
        data = magazines[name]
        print(f"Назва: {name}, Ціна: {data['ціна']} грн, Тираж: {data['тираж']} прим.")
    print()


def average_price_under_10000(magazines):
    """Обчислити середню ціну журналів з тиражем < 10000"""
    filtered = [data["ціна"] for data in magazines.values() if data["тираж"] < 10000]
    if not filtered:
        print("Немає журналів з тиражем менше 10 000 примірників.\n")
    else:
        avg_price = sum(filtered) / len(filtered)
        print(f"Середня ціна журналів з тиражем < 10 000: {avg_price:.2f} грн\n")


def main():
    # Початкові дані
    magazines = {
        "Наука і життя": {"ціна": 85.0, "тираж": 9500},
        "Мандрівник": {"ціна": 60.5, "тираж": 12000},
        "Світ природи": {"ціна": 78.2, "тираж": 8000},
        "IT Сьогодні": {"ціна": 95.3, "тираж": 15000},
        "Кулінарія+": {"ціна": 50.0, "тираж": 7000}
    }

    while True:
        print("МЕНЮ:")
        print("1 - Показати всі журнали")
        print("2 - Додати журнал")
        print("3 - Видалити журнал")
        print("4 - Показати журнали у відсортованому порядку")
        print("5 - Знайти середню ціну журналів з тиражем < 10 000")
        print("0 - Вихід")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            print_magazines(magazines)
        elif choice == "2":
            add_magazine(magazines)
        elif choice == "3":
            delete_magazine(magazines)
        elif choice == "4":
            print_sorted(magazines)
        elif choice == "5":
            average_price_under_10000(magazines)
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.\n")


# Запуск програми
if __name__ == "__main__":
    main()
