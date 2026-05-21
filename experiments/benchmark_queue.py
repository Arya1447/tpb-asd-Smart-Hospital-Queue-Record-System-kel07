import time
import random
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'src'
        )
    )
)

from data_structures.priority_queue import PriorityQueue
from models.pasien import Pasien


# =====================================
# EXPERIMENT PRIORITY QUEUE
# =====================================

JUMLAH_DATA = [
    50,
    200,
    500
]


print('=== EXPERIMENT PRIORITY QUEUE ===')


for jumlah in JUMLAH_DATA:

    queue = PriorityQueue()

    # =================================
    # ENQUEUE EXPERIMENT
    # =================================

    start_enqueue = time.time()

    for i in range(jumlah):

        prioritas = random.randint(
            1,
            3
        )

        pasien = Pasien(
            i + 1,
            f'Pasien{i}',
            'Umum',
            prioritas,
            time.time()
            )

        queue.enqueue(
            pasien
        )

    end_enqueue = time.time()

    # =================================
    # DEQUEUE EXPERIMENT
    # =================================

    start_dequeue = time.time()

    queue.dequeue()

    end_dequeue = time.time()

    # =================================
    # HASIL
    # =================================

    print(
        f'Enqueue Queue {jumlah} data : '
        f'{end_enqueue - start_enqueue:.8f} detik'
    )

    print(
        f'Dequeue Queue {jumlah} data : '
        f'{end_dequeue - start_dequeue:.8f} detik'
    )

    print()