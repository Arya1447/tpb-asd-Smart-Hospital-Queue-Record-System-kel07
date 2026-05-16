class BSTNode:

    def __init__(self, rekord):
        self.rekord = rekord
        self.left = None
        self.right = None


class BSTRekamMedis:

    def __init__(self):
        self.root = None

    def insert(self, rekord):

        new_node = BSTNode(rekord)

        if self.root is None:
            self.root = new_node
            return
            current = self.root

        while True:

            if rekord.no_rm < current.rekord.no_rm:

                if current.left is None:
                    current.left = new_node
                    return

                current = current.left

            else:

                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

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