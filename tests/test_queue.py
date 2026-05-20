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
 # rubah dulu src/data_structures/priority_queue bagian 'from data_structures.node import Node' menjadi 'from src.data_structures.node import Node'

from src.data_structures.priority_queue import PriorityQueue


class Pasien:

    def __init__(
        self,
        nama,
        prioritas
    ):

        self.nama = nama
        self.prioritas = prioritas


queue = PriorityQueue()

queue.enqueue(
    Pasien('Arya', 2)
)

queue.enqueue(
    Pasien('Budi', 1)
)

queue.enqueue(
    Pasien('Caca', 3)
)

print(
    '\n=== ISI PRIORITY QUEUE ==='
)

current = queue.head

while current:

    print(
        current.data.nama,
        '- Prioritas:',
        current.data.prioritas
    )

    current = current.next


print(
    '\n=== DEQUEUE ==='
)

pasien = queue.dequeue()

print(
    'Pasien dipanggil:',
    pasien.nama
)

print(
    '\nTotal pasien:',
    queue.size
)