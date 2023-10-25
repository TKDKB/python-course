VOWELS_STR = "ёуеыаоэяиюЁУЕЫАОЭЯИЮ"
VOWELS_SET = set(VOWELS_STR)
PYTHON_WORD = "python"


def only_even(values: list[int]) -> list[int]:
    even_list = list(filter(lambda x: x % 2 == 0, values))
    return even_list


def sort_age(primary_list: list[tuple]) -> list[tuple]:
    return sorted(primary_list, key=lambda pair: pair[1])


def vowel_start_str(primary_list: list[str]) -> list[str]:
    vowel_start_list = list(filter(lambda el: el[0] in VOWELS_SET, primary_list))
    return vowel_start_list


def square_list(primary_list: list[int]) -> list[int]:
    result = list(map(lambda number: pow(number, 2), primary_list))
    return result


def reversed_length(primary_list: list[str]) -> list[str]:
    return sorted(primary_list, key=len, reverse=True)


def in_python(primary_string: str) -> list[str]:
    result = list(set(filter(lambda el: el in PYTHON_WORD, primary_string))) # сделал так, чтобы были уникальные буквы, чтобы были все можно убрать set()
    return result


def mult_list(primary_list: list[int]) -> list[int]:
    result = list(map(lambda number: number * 10, primary_list))
    return result


def alphabet_sort(primary_list: list[str]) -> list[str]:
    return sorted(primary_list)


def palindrome(primary_list: list[str]) -> list[str]:
    result = list(filter(lambda el: el == "".join(reversed(el)), primary_list))
    return result


def sort_vowels(primary_list: list[str]) -> list[str]:
    return sorted(primary_list, key=lambda x: sum(map(x.count, VOWELS_SET)))


def upper_str(primary_list: list[str]) -> list[str]:
    result = list(map(lambda el: el.upper(), primary_list))
    return result


def plus_hello(primary_list: list[str]) -> list[str]:
    result = list(map(lambda el: "Hello" + el, primary_list))
    return result


def sort_a(primary_list: list[str]) -> list[str]:
    return sorted(primary_list, key=lambda x: sum(map(x.count, "а")))


def sort_unique(primary_list: list[str]) -> list[str]:
    return sorted(primary_list, key=lambda x: sum(filter(lambda y: y == 1, map(x.count, "а"))))


def decorator(func):
    def wrapper(*args, **kwargs):
        for i in range(1, 6):
            func()
            print("Функция вызвана", i)
    return wrapper


@decorator
def decorated_func():
    print("Hello, user!")


print("-" * 100)
print("task_1")
print(only_even([1, 2, 3, 4, 5, 6]))
print("-" * 100)
print("task_2")
print(sort_age([(1, 2), (1, 3), (1, 1)]))
print("-" * 100)
print("task_3")
print(vowel_start_str(["Аоус", "иаа", "бг"]))
print("-" * 100)
print("task_4")
print(square_list([1, 2, 3, 4]))
print("-" * 100)
print("task_5")
print(reversed_length(["fff", "ffffffffffffff", "s"]))
print("-" * 100)
print("task_6")
print(in_python("aoihfbvsfhvaadjvbsadkf"))
print("-" * 100)
print("task_7")
print(mult_list([1, 2, 3, 4]))
print("-" * 100)
print("task_8")
print(alphabet_sort(["bb", "bc", "a"]))
print("-" * 100)
print("task_9")
print(palindrome(["aaa", "bbac", "dveed"]))
print("-" * 100)
print("task_10")
print(sort_vowels(["ааа", "ддис", "ыфы"]))
print("-" * 100)
print("task_11")
print(upper_str(["ааа", "ддис", "ыфы"]))
print("-" * 100)
print("task_12")
print(plus_hello(["ааа", "ддис", "ыфы"]))
print("-" * 100)
print("task_13")
print(sort_a(["ааа", "ддиас", "ыфы"]))
print("-" * 100)
print("task_14")
print(sort_unique(["ааа", "ддиас", "ыфы"]))
print("-" * 100)
print("task_15")
decorated_func()






