from typing import Optional, List


class BSTNode:

    def __init__(self, rekord):
        self.rekord = rekord
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None


class BSTRekamMedis:

    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, rekord):

        new_node = BSTNode(rekord)

        # jika tree kosong
        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:

            # masuk kiri
            if rekord.no_rm < current.rekord.no_rm:

                if current.left is None:
                    current.left = new_node
                    return

                current = current.left

            # masuk kanan
            else:

                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

    # SEARCH
    def search(self, no_rm):

        current = self.root

        while current:

            if no_rm == current.rekord.no_rm:
                return current.rekord

            elif no_rm < current.rekord.no_rm:
                current = current.left

            else:
                current = current.right

        return None

    # INORDER TRAVERSAL
    def inorder(self):

        hasil = []

        def traverse(node):

            if node is not None:

                traverse(node.left)

                hasil.append(node.rekord)

                traverse(node.right)

        traverse(self.root)

        return hasil