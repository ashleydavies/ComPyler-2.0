__author__ = 'Ashley'
from enum import Enum

SpecialIdentifiers = ["import", "if", "then"]

class LexemeType(Enum):
    identifier         = 1,
    operator           = 2,
    integer            = 3,
    special_identifier = 4
    float              = 5,
    string             = 6,
    line_break         = 7,
    boolean            = 8,

    def __str__(self):
        return "{0}".format(self.name.capitalize())

class Lexeme():
    """
    The lexeme class represents a token from the lexer
    """
    def __init__(self, type : LexemeType, val):
        self.token_type = type
        self.token_value = val

    def __eq__(self, other):
        return self.token_type == other.token_type\
               and self.token_value == other.token_value

    def __str__(self):
        return "{0} {1}".format(self.token_type.__str__()[0:2], self.token_value)