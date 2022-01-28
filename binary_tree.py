"""
 Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties −

    1) One node is marked as Root node.
    2) Every node other than the root is associated with one parent node.
    3) Each node can have an arbitrary number of child node.

 We create a tree data structure in python by using the concept os node discussed earlier.
 We designate one node as root node and then add more nodes as child nodes. Below is program to create the root node.
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert Node
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

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root_element):
        res = []
        if root_element:
            res = self.inorderTraversal(root_element.left)
            res.append(root_element.data)
            res = res + self.inorderTraversal(root_element.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root_element):
        res = []
        if root_element:
            res.append(root_element.data)
            res = res + self.PreorderTraversal(root_element.left)
            res = res + self.PreorderTraversal(root_element.right)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print("Inorder Traversal", root.inorderTraversal(root))
print("Preorder Traversal", root.PreorderTraversal(root))
print("Postorder Traversal", root.PostorderTraversal(root))
