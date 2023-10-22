

def make_sentence(words=["This", "is", "a", "sentence"]) ->str:
    result = " ".join(words)
    return result + "."


def sum_of_squares(*args: int) ->int:
    result = 0
    if len(args) == 0:
        return 0
    for number in args:
        result += pow(number, 2)
    return result


def greet(name: str, language="en"):
    if language == "en":
        print(f"hello, {name}")
    elif language == "ru":
        print(f"привет, {name}")
    elif language == "fr":
        print(f"bonjour, {name}")
    else:
        print("неверный выбор языка")


def print_info(**kwargs):
    if not kwargs:
        print("No info given")
        return
    for key in kwargs.keys():
        print(f"{key}: {kwargs[key]}")


def print_table(**kwargs):
    if len(kwargs) == 0:
        print("No data given.")
        return
    print(f"|{'Key':<10}|{'Value':<10}|")
    print("-" * 23)
    for key, value in kwargs.items():
        print(f"|{key:<10}|{value:<10}|")


def calculate(*args: int, operation):
    if not args:
        return 0
    if operation == "+":
        print(sum(args))
    elif operation == "-":
        result = args[0]
        if len(args) == 1:
            print(result)
            return
        for element in args[1:]:
            result -= element
        print(result)
    elif operation == "*":
        result = 1
        for element in args:
            result *= element
        print(result)
    elif operation == "/":
        result = 1
        if len(args) == 1:
            print(result)
            return
        for element in args[1:]:
            result /= element
        print(result)


def print_triangle(height=5):
    amount = 1
    for index in range(height):
        print(f"{'*' * amount:^{height * 2}}")
        amount += 2


def create_post(title, text, author, categorie="general"):
    post = {
        "title": title,
        "text": text,
        "author": author,
        "categorie": categorie
    }
    return post


def create_product(title, price, categorie, rating=0):
    product = {
        "title": title,
        "price": price,
        "categorire": categorie,
        "rating": rating
    }
    return product



def create_student(name, last_name, patronymic, group, admission_date=None, average_grade=None, semester=None, phone_number=None, address=None):
    student = {}
    student["Имя"] = name
    student["Фамилия"] = last_name
    student["Отчество"] = patronymic
    student["Группа"] = group

    if admission_date is not None:
        if not admission_date[0:1].isdigit() or not admission_date[3:4].isdigit() or not admission_date[6:10].isdigit() or admission_date[2] != "." or admission_date[5] != "." or len(admission_date) != 10:
            print("дата не соответствует формату!")
        else:
            student["Дата поступления"] = admission_date
    if average_grade is not None:
        student["Средний бал"] = average_grade
    if semester is not None:
        student["Семестр обучения"] = semester
    if phone_number is not None:
        student["Номер телефона"] = phone_number
    if address is not None:
        student["Адрес"] = address

    return student


def print_menu():
    print(f"""
        1.  Ф-ция для составления предложения из списка строк
        2.  Ф-ция для нахождения суммы квадратов чисел
        3.  Ф-ция для вывода приветствия на выбранном языке
        4.  Ф-ция для вывода информации в формате ключ: значение
        5.  Ф-ция для вывода таблицы в формате ключ: значение
        6.  Ф-ция для проведения арифметической операции
        7.  Ф-ция для вывода пирамидки из звёздочек
        8.  Ф-ция для создания поста для блога
        9.  Ф-ция для создания структуры товара
        10. Ф-ция для создания профиля студента
        11. Завершить работу

    """)


print_menu()

while True:
    print("-" * 100)
    choice = input("Введите свой выбор: ")
    match choice:
        case "1":
            print(make_sentence())

        case "2":
            print(sum_of_squares())

        case "3":
            greet("anna")

        case "4":
            print_info()

        case "5":
            print_table()

        case "6":
            print(calculate(operation="+"))

        case "7":
            print_triangle()

        case "8":
            print(create_post("new post", "hello, this is my new post", "Me"))

        case "9":
            print(create_product("krasnyi chainik", "50 bucks", "chainiki"))

        case "10":
            print(create_student("victor", "tsoi", "robertovich", "gruppa krovi ;)"))

        case "11":
            print("Спасибо за внимание :)")
            break

