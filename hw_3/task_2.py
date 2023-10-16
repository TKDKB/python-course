print("-" * 100)
print("Задание 1")
print("-" * 100)
input_string = input("Введите список чисел через пробел: ")
input_list = input_string.split()
index = 0
sum = 0
while index < len(input_list):
    sum += int(input_list[index])
    index += 1

print("Сумма элементов списка: ", sum)
print("=" * 100)


print("-" * 100)
print("Задание 2")
print("-" * 100)
lowercase_alphabet = "аеиоуыэюя"
vowel_alphabet = lowercase_alphabet + lowercase_alphabet.upper()
input_string = input("Введите вашу строку: ")
index = 0
vowel_amount = 0
while index < len(input_string):
    if input_string[index] in vowel_alphabet:
        vowel_amount += 1
    index += 1
print("Количество гласных букв: ", vowel_amount)
print("=" * 100)


print("-" * 100)
print("Задание 3")
print("-" * 100)
input_string = input("Введите список слов через пробел: ")
input_list = input_string.split()
print("Самая длинная строка: ", max(input_list))
print("=" * 100)


print("-" * 100)
print("Задание 4")
print("-" * 100)
input_string = input("Введите список чисел через пробел: ")
input_list = input_string.split()
index = 0
while index < len(input_list):
    input_list[index] = int(input_list[index])
    index += 1

index = 0
while index < len(input_list):
    if input_list[index] % 2 == 0:
        input_list[index] = input_list[index] * 2
    index += 1

print("Итоговый список: ", input_list)
print("=" * 100)


print("-" * 100)
print("Задание 5")
print("-" * 100)
input_string = input("Введите список чисел через пробел: ")
input_list = input_string.split()
input_list_copy = sorted(input_list)
print(f"""
    Минимальный элемент: {input_list_copy[0]}
    Индекс минимального элемента: {input_list.index(input_list_copy[0])}
""")
print("=" * 100)


print("-" * 100)
print("Задание 6")
print("-" * 100)
input_string = input("Введите список слов через пробел: ")
input_list = input_string.split()
print("Перевёрнутая строка: ", " ".join(list(reversed(input_list))))
print("=" * 100)


