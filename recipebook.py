'''
This file includes the 
'''
import json
import os

from definitions import Method
from enum import Enum
from recipe import Recipe
from ingredient import Ingredient

class Paths(Enum):
    PATH_BACKUP = './data/recipes_backup.json'
    PATH_STORAGE = './data/recipes.json'

class RecipeBook():    
    def __init__(self):
        self.recipies = []
        self.file = open(os.path.join(Paths.PATH_STORAGE.value))
        self.backup = open(os.path.join(Paths.PATH_STORAGE.value))

    #saves the recipies to file in json format
    def save(self):
        json.dump(self.recipies, self.file, indent=4)

    #loads the json file and parses the necessary values to separate classes
    #path must always be relative as we utilise the os.path
    def load(self, path=None):
        if not path:
            data = json.load(self.file)
        else:
            data = json.load(open(os.path.join(path)))

        #wrap the data into a list, so it works
        if not isinstance(data, list):
            data = [data]

        #handle the data here
        for sub in data:
            recipe = Recipe()
            recipe.instructions = sub['instructions']
            recipe.name = sub['name']

            #add the ingredients to the recipe
            for ingredient in sub['ingredients']:
                ing = Ingredient()

                ing.type = ingredient['name']
                ing.amount = ingredient['amount']
                ing.unit = ingredient['unit']

                recipe.add(ing)

            self.recipies.append(recipe)
        

    #adds a recipe and if backup is set then backups the current file before doing so
    def add(self, recipe, backup):
        if backup:
            json.dump(self.recipies, self.backup, indent=4)

        self.recipies.append(recipe)
        self.save()

    #removes a recipe either using a value or a index depending on the given enum method
    #also backsup the file if the backup is set
    def remove(self, method, recipe, backup=False):
        if method == Method.METHOD_INDEX:
            del self.recipies[recipe]
        else:
            self.recipies.remove(recipe)

        if backup:
            json.dump(self.recipies, self.backup, indent=4)

    def search(self, what, value):
        result = []

        for recipe in self.recipies:

            #check if the value exists in the ingredients in the recipe by utilising
            if what == 'ingredient' and (value.lower() in [ingredient.type.lower() for ingredient in recipe.ingredients]):
                result.append(recipe.json())

        return result

if (__name__ == '__main__'):
    book = RecipeBook()
    book.load()

