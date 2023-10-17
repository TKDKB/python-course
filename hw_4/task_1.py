import math


VOWELS_ALPHABET = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"


def russian_alphabet_generator():
    a = ord('а')
    alphabet = ''.join([chr(i) for i in range(a, a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6, a+32)])
    return alphabet


ALPHABET = russian_alphabet_generator()


def root(value):
    return power(value, 2)


def is_even(value):
    if value % 2 == 0:
        return True
    return False


def factorial(value: int):
    result = 1
    while value > 0:
        result = result * value
        value -= 1
    return result


def reverse(message):
    return ''.join(reversed(message))


def fibonacci(n):
    prev = 1
    cur = 1
    counter = 2
    while counter < n:
        temp = cur
        cur = prev + cur
        prev = temp
        counter += 1
    return cur


def count_vowels(message):
    counter = 0
    for element in message:
        if element in VOWELS_ALPHABET:
            counter += 1
    return counter


def is_palindrome(message):
    if message == ''.join(reversed(message)):
        return True
    return False


def power(x, n):
    result = 1
    for i in range(n):
        result = result * x
    return result


def is_anagram(message_1, message_2):
    if len(message_1) != len(message_2):
        return False
    counter_flag = 0
    for element in message_1:
        if element in message_2:
            counter_flag += 1

    if counter_flag == len(message_1):
        return True

    return False


def is_pangram(message):
    counter = 0
    target = len(ALPHABET)
    for letter in ALPHABET:
        if letter in message or letter.upper() in message:
            counter += 1

    if counter == target:
        return True
    return False


def print_menu():
    print(f"""
        1.  Ф-ция для нахождения квадрата числа
        2.  Ф-ция для проверки числа на чётность
        3.  Ф-ция для вычисления факториала
        4.  Ф-ция для возврата перевёрнутой строки
        5.  Ф-ция для поиска n-ого числа Фибоначчи
        6.  Ф-ция для подсчёта гласных букв в строке
        7.  Ф-ция для проверки является ли строка палиндромом
        8.  Ф-ция для для возведения числа x в степень n
        9.  Ф-ция для проверки являются ли строки анаграммами
        10. Ф-ция для прооверки является ли строка панграммой
        11. Завершить работу
        
    """)


print_menu()

while True:
    print("-" * 100)
    choice = input("Введите свой выбор: ")
    match choice:
        case "1":
            number = int(input("Введите своё число: "))
            print("Квадрат Вашего числа:", root(number))

        case "2":
            number = int(input("Введите своё число: "))
            print("Чётное ли число?", is_even(number))

        case "3":
            number = int(input("Введите своё число: "))
            print("Факториал Вашего числа:", factorial(number))

        case "4":
            message = input("Введите свою строку: ")
            print("Перевёрнутая строка:", reverse(message))

        case "5":
            number = int(input("Введите номер числа Фибоначчи: "))
            print("Число Фибоначчи, стоящее под данным номером:", fibonacci(number))

        case "6":
            message = input("Введите свою строку: ")
            print("Количество гласных букв в строке:", count_vowels(message))

        case "7":
            message = input("Введите свою строку: ")
            print("Является ли строка палиндромом?", is_palindrome(message))

        case "8":
            val = int(input("Введите число для возведения в степень: "))
            pow_val = int(input("Введите степень: "))
            print(f"Число {val} с степени {pow_val} = {power(val, pow_val)}")

        case "9":
            message_1 = input("Введите первую строку: ")
            message_2 = input("Введите вторую строку: ")
            print(f"Являются ли строки \"{message_1}\" и \"{message_2}\" анаграммами? {is_anagram(message_1, message_2)}")

        case "10":
            message = input("Введите свою строку: ")
            print(f"Является ли строка \"{message}\" панграммой? {is_pangram(message)}")

        case "11":
            print("Спасибо за внимание :)")
            break
