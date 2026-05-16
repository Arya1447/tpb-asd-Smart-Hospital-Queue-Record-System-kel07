from data_structures.node import Node


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):

        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        self.size += 1

    def pop(self):

        if self.top is None:
            return None

        removed = self.top.data

        self.top = self.top.next

        self.size -= 1

        return removed

    def peek(self):

        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None