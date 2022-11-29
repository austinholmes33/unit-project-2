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

