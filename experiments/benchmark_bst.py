import time
import random

from src.data_structures.bst import BSTRekamMedis
from src.models.rekam_medis import RekamMedis


# =====================================
# EXPERIMENT BST
# =====================================

JUMLAH_DATA = [50,200,500]


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
            f'Pasien{i}',
            'Dokter A',
            'Pemeriksaan',
            '2025-01-01'
        )

        bst.insert(rm)

        data_rm.append(no_rm)

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