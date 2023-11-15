from dataclasses import dataclass
from abc import ABC, abstractmethod

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

@dataclass
class Product:
    id: int
    name: str
    price: float