from dataclasses import dataclass
from Abstractions import Product

@dataclass
class Pizza(Product):
    ingredients: list[str]
    spicy_status: bool
    diameter: int

@dataclass
class Coffee(Product):
    volume: float
    type: str

@dataclass
class Furniture(Product):
    pass

@dataclass
class Sofa(Furniture):
    type: str
    width: int
    height: int
    length: int

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

@dataclass
class ComputerHardware(Product):
    type: str

@dataclass
class Motherboard(ComputerHardware):
    pass

@dataclass
class VideoCard(ComputerHardware):
    pass
