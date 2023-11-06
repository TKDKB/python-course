class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        print(f"{self.__kg} кг = {self.__kg * 2.205} фунтов")

    def set_kg(self, new_kg: int):
        if isinstance(new_kg, int) and new_kg >= 0:
            self.__kg = new_kg
        else:
            print("Wrong value.")

    def get_kg(self):
        print(f"{self.__kg} кг")


new_1 = KgToPounds(12)
new_1.get_kg()
new_1.set_kg(15)
new_1.get_kg()
new_1.to_pounds()
print("=" * 100)

class KgToPoundsVersion2:
    def __init__(self, kg):
        self._kg = kg

    def to_pounds(self):
        print(f"{self._kg} кг = {self._kg * 2.205} фунтов")

    @property
    def set_kg(self, new_kg: int):
        if isinstance(new_kg, int) and new_kg >= 0:
            self._kg = new_kg
        else:
            print("Wrong value.")

    @property
    def get_kg(self):
        return self._kg


new_2 = KgToPoundsVersion2(12)
print(new_2.get_kg)
new_2._kg = 2
print(new_2.get_kg)
new_2.to_pounds()

