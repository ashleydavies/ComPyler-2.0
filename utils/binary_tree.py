__author__ = 'Ashley'

class BinaryTree():
    """ As it says on the tin """
    def __init__(self, node, left = None, right = None):
        self.node = node
        self.left = left
        self.right = right

    def insertLeft(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            newLeft = BinaryTree(node)
            newLeft.left = self.left
            self.left = newLeft

    def insertRight(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            newRight = BinaryTree(node)
            newRight.right = self.right
            self.right = newRight

    def __str__(self):
        return "BTree NODE {0},  LEFT ({1}), RIGHT ({2})".format(self.node, self.left, self.right)