'''

'''
import json
import os
import argparse

from definitions import Method, Paths
from enum import Enum
from recipe import Recipe, Ingredient

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
            #create the recipe object and add instructions and name
            recipe = Recipe()
            recipe.instructions = sub['instructions']
            recipe.name = sub['name']

            #add the ingredients to the recipe
            for ingredient in sub['ingredients']:
                ing = Ingredient()

                #add necessary values
                ing.type = ingredient['name']
                ing.amount = ingredient['amount']
                ing.unit = ingredient['unit']
                
                #add the ingredient to recipe
                recipe.add(ing)

            #add the recipe to the list
            self.recipies.append(recipe)
        
    '''
        Function:
            add(recipe, backup)
        
        Params:
            - recipe: Recipe
            - backup: boolean
    '''
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

    #search for various things you might find in the recipies
    #currently ingredient search is implemented
    #but it could be easily 
    def search(self, what, value):
        result = []

        #check if there is nothing in the recipies
        if len(self.recipies) == 0:
            return result

        #iterate over the list
        for recipe in self.recipies:
            #check if the value exists in the ingredients in the recipe by utilising some list magic
            #also important that we compare the lowercased strings to allow case typos that grandma may have
            #also when using 'and' we are lazily checking the condition instead of using | which is not lazy
            if what == 'ingredient' and (value.lower() in [ingredient.type.lower() for ingredient in recipe.ingredients]):
                result.append(recipe.json())

        return result

#if we are running this program from console/terminal
if (__name__ == '__main__'):
    book = RecipeBook()
    book.load()

    #add necessary arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--search', help='Search for recipies using an ingredient', type=str, required=True)

    args = parser.parse_args()
    data = book.search('ingredient', args.search)
    
    #show the results, no pretty print
    #TODO: add pretty print
    if len(data) == 0:
        print('No results')
    else:
        print(json.dumps(data, indent=4))


