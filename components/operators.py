__author__ = 'Ashley'
from enum import Enum

class Operator(Enum):
    SENTINEL     = 1
    EQUALS       = 2
    ADD          = 3
    MULT         = 4
    L_PAREN      = 5
    R_PAREN      = 6
    CURLY_BEGIN  = 7
    CURLY_END    = 8
    COMMA        = 9
    EQUALITY     = 10

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
    "{": Operator.CURLY_BEGIN,
    "}": Operator.CURLY_END,
    ",": Operator.COMMA,
    "==": Operator.EQUALITY,
    "<-->": Operator.SENTINEL,
}

OperatorPrecedence = {
    Operator.SENTINEL: 0,
    Operator.L_PAREN:  1,
    Operator.R_PAREN:  1,
    Operator.EQUALS:   2,
    Operator.ADD:      5,
    Operator.MULT:     10,
    Operator.EQUALITY: 50
}