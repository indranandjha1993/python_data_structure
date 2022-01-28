"""
 Linked List is possible only to travel forward.
 In double linked list it is possible to travel both forward and backward.
 Following is the features of doubly linked list.

    1) Doubly Linked List contains a link element called first and last.
    2) Each link carries a data field(s) and two link fields called next and prev.
    3) Each link is linked with its next link using its next link.
    4) Each link is linked with its previous link using its previous link.
    5) The last link carries a link as null to mark the end of the list.
"""


class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_element):
        Node1 = Node(new_element)
        Node1.next = self.head
        if self.head is not None:
            self.head.prev = Node1
        self.head = Node1

    def insert(self, prev_node, new_element):
        if prev_node is None:
            return
        Node1 = Node(new_element)
        Node1.next = prev_node.next
        prev_node.next = Node1
        Node1.prev = prev_node
        if Node1.next is not None:
            Node1.next.prev = Node1

    def append(self, new_element):
        Node1 = Node(new_element)
        Node1.next = None
        if self.head is None:
            Node1.prev = None
            self.head = Node1
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = Node1
        Node1.prev = last
        return

    def print_list(self, node):
        while node is not None:
            print(node.element)
            last = node
            node = node.next


dl_list = DoubleLinkedList()

dl_list.push(12)
dl_list.push(8)
dl_list.push(62)
dl_list.push(2)

dl_list.insert(dl_list.head.next, 13)

dl_list.append(45)

dl_list.print_list(dl_list.head)
