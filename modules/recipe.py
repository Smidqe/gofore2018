from enum import Enum
from definitions import Method

class Ingredient():
    def __init__(self):
        self.type = ''
        self.unit = ''
        self.amount = 0

class Recipe():
    def __init__(self):
        self.name = ''
        self.ingredients = []
        self.instructions = ''

    def get(self, method, ingredient):
        result = None

        if method == Method.METHOD_INDEX:
            result = self.ingredients[ingredient]
        else:
            result = self.ingredients[self.ingredients.index(ingredient)]

        return result

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def remove(self, method, ingredient):
        if (self.ingredients.count() == 0):
            return

        if method == Method.METHOD_INDEX:
            del self.ingredients[ingredient]
        else:
            self.ingredients.remove(ingredient)

    def modify(self, index, value):
        self.ingredients[index] = value

    def json(self):
        #grab the ingredients as a json compatible list
        ings = [ing.__dict__ for ing in self.ingredients]

        #create the json object
        result = {'name': self.name, 'ingredients': ings, 'instructions': self.instructions}
        
        return result