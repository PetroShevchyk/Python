# 10) Визначити, дільником яких чисел а, b, с є число k (ввести з клавіатури).

a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))
k = float(input("Введіть число k (дільник): "))

divisible_by_k = [num for num in [a, b, c] if num % k == 0]
print(f"Числа {a}, {b}, {c} діляться на {k}: {divisible_by_k}")
