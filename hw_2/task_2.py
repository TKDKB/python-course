print("Простой Фибоначчи")
print("----------------------------")
fibonachchi = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
choice = int(input("Введите номер числа: "))
print("Число под заданным номером: ", fibonachchi[choice - 1])
print("============================")


print("Выбрать нижний")
print("----------------------------")
choice = int(input("Введите свой выбор: "))
print("Число под заданным номером: ", 1 / (choice + 1))
print("============================")


print("Вычислить длину")
print("----------------------------")
a_coords = input("Точка A, координаты x,y: ")
b_coords = input("Точка B, координаты x,y: ")
a_x, a_y = a_coords.split(",")
b_x, b_y = b_coords.split(",")
distance = ((int(b_x) - int(a_x)) ** 2 + (int(b_y) - int(a_y)) ** 2) ** 0.5
print("Расстояние от точки A до точки В: ", distance)
print("============================")


print("И угол")
print("----------------------------")
a_coords = input("Точка A, координаты x,y: ")
b_coords = input("Точка B, координаты x,y: ")
a_x, a_y = a_coords.split(",")
b_x, b_y = b_coords.split(",")
distance = ((int(b_x) - int(a_x)) ** 2 + (int(b_y) - int(a_y)) ** 2) ** 0.5
print("Расстояние от точки A до точки В: ", distance)
angle = (int(b_y) - int(a_y)) / distance
print("Синус угла: ", angle)
print("============================")


print("Три в ряд")
print("----------------------------")
current = "1 / "
prev = "1 / "
post = "1 / "
n = int(input("Введите число n: "))
current += str(2 ** n)
prev += str(2 ** (n - 1))
post += str(2 ** (n + 1))
print(prev)
print(current)
print(post)
print("============================")
