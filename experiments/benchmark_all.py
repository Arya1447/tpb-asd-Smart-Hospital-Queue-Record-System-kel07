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

# jika ingin menjalankan ini harap ubah priotity que ue bagian 'from data_structures.node import Node' manjadi 'src.from data_structures.node import Node'

import numpy as np
import time
import random

from data_structures.priority_queue import PriorityQueue
from data_structures.bst import BSTRekamMedis

from models.pasien import Pasien
from models.rekam_medis import RekamMedis

np.random.seed(42)
random.seed(42)


def test_priority_queue(n):

    queue = PriorityQueue()

    start = time.time()

    for i in range(n):

        pasien = Pasien(
            i,
            f'Pasien{i}',
            'Umum',
            random.randint(1, 3),
            time.time()
        )

        queue.enqueue(pasien)

    end = time.time()

    print(
        f'Enqueue {n} pasien '
        f': {end - start:.5f} detik'
    )

    start = time.time()

    while not queue.is_empty():

        queue.dequeue()

    end = time.time()

    print(
        f'Dequeue {n} pasien '
        f': {end - start:.5f} detik'
    )


def test_bst(n):

    bst = BSTRekamMedis()

    start = time.time()

    for i in range(n):

        rm = RekamMedis(
            i,
            f'Pasien{i}',
            'Umum',
            []
        )

        bst.insert(rm)

    end = time.time()

    print(
        f'Insert BST {n} data '
        f': {end - start:.5f} detik'
    )

    start = time.time()

    bst.search(n // 2)

    end = time.time()

    print(
        f'Search BST {n} data '
        f': {end - start:.8f} detik'
    )


print('\n=== EXPERIMENT PRIORITY QUEUE ===')

for n in [50, 200, 500, 1000]:

    test_priority_queue(n)

print('\n=== EXPERIMENT BST ===')

for n in [50, 200, 500, 1000]:

    test_bst(n)