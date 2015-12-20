__author__ = 'Ashley'
from components.filereader import FileReader
from components.lexeme import *
from components.operators import Operator
from utils.fancy_print import FancyPrint
import string

lexable_operators = ["+", "-", "/", "*", ",", "=", "!", "$", "^", "&", "{", "}", "(", ")"]
lexable_repeatable_operators = ["+", "-", "/", "*", "=", "!"]

class Lexer():
    """ Turns a file into meaningful tokens """
    def __init__(self, file_reader: FileReader, output: FancyPrint, debug: bool = False):
        self.file_reader = file_reader
        self.output = output
        self.debug = debug

    def get_lexeme(self) -> Lexeme:
        while True:
            read_char = self.file_reader.get_char()
            if read_char == "\n":
                return Lexeme(LexemeType.line_break, 0)
            elif read_char.isspace():
                continue
            elif read_char.isnumeric():
                num = read_char
                read_char = self.file_reader.get_char()
                deci = False
                while read_char.isnumeric() or read_char == ".":
                    if read_char == "." and deci:
                        self.output.error(self.file_reader, "Multiple decimal points in numeric literal")
                    elif read_char == ".":
                        deci = True
                    num += read_char
                    read_char = self.file_reader.get_char()
                self.file_reader.return_char()
                if deci:
                    if self.debug:
                        self.output.line("[Numeric Literal] {0}".format(num))
                    return Lexeme(LexemeType.float, float(num))
                else:
                    if self.debug:
                        self.output.line("[Integer Literal] {0}".format(num))
                    return Lexeme(LexemeType.integer, int(num))
            elif read_char in ["\"", "'"]:
                entry_char = read_char
                string_literal = ""
                read_char = self.file_reader.get_char()
                while not read_char == entry_char:
                    string_literal += read_char
                    read_char = self.file_reader.get_char()
                if self.debug:
                    self.output.line("[String Literal] {0}".format(string_literal))
                return Lexeme(LexemeType.string, string_literal)
            elif read_char in lexable_operators:
                if self.debug:
                    self.output.line("[Operator Literal] {0}".format(read_char))

                operator_literal = read_char
                read_char = self.file_reader.get_char()
                while read_char in lexable_repeatable_operators:
                    operator_literal += read_char
                    read_char = self.file_reader.get_char()

                self.file_reader.return_char()

                op = Operator.fromLiteral(operator_literal)

                return Lexeme(LexemeType.operator, op)
            elif read_char in ["_"] + list(string.ascii_letters):
                identifier = read_char
                read_char = self.file_reader.get_char()
                while read_char in string.ascii_letters:
                    identifier += read_char
                    read_char = self.file_reader.get_char()
                self.file_reader.return_char()
                if self.debug:
                    self.output.line("[Identifier literal] {0}".format(identifier))

                if identifier in ["true", "false"]:
                    return Lexeme(LexemeType.boolean, identifier)

                if identifier in SpecialIdentifiers:
                    return Lexeme(LexemeType.special_identifier, identifier)

                return Lexeme(LexemeType.identifier, identifier)
            elif read_char == "":
                if self.debug:
                    self.output.line("End of file reached")
                return None
