import matplotlib.pyplot as plt

# Дані
days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'Пятниця', 'Субота', 'Неділя']
sales = [120, 150, 90, 200, 220, 180, 80]

# Створення графіка
plt.figure(figsize=(10, 6))
plt.plot(days, sales, marker='o', linestyle='-', color='b')
plt.title('Продажі магазину за тиждень')
plt.xlabel('День тижня')
plt.ylabel('Продажі')
plt.grid(True)
plt.show()