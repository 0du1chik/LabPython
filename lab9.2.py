import json
def Print(data):
    for name in data:
        print(f"Журнал: {name}, Ціна: {data[name]['price']}, Тираж: {data[name]['copies']}")
def Add(data, name, price, copies):
    if name in data:
        data[name]["price"] = price
        data[name]["copies"] = copies
        print(f"Оновлено запис: {name}: Ціна={price}, Тираж={copies}")
    else:
        data[name] = {"price": price, "copies": copies}
        print(f"Додано новий журнал: {name}")
def Delete(data, name):
    if name in data:
        removed = data[name]
        del data[name]
        print(f"Видалено журнал {name}: Ціна={removed['price']}, Тираж={removed['copies']}")
    else:
        print("Журнал не знайдено.")
def Search(data, field, value):
    print("\nРезультати пошуку:")
    found = False
    for name, info in data.items():
        if field == "name" and name == value:
            print(name, info)
            found = True
        elif field in info and str(info[field]) == str(value):
            print(name, info)
            found = True
    if not found:
        print("Нічого не знайдено.")
def Average_price_small_copies(data):  
    total = 0
    count = 0
    for name in data:
        if data[name]["copies"] < 10000:
            total += data[name]["price"]
            count += 1
    if count == 0:
        return 0
    return total / count
def Open_File(filename, mode):
    try:
        return open(filename, mode, encoding="utf-8")
    except:
        print("Помилка відкриття файлу.")
        return None
journals = {
    "Наука і Техніка": {"price": 50, "copies": 8000},
    "Мандрівник": {"price": 45, "copies": 12000},
    "IT-Світ": {"price": 60, "copies": 9000},
    "Здоров’я": {"price": 40, "copies": 15000},
    "Історик": {"price": 55, "copies": 7000}
}
def main():
    # початковий запис файлу
    json_data = json.dumps(journals, ensure_ascii=False)
    file = Open_File("Journals.json", "w")
    file.write(json_data)
    file.close()
    while True:
        print("\nОберіть дію:")
        print("1 - Вивести JSON на екран")
        print("2 - Додати або оновити журнал")
        print("3 - Видалити журнал")
        print("4 - Пошук за полем")
        print("5 - Середня ціна журналів з тиражем < 10000")
        print("6 - Вийти")
        try:
            choice = int(input("Ваш вибір: "))
        except ValueError:
            print("Помилкове значення.")
            continue
        if choice == 1:
            f = Open_File("Journals.json", "r")
            data = json.loads(f.read())
            f.close()
            Print(data)
        elif choice == 2:
            f = Open_File("Journals.json", "r")
            data = json.loads(f.read())
            f.close()
            name = input("Назва журналу: ")
            try:
                price = int(input("Ціна: "))
                copies = int(input("Тираж: "))
            except ValueError:
                print("Помилка: потрібно вводити числа.")
                continue
            Add(data, name, price, copies)
            f = Open_File("Journals.json", "w")
            f.write(json.dumps(data, ensure_ascii=False))
            f.close()
        elif choice == 3:
            f = Open_File("Journals.json", "r")
            data = json.loads(f.read())
            f.close()
            name = input("Назва журналу для видалення: ")
            Delete(data, name)
            f = Open_File("Journals.json", "w")
            f.write(json.dumps(data, ensure_ascii=False))
            f.close()
        elif choice == 4:
            f = Open_File("Journals.json", "r")
            data = json.loads(f.read())
            f.close()
            print("Можливі поля: name, price, copies")
            field = input("Введіть поле: ")
            value = input("Введіть значення: ")
            Search(data, field, value)
        elif choice == 5:
            f = Open_File("Journals.json", "r")
            data = json.loads(f.read())
            f.close()
            avg = Average_price_small_copies(data)
            print(f"Середня ціна журналів з тиражем < 10000: {avg}")
            f = Open_File("Result.json", "w")
            f.write(json.dumps({"average_price": avg}, ensure_ascii=False))
            f.close()
        elif choice == 6:
            print("Вихід...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
main()