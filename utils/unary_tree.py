from utils.tree import Tree

__author__ = 'Ashley'

class UnaryTree(Tree):
    def __init__(self, node, center = None):
        self.node = node
        self.center = center

    def __str__(self):
        return "UTree NODE {0},  CENTER ({1})".format(self.node, self.center)