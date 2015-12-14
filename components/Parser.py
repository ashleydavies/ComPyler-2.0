__author__ = 'Ashley'
from utils.fancy_print import FancyPrint
from utils.binary_tree import BinaryTree
from components.lexer import *
from components.lexeme import *

class Parser():
    """ Accepts a lexer and creates an abstract syntax tree by requesting lexemes """
    def __init__(self, lexemes: [Lexeme], output: FancyPrint):
        self.output = output
        self.lexemes = lexemes
        self.tree = BinaryTree("PROGRAM")
        self.treeNode = self.tree

    def parse(self):
        lex = self.lexeme_peek()

        self.treeNode.left = []

        while lex != None:
            self.statement()
            lex = self.lexeme_peek()

    def statement(self):
        lex = self.lexeme_get()
        if lex.token_type == LexemeType.identifier:
            next = self.lexeme_get()
            if next.token_type == LexemeType.operator and next.token_value == Operator.EQUALS:
                self.treeNode.left.append(BinaryTree(next.token_value, lex, self.expr()))
            else:
                pass

    def expr(self):
        return self.recursive_expr([Operator.SENTINEL], [])


    def recursive_expr(self, operatorStack, operandStack):
        lex = self.lexeme_peek()
        if lex == None:
            return
        operables = [LexemeType.identifier, LexemeType.float, LexemeType.integer, LexemeType.string]
        if lex.token_type in operables:
            operandStack.append(self.lexeme_get())
        elif lex.token_type == LexemeType.operator:
            if (lex.token_value.precedence() > operatorStack[-1].precedence()):
                operatorStack.append(self.lexeme_get().token_value)
            else:
                operandStack.append(BinaryTree(operatorStack.pop(), operandStack.pop(), operandStack.pop()))
        else:
            if (len(operandStack) > 1):
                operandStack.append(BinaryTree(operatorStack.pop(), operandStack.pop(), operandStack.pop()))
            else:
                return operandStack[0]

        return self.recursive_expr(operatorStack, operandStack)

    def lexeme_peek(self):
        if len(self.lexemes) > 0:
            return self.lexemes[0]
        else:
            return None

    def lexeme_get(self):
        lex = self.lexeme_peek()
        if lex == None:
            return None

        self.lexemes = self.lexemes[1:]
        return lex