from Abstractions import AbstractShop, Product
from Products import Furniture, Literature, ComputerHardware

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