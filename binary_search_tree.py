"""
 A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties.The left subtree
 of a node has a key less than or equal to its parent node's key.The right subtree of a node has a key greater than
 to its parent node's key.Thus, BST divides all its subtrees into two segments; the left subtree and the right subtree.

 Searching for a value in a tree involves comparing the incoming value with the value exiting nodes.
 Here also we traverse the nodes from left to right and then finally with the parent. If the searched for value
 does not match any of the exiting value, then we return not found message, or else the found message is returned.
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # find val method to compare the value with nodes
    def find_val(self, lkp_val):
        if lkp_val < self.data:
            if self.left is None:
                return str(lkp_val) + " Not Found"
            return self.left.find_val(lkp_val)
        elif lkp_val > self.data:
            if self.right is None:
                return str(lkp_val) + " Not Found"
            return self.right.find_val(lkp_val)
        else:
            print(str(self.data) + ' is found')

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.find_val(7))
print(root.find_val(14))
