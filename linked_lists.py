"""
 Creation of linked list
"""


class Node:
    def __init__(self, element=None):
        self.element = element
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_element = None

    def print_linked_list(self):
        print_element = self.head_element
        while print_element is not None:
            print(print_element.element)
            print_element = print_element.next_element


list1 = LinkedList()
list1.head_element = Node('Monday')
e2 = Node('Tuesday')
e3 = Node('Wednesday')

# linked first node to second node
list1.head_element.next_element = e2

# linked second node to third node
e2.next_element = e3

"""
 print linked-list
"""
list1.print_linked_list()
