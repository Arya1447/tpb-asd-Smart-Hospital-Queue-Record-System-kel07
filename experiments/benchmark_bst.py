import sys
import os
import time
import random

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'src'
        )
    )
)

from data_structures.bst import BSTRekamMedis
# =====================================
# DUMMY REKAM MEDIS
# =====================================

class RekamMedis:

    def __init__(
        self,
        no_rm,
        nama
    ):

        self.no_rm = no_rm
        self.nama = nama


# =====================================
# EXPERIMENT BST
# =====================================

JUMLAH_DATA = [
    50,
    200,
    500
]

print('=== EXPERIMENT BST ===')


for jumlah in JUMLAH_DATA:

    bst = BSTRekamMedis()

    data_rm = []

    # =================================
    # INSERT EXPERIMENT
    # =================================

    start_insert = time.time()

    for i in range(jumlah):

        no_rm = random.randint(
            1000,
            9999
        )

        rm = RekamMedis(
            no_rm,
            f'Pasien{i}'
        )

        bst.insert(rm)

        data_rm.append(
            no_rm
        )

    end_insert = time.time()

    # =================================
    # SEARCH EXPERIMENT
    # =================================

    target = random.choice(
        data_rm
    )

    start_search = time.time()

    bst.search(target)

    end_search = time.time()

    # =================================
    # HASIL
    # =================================

    print(
        f'Insert BST {jumlah} data : '
        f'{end_insert - start_insert:.8f} detik'
    )

    print(
        f'Search BST {jumlah} data : '
        f'{end_search - start_search:.8f} detik'
    )

    print()