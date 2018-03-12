from enum import Enum
from definitions import Units

class Ingredient():
    def __init__(self):
        self.type = ''
        self.unit = Units.UNIT_UNKNOWN
        self.amount = 0

