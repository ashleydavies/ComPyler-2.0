__author__ = 'Ashley'
from components.filereader import FileReader
from components.lexeme import Lexeme
from components.lexer import Lexer
from components.operators import Operator
from components.parser import Parser
from utils.fancy_print import Alignment
from utils.fancy_print import FancyPrint
from utils.tree import Tree
from utils.unary_tree import UnaryTree
from utils.binary_tree import BinaryTree
from utils.trinary_tree import TrinaryTree

def t2s(tree, level=0):
    if (type(tree) is UnaryTree) or (type(tree) is TrinaryTree):
        assert isinstance(tree.center, Tree) or tree.center is None, "Center of %s should be a tree" % tree

    if (type(tree) is BinaryTree) or (type(tree) is TrinaryTree):
        assert isinstance(tree.left, Tree) or tree.left is None, "Left of %s should be a tree" % tree
        assert isinstance(tree.right, Tree) or tree.right is None, "Right of %s should be a tree" % tree

    pre = "\n" + " " * level + "> "
    level = level + 1

    if type(tree) is UnaryTree:
        return pre + "UT N[{0}]: C[{1}]".format(n2s(tree.node, level), t2s(tree.center, level))
    elif type(tree) is BinaryTree:
        return pre + "BT N[{0}]: L[{1}], R[{2}]".format(n2s(tree.node, level), t2s(tree.left, level), t2s(tree.right, level))
    elif type(tree) is TrinaryTree:
        return pre + "TT N[{0}]: L[{1}], C[{2}], R[{3}]".format(n2s(tree.node, level), t2s(tree.left, level), t2s(tree.center, level), t2s(tree.right, level))
    else:
        return n2s(tree, level)

def n2s(node, level=0):
    if type(node) is Lexeme:
        return node.__str__()
    elif isinstance(node, list):
        return "{List: " + ", ".join([t2s(x, level) for x in node]) + "}"
    else:
        return node

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
    x = True
    print(t2s(parser.tree))

    f_out.line("")
    f_out.line("End")
    f_out.stop()
