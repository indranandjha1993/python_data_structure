"""
    The queue data structure also means the same where the data elements are arranged in a queue. The uniqueness of
    queue lies in the way items are added and removed. The items are allowed at on end but removed form the other end.
    So it is a First-in-First out method.

    A queue can be implemented using python list where we can use the insert() and pop() methods to add and remove
    elements. There is no insertion as data elements are always added at the end of the queue.
"""


class Queue:
    def __init__(self):
        self.queue = []

    def add(self, element):
        if element not in self.queue:
            self.queue.insert(0, element)
            return True
        else:
            return False

    def size(self):
        return len(self.queue)

    def remove(self):
        if len(self.queue) > 0:
            self.queue.pop()
            return "First Inserted element has been removed from queue"
        else:
            return "There has no element in queue"

    def get_all(self):
        return self.queue


Queue1 = Queue()
Queue1.add('Mon')
Queue1.add('Tue')
Queue1.add('Wed')
Queue1.add('Thu')
print(Queue1.get_all())

print(Queue1.size())

Queue1.remove()
print(Queue1.get_all())
