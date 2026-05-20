import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

from src.data_structures.linked_list import LinkedList

#untuk menjalankan ini rubah file data_structures/linked_list.py bagian "from data_structures.node import Node" menjadi "from src.data_structures.node import Node"
# =====================================
# TEST LINKED LIST
# =====================================

linked_list = LinkedList()

# append data
linked_list.append('Pasien Arya')

linked_list.append('Pasien Budi')

linked_list.append('Pasien Caca')

print(
    '\n=== LINKED LIST ==='
)

linked_list.display()

print(
    '\n=== DELETE FIRST ==='
)

removed = linked_list.delete_first()

print(
    'Data dihapus:',
    removed
)

print(
    '\n=== LINKED LIST SETELAH DELETE ==='
)

linked_list.display()

print(
    '\nTotal data:',
    linked_list.size
)