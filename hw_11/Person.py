class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self. gender = gender

    def str(self):
        return f"Имя: {name}, Возраст: {age}, Пол: {gender}"

    def get_name(self):
        return self.name

    @property
    def set_name(self, new_name: str):
        self.name = new_name

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False

    @classmethod
    def create_from_string(cls, string):
        obj_list = string.split("-")
        return cls(obj_list[0], obj_list[1], obj_list[2])
