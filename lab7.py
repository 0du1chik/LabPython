import re

# Функція для відкриття файлу з обробкою помилок
def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except Exception as e:
        print(f"File {file_name} wasn't opened! Error: {e}")
        return None
    else:
        print(f"File {file_name} was opened!")
        return file

# Імена файлів
file1_name = "TF14_1.txt"
file2_name = "TF14_2.txt"

# a) Створення текстового файлу TF14_1 із рядків різної довжини
file_1_w = Open(file1_name, "w")
if file_1_w:
    file_1_w.write("Order number 407 includes 1.5 kg of apples and 2 bottles of juice.\n")
    file_1_w.write("The train speed reached 108.25 km/h before the stop.\n")
    file_1_w.write("Today's temperature ranges from -5.2 to 10.8 degrees Celsius.\n")
    file_1_w.write("Your total payment is 263.68 dollars, discount 19.99 percent.\n")
    print(f"Information was successfully added to {file1_name}!")
    file_1_w.close()
    print(f"File {file1_name} was closed!")
# b) Зчитування TF14_1, пошук усіх дійсних чисел і запис у TF14_2
file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r and file_2_w:
    content = file_2_r.read()
    # регулярний вираз для дійсних чисел (з можливим знаком)
    numbers = re.findall(r'[-+]?\d*\.\d+|\d+', content)
    file_2_w.write(" ".join(numbers))
    file_2_r.close()
    file_2_w.close()
    print("Numbers were extracted and written to TF14_2.txt")
    print("Files were closed!")

# c) Зчитування TF14_2 та знаходження найбільшого числа
file_3_r = Open(file2_name, "r")
if file_3_r:
    numbers_list = [float(num) for num in file_3_r.read().split()]
    if numbers_list:
        max_value = max(numbers_list)
        print("Numbers found:", numbers_list)
        print("Maximum number:", max_value)
    else:
        print("No numbers found in the file.")
    file_3_r.close()
    print(f"File {file2_name} was closed!")
