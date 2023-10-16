print("-" * 100)
print("По середине")
print("-" * 100)
greeting = input("Введите приветствие: ")
if len(greeting) > 30:
    print(f"""
        {"=" * 30:^30}
        {greeting[:30]:^30}
        {"=" * 30:^30}
    """)
else:
    print(f"""
            {"=" * 30}
            {greeting:^30}
            {"=" * 30}
        """)
print("=" * 100)


print("-" * 100)
print("Только +")
print("-" * 100)
sum = 0
for index in range(3):
    while True:
        try:
            current_value = int(input(f"Число {index + 1}: "))
            break
        except:
            print("Значение должно быть числом!")
    if current_value > 0:
        sum += current_value
print("Сумма положительных чисел: ", sum)
print("=" * 100)


print("-" * 100)
print("Високосный год")
print("-" * 100)
year = int(input("Введите год: "))
if year % 4 == 0:
    print("Год високосный")
else:
    print("Год не високосный")
print("=" * 100)


print("-" * 100)
print("Ход ладьи")
print("-" * 100)
input_string = input("Введите две клетки шахматной доски через пробел: ")
primary_list = input_string.split(" ")
secondary_list = []
index = 0
while index < len(primary_list):
    secondary_list.append(list(primary_list[index]))
    index += 1
index = 0
while index < len(primary_list):
    secondary_list[index][1] = int(secondary_list[index][1])
    index += 1
if secondary_list[0] == secondary_list[1]:
    print("Клетки одинаковые")
elif secondary_list[0][0] == secondary_list[1][0] or secondary_list[0][1] == secondary_list[1][1]:
    print("Осуществление хода возможно")
else:
    print("Осуществление хода невозможно")

print("=" * 100)




