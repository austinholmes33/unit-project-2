from abc import ABC, abstractmethod
from pprint import pprint
import csv

def read_csv(file):
    with open(file, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)
read_csv("sample.csv")



class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, cake, frosting, sprinkles, price):
        self.name = name
        self.cake = cake
        self.frosting = frosting
        self.sprinkles = sprinkles
        self.price = price

    # def add_sprinkles(self, *args):
    #     for sprinkle in args:
    #         self.sprinkles.append(sprinkle)
    
    @ abstractmethod 
    def calculate_price(self, quantity):
        return quantity * self.price

# instantiation
# triple_chocolate = Cupcake('triple chocolate', 'chocolate', 'chocolate', 'chocolate', 2.75)

# cookies_and_cream = Cupcake('cookies and cream', 'chocolate', 'vanilla', 'oreo', 2.99)

# cookies_and_cream.frosting = 'chocolate'
# cookies_and_cream.filling = 'vanilla'

# cookies_and_cream.add_sprinkles('oreo crumbs', 'vanilla')

class Mini(Cupcake):
    size = "Mini"

    def __init__(self, name, cake, frosting, sprinkles, price):
        super().__init__(name, cake, frosting, sprinkles, price)

    # def add_sprinkles(self, *args):
    #     for sprinkle in args:
    #         self.sprinkles.append(sprinkle)

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

class Large(Cupcake):
    size = "Large"

    def __init__(self, name, cake, frosting, filling, sprinkles, price):
        super().__init__(name, cake, frosting, sprinkles, price)
        self.filling = filling

    # def add_sprinkles(self, *args):
    #     for sprinkle in args:
    #         self.sprinkles.append(sprinkle)

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

class Medium(Cupcake):
    size = "Medium"

    def __init__(self, name, cake, frosting, sprinkles, price):
        super().__init__(name, cake, frosting, sprinkles, price)

    # def add_sprinkles(self, *args):
    #     for sprinkle in args:
    #         self.sprinkles.append(sprinkle)

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

mini_chocolate = Mini('mini chocolate', 'chocolate', 'vanilla', 'chocolate', 1.99)

mini_vanilla = Mini("mini vanilla", "vanilla", "vanilla", "chocolate", 1.50)
# mini_vanilla.add_sprinkles("chocolate")

mini_cookies_and_cream = Mini("mini cookies and cream", "chocolate", "vanilla", "oreo", 2.00)
# mini_cookies_and_cream.add_sprinkles("oreo crumbs", "vanilla")

medium_triple_chocolate = Medium("medium triple chocolate", "chocolate", "chocolate", "chocolate", 3.50)

medium_vanilla = Medium("medium vanilla", "vanilla", "chocolate", "vanilla", 3.00)
# medium_vanilla.add_sprinkles("chocolate")

large_red_velvet = Large("large red velvet", "red velvet", "cream cheese", None, "red", 4.50)



cupcake_list = [
    medium_triple_chocolate,
    medium_vanilla,
    mini_cookies_and_cream,
    mini_chocolate,
    mini_vanilla,
    large_red_velvet
]

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "cake", "frosting", "filling", "price", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "cake": cupcake.cake, "frosting": cupcake.frosting, "filling": cupcake.filling, "price": cupcake.price, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "cake": cupcake.cake, "frosting": cupcake.frosting, "price": cupcake.price, "sprinkles": cupcake.sprinkles})

write_new_csv("order.csv", [])
write_new_csv("cupcakes.csv", cupcake_list)

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "cake", "frosting", "filling", "price", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "cake": cupcake.cake, "frosting": cupcake.frosting, "filling": cupcake.filling, "price": cupcake.price, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "cake": cupcake.cake, "frosting": cupcake.frosting, "price": cupcake.price, "sprinkles": cupcake.sprinkles})

# add_cupcake("cupcakes.csv", medium_vanilla)

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, cupcake):
    for cupcake in get_cupcakes(file):
        print(cupcake)
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "cake", "frosting", "sprinkles", "filling", "price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)