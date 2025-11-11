
# OBJECTIVE :
# 1.) BUILD a binary expression tree from a postfix expression
# 2.) EVALUATE tree by using a recursive algorithm

from stack import Stack
from tree_node import TreeNode

class BinaryExpressionTree():
    def __init__(self, root): # constructor that creates an empty tree
        self.root = None

    ## MAIN FUNCTIONS ##

    def is_empty(self): # booleen that checks if the tree is empty
        if self.root == None:
            return True
        else:
            return False

    def clear_Tree(self): # clears the tree
        self.root == None

    def build_from_postfix(self): # builds expression tree representing the postfix expression
        pass

    def evaluate_tree(self): # evaluates the expression tree and returns the result
        pass

    def infix_traversal(self): # returns an infix string w/ parentheses for clarity
        pass

    def postfix_traversal(self): # returns a space-seperated postfix string
        pass

    ## HELPER FUNCTIONS ##
    
    def _inorder(self): # Appends values to out using infix order with parentheses.
        pass

    def _postorder(self): # Appends values to out in postfix order.
        pass

    def _evaluate(self): # Recursively computes value of subtree.
        pass
