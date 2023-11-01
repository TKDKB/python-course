import time


class Auto:
    brand: str
    age: int
    color: str
    mark: str

    def __init__(self, brand: str, age: int, mark: str):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


class Truck(Auto):
    max_load: int
    def __init__(self, brand: str, age: int, mark: str, max_load: int):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    max_speed: int

    def __init__(self, brand: str, age: int, mark: str, max_speed: int):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("max speed is", self.max_speed)


truck_1 = Truck("RAM", 10, "2203", 1000)
truck_2 = Truck("Chevrolet", 15, "331", 1500)

car_1 = Car("BMW", 5, "M4", 300)
car_2 = Car("Mercedes", 1, "G63", 220)

print("=" * 100)
print("Truck 1")
print(f"""
brand: {truck_1.brand}
age: {truck_1.age}
mark: {truck_1.mark}
max_load: {truck_1.max_load}
""")

print("-" * 100)
truck_1.move()
print("-" * 100)
truck_1.stop()
print("-" * 100)
truck_1.load()
print("-" * 100)
truck_1.birthday()
print("new age: ", truck_1.age)

print("\n" + "=" * 100)
print("Truck 2")
print(f"""
brand: {truck_2.brand}
age: {truck_2.age}
mark: {truck_2.mark}
max_load: {truck_2.max_load}
""")

print("-" * 100)
truck_2.move()
print("-" * 100)
truck_2.stop()
print("-" * 100)
truck_2.load()
print("-" * 100)
truck_2.birthday()
print("new age: ", truck_2.age)

print("\n" + "=" * 100)
print("Car 1")
print(f"""
brand: {car_1.brand}
age: {car_1.age}
mark: {car_1.mark}
max_load: {car_1.max_speed}
""")

print("-" * 100)
car_1.move()
print("-" * 100)
car_1.stop()
print("-" * 100)
car_1.birthday()
print("new age: ", car_1.age)

print("\n" + "=" * 100)
print("Car 2")
print(f"""
brand: {car_2.brand}
age: {car_2.age}
mark: {car_2.mark}
max_load: {car_2.max_speed}
""")

print("-" * 100)
car_2.move()
print("-" * 100)
car_2.stop()
print("-" * 100)
car_2.birthday()
print("new age: ", car_2.age)

