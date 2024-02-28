# 1 Задання значень змінним
var_int = 10
var_float = 8.4
var_str = "No"

# 2 Збільшення значення var_int в 3.5 рази і зв'язування результату з big_int
big_int = var_int * 3.5

# 3 Зменшення значення var_float на одиницю
var_float -= 1

# 4 Розділення var_int на var_float і big_int на var_float
result1 = var_int / var_float
result2 = big_int / var_float
print("Результат розділення var_int на var_float:", result1)
print("Результат розділення big_int на var_float:", result2)

# 5 Зміна значення var_str
var_str = var_str * 2 + "Yes" * 3
print("Нове значення змінної var_str:", var_str)

# 6 Виведіть значення всіх змінних. Використовуючи тільки основи і процедурне програмування
import math

# Введення значень змінних a, b, c, d
a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
c = float(input("Введіть значення c: "))
d = float(input("Введіть значення d: "))

# Обчислення виразу за формулою
Z = (a * math.sqrt(b) - c * math.sqrt(d)) ** 2 * (5.6 / (a + b + c))

# Виведення результату
print("Значення Z:", Z)
