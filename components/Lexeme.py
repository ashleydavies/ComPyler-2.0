__author__ = 'Ashley'

class Lexeme():
    """
    The lexeme class represents a token from the lexer
    """
    def __init__(self, type, val):
        self.token_type = type
        self.token_value = val