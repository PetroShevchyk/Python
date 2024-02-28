# 1. Присвоєння значень двом змінним
num1 = 10
num2 = -5

# 2. Складання чотирьох складних логічних виразів з використанням оператора and
logical_and_exp1 = (num1 > 0) and (num2 < 0)  # True and True
logical_and_exp2 = (num1 > 0) and (num2 > 0)  # True and False
logical_and_exp3 = (num1 < 0) and (num2 > 0)  # False and False
logical_and_exp4 = (num1 < 0) and (num2 < 0)  # False and True

# 3. Складання чотирьох складних логічних виразів з використанням оператора or
logical_or_exp1 = (num1 > 0) or (num2 < 0)  # True or True
logical_or_exp2 = (num1 > 0) or (num2 > 0)  # True or False
logical_or_exp3 = (num1 < 0) or (num2 > 0)  # False or True
logical_or_exp4 = (num1 < 0) or (num2 < 0)  # False or False

# 4. Робота зі змінними рядкового типу в логічних виразах
str1 = "hello"
str2 = "world"
logical_str_exp1 = (str1 == "hello") and (str2 != "world")
logical_str_exp2 = (str1 == "hello") or (str2 == "world")

# 5. Виведення спеціального повідомлення в залежності від значення змінної
if num1 > 0:
    print("Значення num1 більше за 0")
else:
    print("Значення num1 менше або дорівнює 0")

# 6. Виведення 1 або -1 в залежності від значення змінної
if num1 > 0:
    print(1)
else:
    print(-1)

# 7. Програмний код за вказаним описом
if num1 > num2:
    num3 = num1 - num2
elif num1 < num2:
    num3 = num1 + num2
else:
    num3 = num1

print("Значення третьої змінної:", num3)

# 8. Визначити до якої пори року відноситься і як називається місяць, номер якого ввів користувач.
# Введення номеру місяця
month_number = int(input("Введіть номер місяця (1-12): "))

# Перевірка номера місяця і визначення пори року
if 1 <= month_number <= 2 or month_number == 12:
    season = "зима"
elif 3 <= month_number <= 5:
    season = "весна"
elif 6 <= month_number <= 8:
    season = "літо"
elif 9 <= month_number <= 11:
    season = "осінь"
else:
    season = "невідома"

# Виведення результату
if season != "невідома":
    print(f"Місяць з номером {month_number} відноситься до пори року {season}.")
else:
    print("Неправильний номер місяця. Введіть число від 1 до 12.")

# 9. a) Cкрипт на Python, який виводить ряд чисел Фібоначчі від п'ятого до двадцятого члену
# Визначення початкових членів ряду Фібоначчі
fibonacci = [0, 1]

# Додавання наступних членів ряду Фібоначчі до списку
while len(fibonacci) < 20:
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)

# Виведення ряду Фібоначчі від п'ятого до двадцятого члену
print("Ряд чисел Фібоначчі від п'ятого до двадцятого члену:")
print(fibonacci[4:])  # Виводимо елементи списку, починаючи з індексу 4

# b) Цикл, який виводить ряд парних чисел від 0 до 20, а потім кожне третє число в ряді від -1 до -21
# Виведення ряду парних чисел від 0 до 20
print("Ряд парних чисел від 0 до 20:")
number = 0
while number <= 20:
    print(number, end=" ")
    number += 2

# Перехід до нового ряду
print("\n")

# Виведення кожного третього числа в ряді від -1 до -21
print("Кожне третє число від -1 до -21:")
number = -1
count = 0
while number >= -21:
    print(number, end=" ")
    number -= 3

# 10. Дано натуральне число n (яке також може бути нуль). Обчислити n!
# Введення числа n
n = int(input("Введіть натуральне число n: "))

# Ініціалізація змінної для зберігання результату
factorial = 1

# Обчислення факторіалу числа n
for i in range(1, n + 1):
    factorial *= i

# Виведення результату
print(f"Факторіал числа {n} = {factorial}")

