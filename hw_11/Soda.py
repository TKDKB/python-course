class Soda:
    def __init__(self, topping = None):
        self.topping = topping
    def show_my_drink(self):
        if self.topping:
            print(f"Газировка и {self.topping}")
        else:
            print("Обычная газировка")
