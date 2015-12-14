__author__ = 'Ashley'
from enum import Enum

class Operator(Enum):
    SENTINEL = 1,
    EQUALS   = 2
    ADD      = 3,
    MULT     = 4,


    def precedence(self):
        return OperatorPrecedence[self]

    def getLiteral(self):
        return [x for x, val in OperatorLiterals.items() if val == self][0]

OperatorLiterals = {
    "+": Operator.ADD,
    "=": Operator.EQUALS,
    "*": Operator.MULT,
    "<-->": Operator.SENTINEL,
}

OperatorPrecedence = {
    Operator.SENTINEL: 0,
    Operator.EQUALS:   1,
    Operator.ADD:      5,
    Operator.MULT:     10,
}