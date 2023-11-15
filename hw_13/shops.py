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
    def add_product(self, object: Product):
        pass

    @abstractmethod
    def sell_product(self, object: Product):
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

    def all_products(self) -> list[Product]:
        return self.product_list

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

    def all_products(self) -> list[Furniture]:
        return self.product_list

@dataclass
class Literature(Product):
    author: str
    publishinп_house: str

@dataclass
class Book(Literature):
    pass

@dataclass
class Magazine(Literature):
    pass


class BookShop(AbstractShop):
    def __init__(self, product_list: list[Literature]):
        self.product_list = product_list

    def add_product(self, new_product: Literature):
        if isinstance(new_product, Literature):
            self.product_list.append(new_product)
        else:
            raise NonProductError("переданный объект не является продуктом!")

    def sell_product(self, target_product: Literature):
        if isinstance(target_product, Literature):
            if target_product in self.product_list:
                self.product_list.remove(target_product)
            else:
                print("такого нет!")
        else:
            raise NonProductError("переданный объект не является продуктом!")

    def all_products(self) -> list[Literature]:
        return self.product_list



@dataclass
class ComputerHardware(Product):
    type: str

@dataclass
class Motherboard(ComputerHardware):
    pass

@dataclass
class VideoCard(ComputerHardware):
    pass

class ComputerHardwareShop(AbstractShop):
    def __init__(self, product_list: list[ComputerHardware]):
        self.product_list = product_list

    def add_product(self, new_product: ComputerHardware):
        if isinstance(new_product, ComputerHardware):
            self.product_list.append(new_product)
        else:
            raise NonProductError("переданный объект не является продуктом!")

    def sell_product(self, target_product: ComputerHardware):
        if isinstance(target_product, ComputerHardware):
            if target_product in self.product_list:
                self.product_list.remove(target_product)
            else:
                print("такого нет!")
        else:
            raise NonProductError("переданный объект не является продуктом!")

    def all_products(self) -> list[ComputerHardware]:
        return self.product_list