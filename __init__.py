__author__ = 'Ashley'
from components.lexer import Lexer
from components.operators import OperatorPrecedence
from components.parser import Parser
from components.lexeme import Lexeme
from components.filereader import FileReader
from utils.fancy_print import FancyPrint
from utils.fancy_print import Alignment

def e2s(tree):
    if type(tree) is Lexeme:
        return tree
    elif tree.node in OperatorPrecedence:
        return "({0}) {1} ({2})".format(e2s(tree.left), tree.node.getLiteral(), e2s(tree.right))
    else:
        return tree.node

if __name__ == "__main__":
    f_out = FancyPrint(48)

    f_out.line("ComPyler 2.0 - AScript", Alignment.Center)
    f_out.line_break()

    f_out.line("Creating File Reader for file \"{0}.AScript\"".format("Game"))
    file_reader = FileReader("Test")
    f_out.line("Successfully opened file: {0}".format(file_reader.get_open()))
    f_out.line_break()
    f_out.line("Creating Lexer")
    f_out.line_break()

    lexer = Lexer(file_reader, f_out)

    lexemes = []
    lexeme = lexer.get_lexeme()

    while True:
        lexemes.append(lexeme)
        f_out.line("Lexeme: {0}".format(lexeme))
        lexeme = lexer.get_lexeme()

        if lexeme == None:
            break

    f_out.line_break()
    f_out.line("Creating Parser")
    f_out.line_break()

    parser = Parser(lexemes, f_out)
    parser.parse()
    f_out.line(e2s(parser.tree.left.node[0]))

    f_out.line("")
    f_out.line("End")
    f_out.stop()