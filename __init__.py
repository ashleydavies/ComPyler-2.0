__author__ = 'Ashley'
from components.lexer import Lexer
from components.lexeme import LexemeType
from components.operators import Operator
from components.parser import Parser
from components.lexeme import Lexeme
from components.filereader import FileReader
from utils.fancy_print import FancyPrint
from utils.fancy_print import Alignment
from utils.unary_tree import UnaryTree
from utils.binary_tree import BinaryTree
from utils.trinary_tree import TrinaryTree

def e2s(tree,level=0):
    pre = "\n" + " " * level + "> "
    opPre = "\n" + " " * (level + 1) + "OP "
    if type(tree) is Lexeme:
        return pre + tree.__str__()
    elif type(tree) is UnaryTree:
        return pre + "{0} {1}".format(tree.node, e2s(tree.center, level + 1))
    elif type(tree) is BinaryTree:
        if type(tree.node) is Operator:
            return pre + "{0} {1} {2}".format(e2s(tree.left, level + 1), tree.node.getLiteral(), e2s(tree.right, level + 1))
        else:
            return pre + "{0} {1} {2}".format(tree.node, e2s(tree.left, level + 1), e2s(tree.right, level + 1))
    elif type(tree) is TrinaryTree:
        return pre + "{0} {1} {2} {3}".format(tree.node, e2s(tree.left, level + 1), e2s(tree.center, level + 1), e2s(tree.right, level + 1))

    elif isinstance(tree, list):
        return "".join([e2s(x, level) for x in tree])
    else:
        return tree

if __name__ == "__main__":
    f_out = FancyPrint(48)

    f_out.line("ComPyler 2.0 - AScript", Alignment.Center)
    f_out.line_break()

    file = "Test"

    f_out.line("Creating File Reader for file \"{0}.AScript\"".format(file))
    file_reader = FileReader(file)
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

        if lexeme is None:
            break

    f_out.line_break()
    f_out.line("Creating Parser")
    f_out.line_break()

    parser = Parser(lexemes, f_out)
    parser.parse()

    print(e2s(parser.tree))

    f_out.line("")
    f_out.line("End")
    f_out.stop()