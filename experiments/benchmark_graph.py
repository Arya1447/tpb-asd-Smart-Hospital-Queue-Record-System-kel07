import time

from src.data_structures.graph import Graph
from src.models.pasien import Pasien


# =====================================
# EXPERIMENT GRAPH
# =====================================

JUMLAH_DATA = [
    50,
    200,
    500
]

print('=== EXPERIMENT GRAPH ===')


for jumlah in JUMLAH_DATA:

    graph = Graph()

    pasien_list = []

    # =================================
    # INSERT / ROUTING EXPERIMENT
    # =================================

    start_route = time.time()

    for i in range(jumlah):

        # PRIORITAS ACAK
        prioritas = (
            (i % 3) + 1
        )

        # POLI ACAK
        if i % 5 == 0:
            poli = 'Jantung'

        elif i % 5 == 1:
            poli = 'Umum'

        elif i % 5 == 2:
            poli = 'Ortopedi'

        elif i % 5 == 3:
            poli = 'Anak'

        else:
            poli = 'Gigi'

        pasien = Pasien(
            i + 1,
            f'Pasien{i}',
            poli,
            prioritas
        )

        pasien_list.append(
            pasien
        )

        graph.route_pasien(
            pasien
        )

    end_route = time.time()

    # =================================
    # SEARCH ROUTING EXPERIMENT
    # =================================

    target = pasien_list[
        jumlah // 2
    ]

    start_search = time.time()

    graph.route_pasien(
        target
    )

    end_search = time.time()

    # =================================
    # HASIL
    # =================================

    print(
        f'Routing Graph {jumlah} data : '
        f'{end_route - start_route:.8f} detik'
    )

    print(
        f'Search Routing {jumlah} data : '
        f'{end_search - start_search:.8f} detik'
    )

    print()