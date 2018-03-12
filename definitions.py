from enum import Enum

class Units(Enum):
    UNIT_UNKNOWN = -1
    UNIT_VOLUME = 0
    UNIT_MASS = 1
    UNIT_UNIT = 2

class Method(Enum):
    METHOD_REMOVE = 0
    METHOD_ADD = 1
    METHOD_INDEX = 2
    METHOD_VALUE = 3
    