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
    filereader = FileReader("Game")
    f_out.line("Successfully opened file: {0}".format(filereader.get_open()))
    f_out.line_break()

    f_out.line("Creating Lexer")
    lexer = Lexer()

    f_out.line("Creating Parser")
    parser = Parser()

    f_out.line("")
    f_out.line("End")
    f_out.stop()