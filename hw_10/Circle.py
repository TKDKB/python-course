class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle:  # в этот класс добавлен атрибут "центр", чтобы была хотя бы какая-то логика, откуда взять точку
    PI = 3.14

    def __init__(self, radius: int | float, center: Point):
        self.radius = radius
        self.center = center

    def area(self) -> int | float:

        return self.PI * self.radius**2

    def subtraction(self, other):
        """
        центром результирующей окружности будет центр большей окружности,
        либо той, что передана первой, если они равны
        """
        new_radius = abs(self.radius - other.radius)
        if self.radius < other.radius:
            new_center = other.center
        elif self.radius > other.radius:
            new_center = self.center
        else:
            new_center = self.center
        if new_radius != 0:
            return Circle(new_radius, new_center)
        else:
            return Point(new_center.x, new_center.y)

    def print(self):
        print("О")


circle_1 = Circle(3, Point(1, 1))
circle_2 = Circle(3, Point(3, -6))

result = circle_1.subtraction(circle_2)
if type(result) == Circle:
    print(f"Радиус результирующей окружности: {result.radius}")
    print(f"Координаты центра результирующей окружности: x - {result.center.x}, y - {result.center.y}")
else:
    print(f"Координаты точки: x - {result.x}, y - {result.y}")

