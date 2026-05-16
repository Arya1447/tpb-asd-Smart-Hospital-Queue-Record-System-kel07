from data_structures.node import Node


class PriorityQueue:

    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, pasien):

        new_node = Node(pasien)

        if self.head is None:
            self.head = new_node

        elif pasien.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node

        else:
            current = self.head

            while (
                current.next is not None and
                current.next.data.prioritas <= pasien.prioritas
            ):
                current = current.next

            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def dequeue(self):

        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next

        self.size -= 1

        return removed

    def peek(self):

        if self.head is None:
            return None

        return self.head.data

    def is_empty(self):
        return self.head is None