__author__ = 'Ashley'
from components.lexer import Lexer
from components.parser import Parser
from components.filereader import FileReader
from utils.fancyprint import FancyPrint
from utils.fancyprint import Alignment

if __name__ == "__main__":
    f_out = FancyPrint(64)

    f_out.line("ComPyler 2.0 - AScript", Alignment.Center)
    f_out.line_break()

    f_out.line("Creating File Reader for file \"{0}.AScript\"".format("Game"))
    file_reader = FileReader("Test")
    f_out.line("Successfully opened file: {0}".format(file_reader.get_open()))
    f_out.line_break()

    f_out.line("Creating Lexer")
    lexer = Lexer(file_reader, f_out)
    lexer.get_lexeme()

    f_out.line("Creating Parser")
    parser = Parser()

    f_out.line("")
    f_out.line("End")
    f_out.stop()