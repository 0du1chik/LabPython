import csv

input_file = "Data_fixed.csv"
output_file = "result.csv"
try:
    with open(input_file, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")

        print("=== Вміст файлу ===")
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"Файл {input_file} не знайдено!")
    exit()
try:
    with open(input_file, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")
        year_col = "2019 [YR2019]"
        data_2019 = {
            row["Country Name"]: row[year_col]
            for row in reader
            if row[year_col] != ""
        }
        print("\nВведіть назви країн (через кому):")
        countries_input = input().split(",")
        countries = [c.strip() for c in countries_input]
        results = []
        for country in countries:
            value = data_2019.get(country, "Немає даних")
            results.append([country, value])
        with open(output_file, "w", newline="", encoding="utf-8") as f_out:
            writer = csv.writer(f_out, delimiter=";")
            writer.writerow(["Country", "Life expectancy 2019"])
            writer.writerows(results)
        print(f"\nДані успішно записано у файл {output_file}")
except FileNotFoundError:
    print(f"Не вдалося відкрити файл {input_file}")