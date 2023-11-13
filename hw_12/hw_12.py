from dataclasses import dataclass
from abc import ABC, abstractmethod

class NonProductError(ValueError):
    pass

@dataclass
class Product:
    id: int
    name: str
    price: float

@dataclass
class Pizza(Product):
    ingredients: list[str]
    spicy_status: bool
    diameter: int

@dataclass
class Coffee(Product):
    volume: float
    type: str

class AbstractShop(ABC):
    @abstractmethod
    def add_product(self):
        pass

    @abstractmethod
    def sell_product(self):
        pass

    @abstractmethod
    def all_products(self):
        pass

class RealShop(AbstractShop):
    def __init__(self, product_list: list[Product]):
        self.product_list = product_list

    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            self.product_list.append(new_product)
        else:
            raise NonProductError("переданный объект не является продуктом!")

    def sell_product(self, target_product: Product):
        if isinstance(target_product, Product):
            if target_product in self.product_list:
                self.product_list.remove(target_product)
            else:
                print("такого нет!")
        else:
            raise NonProductError("переданный объект не является продуктом!")

    def all_products(self):
        result = ""
        for el in self.product_list:
            result += f"{el}\n{'-' * 100}\n"
        return result

@dataclass
class Furniture(Product):
    pass

@dataclass
class Sofa(Furniture):
    type: str
    width: int
    height: int
    length: int

class FurnitureShop(AbstractShop):
    def __init__(self, product_list: list[Furniture]):
        self.product_list = product_list

    def add_product(self, new_product: Furniture):
        if isinstance(new_product, Furniture):
            self.product_list.append(new_product)
        else:
            raise NonProductError("переданный объект не является продуктом!")

    def sell_product(self, target_product: Furniture):
        if isinstance(target_product, Furniture):
            if target_product in self.product_list:
                self.product_list.remove(target_product)
            else:
                print("такого нет!")
        else:
            raise NonProductError("переданный объект не является продуктом!")

    def all_products(self):
        result = ""
        for el in self.product_list:
            result += f"{el}\n{'-' * 100}\n"
        return result


coffee_1 = Coffee(id=1, name="coffe_1", price=5.5, volume=150, type="latte")
coffee_2 = Coffee(id=2, name="coffe_2", price=6.7, volume=200, type="americano")
pizza_1 = Pizza(id=3, name="pizza_1", price=13.90, ingredients=["cheese", "salami"], spicy_status=False, diameter=30)
pizza_2 = Pizza(id=4, name="pizza_2", price=17.79, ingredients=["chedder", "pepper"], spicy_status=True, diameter=23)
pizza_3 = Pizza(id=5, name="pizza_3", price=20, ingredients=["chedder", "pepper"], spicy_status=True, diameter=35)
sofa_1 = Sofa(id=6, name="sofa_1", price=500, type="angle", width=150, length=200, height=50)
sofa_2 = Sofa(id=7, name="sofa_2", price=500, type="angle", width=150, length=200, height=50)
new_shop = RealShop([coffee_1, coffee_2, pizza_1, pizza_2])
print(new_shop.all_products())
new_shop.add_product(pizza_3)
print(new_shop.all_products())
new_shop.sell_product(pizza_3)
print(new_shop.all_products())
new_furniture_shop = FurnitureShop([sofa_1, sofa_2])
new_furniture_shop.all_products()
