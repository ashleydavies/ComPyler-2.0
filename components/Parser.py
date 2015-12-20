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

        while lex is not None:
            self.statement()
            lex = self.lexeme_peek()


    def statement(self):
        lex = self.lexeme_get()
        if lex.token_type == LexemeType.identifier:
            next = self.lexeme_peek()
            if next.token_type == LexemeType.operator and next.token_value == Operator.EQUALS:
                self.treeNode.left.append(BinaryTree(self.lexeme_get().token_value, lex, self.expr()))
            else:
                self.treeNode.left.append(self.call(lex))
        elif lex.token_type == LexemeType.special_identifier:
            if lex.token_value == "if":
                self.ifstmt()
            elif lex.token_value == "import":
                name = self.lexeme_get()
                assert name.token_type == LexemeType.string
                self.treeNode.left.append(BinaryTree("IMPORT", name.token_value))

    def match(self, lexeme):
        assert lexeme == self.lexeme_get()

    def call(self, identifier):
        tree = BinaryTree("CALL", identifier, [])
        self.match(Lexeme(LexemeType.operator, Operator.L_PAREN))

        while self.lexeme_peek().token_value != Operator.R_PAREN:
            tree.right.append(self.expr())
            if self.lexeme_peek().token_value == Operator.COMMA:
                self.match(self.lexeme_peek())
            else:
                break

        self.match(Lexeme(LexemeType.operator, Operator.R_PAREN))
        return tree

    def ifstmt(self):
        cond = self.expr()
        self.match(Lexeme(LexemeType.special_identifier, "then"))
        block = self.block()
        self.treeNode.left.append(BinaryTree("IF", cond, block))

    def block(self):
        oldTree = self.treeNode
        self.treeNode = BinaryTree("BLOCK", [], None)
        self.match(Lexeme(LexemeType.operator, Operator.CURLY_BEGIN))

        while self.lexeme_peek().token_value != Operator.CURLY_END:
            self.statement()

        self.match(Lexeme(LexemeType.operator, Operator.CURLY_END))

        newTree = self.treeNode
        self.treeNode = oldTree
        return newTree

    def expr(self):
        return self.recursive_expr([Operator.SENTINEL], [])

    def recursive_expr(self, operatorStack, operandStack):
        lex = self.lexeme_peek()
        if lex is None:
            return
        operables = [LexemeType.identifier, LexemeType.float, LexemeType.integer, LexemeType.string, LexemeType.boolean]
        binaryoperables = [Operator.ADD, Operator.MULT, Operator.EQUALITY]

        if lex.token_type in operables:
            lex = self.lexeme_get()
            if lex.token_type == LexemeType.identifier and self.lexeme_peek().token_value == Operator.L_PAREN:
                operandStack.append(self.call(lex))
            else:
                operandStack.append(lex)
        elif lex.token_type == LexemeType.operator and lex.token_value in binaryoperables:
            if lex.token_value.precedence() > operatorStack[-1].precedence():
                operatorStack.append(self.lexeme_get().token_value)
            else:
                operandStack.append(BinaryTree(operatorStack.pop(), operandStack.pop(), operandStack.pop()))
        elif lex.token_type == LexemeType.operator and lex.token_value == Operator.L_PAREN:
            self.lexeme_get()
            operandStack.append(self.expr())
        else:
            if (len(operandStack) > 1):
                self.recursive_expr_popper(operatorStack, operandStack)
            else:
                return operandStack[0]

        return self.recursive_expr(operatorStack, operandStack)

    def recursive_expr_popper(self, operatorStack, operandStack):
        node = operatorStack.pop()
        right = operandStack.pop()
        left = operandStack.pop()
        operandStack.append(BinaryTree(node, left, right))

    def lexeme_peek(self):
        if len(self.lexemes) > 0:
            return self.lexemes[0]
        else:
            return None

    def lexeme_get(self):
        lex = self.lexeme_peek()
        if lex is None:
            return None

        self.lexemes = self.lexemes[1:]
        return lex