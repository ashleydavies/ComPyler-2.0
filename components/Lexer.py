from components.filereader import FileReader
from utils.fancyprint import FancyPrint
__author__ = 'Ashley'


class Lexer():
    """ The Lexer is a mystical tool from the realms of Gondor that turns a file into meaningful tokens """
    def __init__(self, file_reader: FileReader, output: FancyPrint):
        self.file_reader = file_reader
        self.output = output

    def get_lexeme(self):
        while True:
            read_char = self.file_reader.get_char()

            if read_char.isspace():
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

                self.output.line("[Numeric Literal] {0}".format(num))
                self.file_reader.return_char()
            elif read_char in ["\"", "'"]:
                entry_char = read_char
                string_literal = ""
                read_char = self.file_reader.get_char()
                while not read_char == entry_char:
                    string_literal += read_char
                    read_char = self.file_reader.get_char()
                self.output.line("[String Literal] {0}".format(string_literal))
            elif read_char in ["+", "-", "/", "*", "=", "!", "$", "^", "&"]:
                self.output.line("[Operator Literal] {0}".format(read_char))
            elif read_char == "":
                self.output.line("End of file reached")
                # EOF reached
                break
