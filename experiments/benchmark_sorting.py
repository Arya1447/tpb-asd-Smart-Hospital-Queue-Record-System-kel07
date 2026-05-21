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

from modules.sorting_service import SortingService


# =====================================
# EXPERIMENT SORTING
# =====================================

JUMLAH_DATA = [
    50,
    200,
    500
]

print('=== EXPERIMENT SORTING ===')


for jumlah in JUMLAH_DATA:

    data = [

        random.randint(
            1,
            10000
        )

        for _ in range(jumlah)
    ]

    # =================================
    # BUBBLE SORT EXPERIMENT
    # =================================

    start = time.time()

    SortingService.bubble_sort_pasien(
        data.copy()
    )

    end = time.time()

    # =================================
    # HASIL
    # =================================

    print(
        f'Bubble Sort {jumlah} data : '
        f'{end - start:.8f} detik'
    )

    print()