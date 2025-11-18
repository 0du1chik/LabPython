import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("comptage_velo_2018.csv")
# Перевірка структури DataFrame
print("Перші 5 рядків:\n", df.head(), "\n")
print("Інформація про DataFrame:\n")
df.info()
print("\nОписова статистика:\n", df.describe(), "\n")
# Загальна кількість велосипедистів за рік на всіх велодоріжках
total_cyclists = df.select_dtypes(include=["number", "float", "int"]).sum().sum()
print("Загальна кількість велосипедистів за рік на всіх доріжках:", total_cyclists)
# Загальна кількість велосипедистів на кожній доріжці
sum_per_path = df.select_dtypes(include=["number", "float", "int"]).sum()
print("\nКількість велосипедистів за рік на кожній велодоріжці:\n", sum_per_path)
# Визначення трьох довільних велодоріжок (перші три числові колонки)
numeric_cols = df.select_dtypes(include=["number", "float", "int"]).columns[:3]
# Перетворення стовпця дати, якщо є
if "Date" in df.columns or "date" in df.columns:
    date_col = "Date" if "Date" in df.columns else "date"
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df["Місяць"] = df[date_col].dt.month
else:
    df["Місяць"] = range(1, len(df) + 1)
# Визначення найпопулярнішого місяця для кожної з 3 доріжок
print("\nНайпопулярніші місяці на трьох вибраних велодоріжках:")
for col in numeric_cols:
    popular_month = df.groupby("Місяць")[col].sum().idxmax()
    print(f"{col}: місяць {popular_month}")
# Побудова графіка для однієї велодоріжки (першої)
path_to_plot = numeric_cols[0]
monthly_data = df.groupby("Місяць")[path_to_plot].sum()
plt.figure(figsize=(8,5))
plt.plot(monthly_data.index, monthly_data.values, marker='o')
plt.title(f"Завантаженість велодоріжки '{path_to_plot}' по місяцях (2018)")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.grid(True)
plt.show()