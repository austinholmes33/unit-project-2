from abc import ABC, abstractmethod
from pprint import pprint

def read_csv(file):
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)
read_csv("sample.csv")



class Cupcake:
    size = "regular"
    def __init__(self, name, cake, frosting, filling, price):
        self.name = name
        self.cake = cake
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
        self.price = price

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    def calculate_price(self, quantity):
        return quantity * self.price

# instantiation
triple_chocolate = Cupcake('triple chocolate', 'chocolate', 'chocolate', 'chocolate', 2.75)

cookies_and_cream = Cupcake('cookies and cream', 'chocolate', 'vanilla', 'oreo', 2.99)

cookies_and_cream.frosting = 'chocolate'
cookies_and_cream.filling = 'vanilla'

cookies_and_cream.add_sprinkles('oreo crumbs', 'vanilla')

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, cake, frosting, price):
        self.name = name
        self.cake = cake
        self.frosting = frosting
        self.price = price
        self.sprinkles = []

mini_chocolate = Mini('mini chocolate', 'chocolate', 'vanilla', 1.99)

cupcake_list = [
    triple_chocolate,
    cookies_and_cream
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

write_new_csv("sample.csv", cupcake_list)

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "cake", "frosting", "filling", "price", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "cake": cupcake.cake, "frosting": cupcake.frosting, "filling": cupcake.filling, "price": cupcake.price, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "cake": cupcake.cake, "frosting": cupcake.frosting, "price": cupcake.price, "sprinkles": cupcake.sprinkles})