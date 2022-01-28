"""
    In the english dictionary the word stack means arranging objects on over another. It is the same way memory is
    allocated in this data structure. It stores the data elements in a similar fashion as a bunch of plates are stored
    one above another in the kitchen. So stack data structure allows operations at one end which can be called top of
    the stack.We can add elements or remove elements only form this en dof the stack.

    In a stack the element inserted last in sequence will come out first as we can remove only from the top of the
    stack. Such feature is known as Last in First Out(LIFO) feature. The operations of adding and removing the
    elements is known as PUSH and POP. In the following program we implement it as add and remove functions. We
    declare an empty list and use to append() and pop() methods to add and remove the data elements.
"""


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, element):
        if element not in self.stack:
            self.stack.append(element)
            return True
        else:
            return False

    def get(self):
        return self.stack[-1]

    def remove(self):
        if len(self.stack) == 0:
            return "There has no element in stack to remove"
        else:
            self.stack.pop()
            return "Last element of stack has been removed"


Stack1 = Stack()
Stack1.add('Mon')
Stack1.add('Tue')
print(Stack1.get())
Stack1.add('Wed')
print(Stack1.get())
print(Stack1.remove())
print(Stack1.get())
