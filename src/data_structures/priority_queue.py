from typing import Optional


class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['LLNode'] = None


class PriorityQueue:

    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, pasien):

        new_node = LLNode(pasien)

        # jika queue kosong
        if self.head is None:
            self.head = new_node

        # jika prioritas lebih tinggi
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

        self._size += 1

    def dequeue(self):

        if self.head is None:
            return None

        removed = self.head.data
        self.head = self.head.next
        self._size -= 1

        return removed

    def peek(self):

        if self.head is None:
            return None

        return self.head.data

    def is_empty(self):

        return self._size == 0

    def __len__(self):

        return self._size