#1. Увести з клавіатури три дійсних числа. Піднести до квадрата ті з них, значення яких невід'ємні, і в четверту ступінь - від`ємні .
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

if a >= 0:
   a_squared = a ** 2
else:
   a_squared = a ** 4

if b >= 0:
   b_squared = b ** 2
else:
   b_squared = b ** 4

if c >= 0:
   c_squared = c ** 2
else:
   c_squared = c ** 4

print("Результати підняття до ступеня:")
print("a:", a_squared)
print("b:", b_squared)
print("c:", c_squared)