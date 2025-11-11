
# OBJECTIVE :
# 1.) BUILD a binary expression tree from a postfix expression
# 2.) EVALUATE tree by using a recursive algorithm

from stack import Stack
from tree_node import TreeNode

class BinaryExpressionTree():
    def __init__(self, root): # constructor that creates an empty tree
        """
        Pre:

        Post: root == None
        
        Errors:  
        """
        self.root = None

    ## MAIN FUNCTIONS ##

    def is_empty(self): # booleen that checks if the tree is empty
        """
        Pre:

        Post: Returns True if root == None, else False
        
        Errors:  
        """
        if self.root == None:
            return True
        else:
            return False

    def clear_Tree(self): # clears the tree
        """
        Pre:

        Post: root == None
        
        Errors:  
        """
        self.root == None

    def build_from_postfix(self, postfix: str): # builds expression tree representing the postfix expression
        """
        Pre: Postfix is a valid whitespace-separated postfix expression (tokens = numbers
        or + - * /)

        Post: Builds expression tree representing the postfix expression
        
        Errors: 1) Invalid token ? ValueError.
                2) Too few operands ? ValueError.
                3) Extra operands/operators left ? ValueError 
        """
        if not isinstance(postfix, str):
            raise ValueError("Postfix input must be a string")

        ops = {"+","-","*","/"}
        stack = Stack()

        for token in postfix.split():
            try: #try to read a number
                _ = int(token)
            except ValueError: # if its not a number
                if token in ops:
                    try:
                        right = stack.pop()
                        left = stack.pop()
                    except IndexError:
                        raise ValueError("Needs another operand")
                    stack.push(TreeNode(token, left, right))
                else:
                    raise ValueError(f"Invalid token: {token}")
            else: # if it's a number make it a leaf
                stack.push(TreeNode(token))

        if stack.size() != 1:
            raise ValueError("Invalid postfix expression (extra operands/operators).")
        
        self.root = stack.pop()

    def evaluate_tree(self) -> float: # evaluates the expression tree and returns the result
        """
        Pre: Tree is not empty

        Post: Returns numeric value of expression
        
        Errors: Division by zero -> ZeroDivisonError
        """
        if self.root is None:
            raise ValueError("Tree is empty")
        return self._evaluate(self.root)
        
    def infix_traversal(self) -> str: # returns an infix string w/ parentheses for clarity
        pass

    def postfix_traversal(self) -> str: # returns a space-seperated postfix string
        pass

    ## HELPER FUNCTIONS ##
    
    def _inorder(self): # Appends values to out using infix order with parentheses.
        pass

    def _postorder(self): # Appends values to out in postfix order.
        pass

    def _evaluate(self, node) -> int: # Recursively computes value of subtree.
        if node.left is None and node.right is None:
            return int(node.value)

        a = self._evaluate(node.left)
        b = self._evaluate(node.right)
        op = node.value

        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                raise ZeroDivisionError("division by zero")
            return a // b

        raise ValueError(f"Invalid operator: {op}")