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

        # jika root kosong
        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:

            # ke kiri
            if rekord.no_rm < current.rekord.no_rm:

                if current.left is None:
                    current.left = new_node
                    return

                current = current.left

            # ke kanan
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


# untuk mengetes BST

class RekamMedis:

    def __init__(self, no_rm, nama):

        self.no_rm = no_rm
        self.nama = nama


bst = BSTRekamMedis()

bst.insert(
    RekamMedis(10, 'Arya')
)

bst.insert(
    RekamMedis(5, 'Budi')
)

bst.insert(
    RekamMedis(20, 'Caca')
)

bst.insert(
    RekamMedis(15, 'Dina')
)

# mencari data
hasil = bst.search(20)     #untuk cari data di insert BST

# tampilkan hasil
if hasil:

    print(
        'Data ditemukan'
    )

    print(
        'No RM :',
        hasil.no_rm
    )

    print(
        'Nama  :',
        hasil.nama
    )

else:

    print(
        'Data tidak ditemukan'
    )