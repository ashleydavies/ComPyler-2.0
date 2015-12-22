from utils.tree import Tree

__author__ = 'Ashley'

class TrinaryTree(Tree):
    def __init__(self, node, left = None, center = None, right = None):
        self.node = node
        self.left = left
        self.center = center
        self.right = right

    def __str__(self):
        return "TTree NODE {0},  LEFT ({1}), CENTER ({2}), RIGHT ({3})".format(self.node, self.left, self.center, self.right)