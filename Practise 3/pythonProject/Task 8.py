# 8) Підрахувати кількість додатних серед чисел а, b, с (ввести з клавіатури).

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))

positive_count = sum(1 for num in [a, b, c] if num > 0)
print("Кількість додатних чисел:", positive_count)
