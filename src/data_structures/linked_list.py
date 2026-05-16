from typing import Optional


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['Node'] = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):

        new_node = Node(data)

        # jika kosong
        if self.head is None:
            self.head = new_node

        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        self.size += 1

    def prepend(self, data):

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def delete_first(self):

        if self.head is None:
            return None

        removed = self.head.data
        self.head = self.head.next

        self.size -= 1

        return removed

    def display(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def is_empty(self):

        return self.head is None

    def __len__(self):

        return self.size