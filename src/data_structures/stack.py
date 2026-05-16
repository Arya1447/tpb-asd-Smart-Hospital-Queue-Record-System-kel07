from typing import Optional


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next: Optional['Node'] = None


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    # PUSH
    def push(self, data):

        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        self.size += 1

    # POP
    def pop(self):

        if self.top is None:
            return None

        removed = self.top.data

        self.top = self.top.next

        self.size -= 1

        return removed

    # PEEK
    def peek(self):

        if self.top is None:
            return None

        return self.top.data

    # ISEMPTY
    def is_empty(self):

        return self.top is None

    # LENGTH
    def __len__(self):

        return self.size