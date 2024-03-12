#5. На площині ХОY задана своїми координатами точка А (координати ввести з клавіатури). Вказати, де вона розташована (на якій осі або в якому координатном куті).

x_coordinate, y_coordinate = map(float, input("Введіть координати точки A (x, y): ").split())

if x_coordinate == 0 and y_coordinate == 0:
   print("Точка розташована в початку координат.")
elif x_coordinate == 0:
   print("Точка розташована на осі Y.")
elif y_coordinate == 0:
   print("Точка розташована на осі X.")
elif x_coordinate > 0 and y_coordinate > 0:
   print("Точка розташована в першому квадранті.")
elif x_coordinate < 0 and y_coordinate > 0:
   print("Точка розташована в другому квадранті.")
elif x_coordinate < 0 and y_coordinate < 0:
   print("Точка розташована в третьому квадранті.")
else:
   print("Точка розташована в четвертому квадранті.")
