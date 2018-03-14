from enum import Enum

#Method constants
class Method(Enum):
    METHOD_REMOVE = 0
    METHOD_ADD = 1
    METHOD_INDEX = 2
    METHOD_VALUE = 3

#Path constants (relative to main file)
class Paths(Enum):
    PATH_BACKUP = './data/recipes_backup.json'
    PATH_STORAGE = './data/recipes.json'