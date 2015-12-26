__author__ = 'Ashley'
from enum import Enum

class Operator(Enum):
    SENTINEL     = 1
    EQUALS       = 2
    ADD          = 3
    MULT         = 4
    L_PAREN      = 5
    R_PAREN      = 6
    L_CURLY      = 7
    R_CURLY      = 8
    L_SQUARE     = 9
    R_SQUARE     = 10
    COMMA        = 11
    EQUALITY     = 12

    @staticmethod
    def fromLiteral(operator):
        return OperatorLiterals[operator]

    def precedence(self):
        return OperatorPrecedence[self]

    def getLiteral(self):
        return [x for x, val in OperatorLiterals.items() if val == self][0]

OperatorLiterals = {
    "+": Operator.ADD,
    "=": Operator.EQUALS,
    "*": Operator.MULT,
    "(": Operator.L_PAREN,
    ")": Operator.R_PAREN,
    "{": Operator.L_CURLY,
    "}": Operator.R_CURLY,
    "[": Operator.L_SQUARE,
    "]": Operator.R_SQUARE,
    ",": Operator.COMMA,
    "==": Operator.EQUALITY,
    "<-->": Operator.SENTINEL,
}

OperatorPrecedence = {
    Operator.SENTINEL: 0,
    Operator.L_PAREN:  1,
    Operator.R_PAREN:  1,
    Operator.EQUALITY: 1,
    Operator.EQUALS:   2,
    Operator.ADD:      5,
    Operator.MULT:     10,
}