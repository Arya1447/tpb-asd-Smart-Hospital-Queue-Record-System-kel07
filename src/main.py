import numpy as np
import time
import random

from data_structures.priority_queue import PriorityQueue
from data_structures.stack import Stack
from data_structures.bst import BSTRekamMedis
from data_structures.graph import Graph

from modules.antrean_pasien import AntreanPasien
from modules.dokter_service import DokterService
from modules.laporan_service import LaporanService
from modules.rekam_medis_service import RekamMedisService

from models.rekam_medis import RekamMedis

np.random.seed(42)
random.seed(42)

POLI = ['Umum', 'Jantung', 'Ortopedi', 'Anak', 'Gigi']

PRIORITAS = {
    'KRITIS': 1,
    'PRIORITAS': 2,
    'REGULER': 3
}


def main():

    queues = {
        poli: PriorityQueue()
        for poli in POLI
    }

    dokter_stacks = {
        poli: Stack()
        for poli in POLI
    }

    bst_rm = BSTRekamMedis()

    graph_poli = Graph()

    antrean_service = AntreanPasien()
    dokter_service = DokterService()
    laporan_service = LaporanService()
    rekam_medis_service = RekamMedisService()

    # =========================
    # GRAPH RUJUKAN POLI
    # =========================

    graph_poli.add_edge('Umum', 'Jantung')
    graph_poli.add_edge('Umum', 'Anak')
    graph_poli.add_edge('Jantung', 'ICU')
    graph_poli.add_edge('Ortopedi', 'Radiologi')
    graph_poli.add_edge('Anak', 'Laboratorium')
    graph_poli.add_edge('Gigi', 'Radiologi')

    semua_waktu_tunggu = []

    counter = 1

    print('=== SMART HOSPITAL QUEUE SYSTEM ===')

    while True:

        print('\nMenu:')
        print('1. Daftar Pasien')
        print('2. Panggil Pasien')
        print('3. Undo Tindakan')
        print('4. Rekam Medis')
        print('5. Laporan')
        print('6. Simulasi Pasien Random')
        print('7. Graph Rujukan Poli')
        print('8. Keluar')

        pilihan = input(
            'Pilih menu: '
        ).strip().lower()

        # =====================================
        # DAFTAR PASIEN
        # =====================================

        if pilihan in ['1', 'daftar pasien']:

            nama = input(
                'Nama pasien: '
            ).strip()

            poli = input(
                'Poli (Umum/Jantung/Ortopedi/Anak/Gigi): '
            ).strip().capitalize()

            prioritas = input(
                'Prioritas (KRITIS/PRIORITAS/REGULER): '
            ).strip().upper()

            if poli not in queues:

                print('Poli tidak tersedia')
                continue

            if prioritas not in PRIORITAS:

                print('Prioritas tidak valid')
                continue

            antrean_service.daftar_pasien(
                queues[poli],
                counter,
                nama,
                poli,
                PRIORITAS[prioritas]
            )

            print(
                f'Pasien {nama} berhasil '
                f'ditambahkan ke poli {poli}'
            )

            counter += 1

        # =====================================
        # PANGGIL PASIEN
        # =====================================

        elif pilihan in ['2', 'panggil pasien']:

            poli = input(
                'Poli (Umum/Jantung/Ortopedi/Anak/Gigi): '
            ).strip().capitalize()

            if poli not in queues:

                print('Poli tidak tersedia')
                continue

            pasien = antrean_service.panggil_pasien(
                queues[poli]
            )

            if pasien:

                dokter = dokter_service.get_dokter(
                    poli
                )

                semua_waktu_tunggu.append(
                    pasien.waktu_tunggu
                )

                print('\n=== PASIEN DIPANGGIL ===')

                print(
                    'Nama :',
                    pasien.nama
                )

                print(
                    'Poli :',
                    pasien.poli
                )

                print(
                    'Dokter :',
                    dokter
                )

                print(
                    'Waktu Tunggu :',
                    f'{pasien.waktu_tunggu:.2f} detik'
                )

                while True:

                    tindakan = input(
                        'Masukkan tindakan '
                        '(ketik selesai jika selesai): '
                    ).strip()

                    if tindakan.lower() == 'selesai':
                        break

                    tanggal = time.strftime(
                        '%Y-%m-%d %H:%M:%S'
                    )

                    dokter_service.tambah_tindakan(
                        dokter_stacks[poli],
                        pasien,
                        dokter,
                        tindakan
                    )

                    rm_lama = bst_rm.search(
                        pasien.no_antrian
                    )

                    data_tindakan = {
                        "tindakan": tindakan,
                        "dokter": dokter,
                        "tanggal": tanggal
                    }

                    if rm_lama:

                        rm_lama.riwayat.append(
                            data_tindakan
                        )

                    else:

                        rm = RekamMedis(
                            pasien.no_antrian,
                            pasien.nama,
                            pasien.poli,
                            [data_tindakan]
                        )

                        bst_rm.insert(rm)

                    print(
                        f'Tindakan "{tindakan}" '
                        f'berhasil ditambahkan'
                    )

                print('\n=== REKAM MEDIS ===')

                print(
                    'No RM :',
                    pasien.no_antrian
                )

                print(
                    'Nama  :',
                    pasien.nama
                )

                print(
                    'Poli  :',
                    pasien.poli
                )

                print(
                    'Dokter :',
                    dokter
                )

                print(
                    'Waktu Tunggu :',
                    f'{pasien.waktu_tunggu:.2f} detik'
                )

                hasil = bst_rm.search(
                    pasien.no_antrian
                )

                if hasil:

                    print(
                        'Riwayat Tindakan:'
                    )

                    for item in hasil.riwayat:

                        print(
                            '-------------------'
                        )

                        print(
                            'Tindakan :',
                            item["tindakan"]
                        )

                        print(
                            'Dokter   :',
                            item["dokter"]
                        )

                        print(
                            'Tanggal  :',
                            item["tanggal"]
                        )

            else:

                print('Antrean kosong')

        # =====================================
        # UNDO TINDAKAN
        # =====================================

        elif pilihan in ['3', 'undo tindakan']:

            poli = input(
                'Poli: '
            ).strip().capitalize()

            if poli not in dokter_stacks:

                print('Poli tidak tersedia')
                continue

            try:

                nomor_rm = int(
                    input('Nomor RM: ')
                )

            except ValueError:

                print('Nomor RM harus angka')
                continue

            rm = bst_rm.search(
                nomor_rm
            )

            if rm is None:

                print(
                    'Rekam medis tidak ditemukan'
                )

                continue

            hasil_undo = dokter_service.undo_tindakan(
                dokter_stacks[poli]
            )

            if hasil_undo:

                if rm.riwayat:

                    tindakan_dihapus = (
                        rm.riwayat.pop()
                    )

                    print(
                        '\nUndo berhasil'
                    )

                    print(
                        'No RM :',
                        rm.no_rm
                    )

                    print(
                        'Nama  :',
                        rm.nama
                    )

                    print(
                        'Tindakan dihapus :',
                        tindakan_dihapus[
                            "tindakan"
                        ]
                    )

                    print(
                        'Dokter :',
                        tindakan_dihapus[
                            "dokter"
                        ]
                    )

                    print(
                        'Tanggal :',
                        tindakan_dihapus[
                            "tanggal"
                        ]
                    )

                else:

                    print(
                        'Riwayat tindakan kosong'
                    )

            else:

                print('Tidak ada tindakan')

        # =====================================
        # REKAM MEDIS
        # =====================================

        elif pilihan in ['4', 'rekam medis']:

            try:

                nomor_rm = int(
                    input(
                        'Masukkan nomor RM: '
                    )
                )

            except ValueError:

                print('Nomor RM harus angka')
                continue

            hasil = bst_rm.search(
                nomor_rm
            )

            if hasil:

                print(
                    '\n=== REKAM MEDIS ==='
                )

                print(
                    'No RM :',
                    hasil.no_rm
                )

                print(
                    'Nama  :',
                    hasil.nama
                )

                print(
                    'Poli  :',
                    hasil.poli
                )

                print(
                    'Riwayat Tindakan:'
                )

                for item in hasil.riwayat:

                    print(
                        '-------------------'
                    )

                    print(
                        'Tindakan :',
                        item["tindakan"]
                    )

                    print(
                        'Dokter   :',
                        item["dokter"]
                    )

                    print(
                        'Tanggal  :',
                        item["tanggal"]
                    )

            else:

                print(
                    'Rekam medis tidak ditemukan'
                )

        # =====================================
        # LAPORAN
        # =====================================

        elif pilihan in ['5', 'laporan']:

            print(
                '\n=== LAPORAN PASIEN ==='
            )

            total = 0

            for poli, queue in queues.items():

                print(f'\nPoli {poli}')

                laporan_service.tampilkan_total_pasien(
                    poli,
                    queue
                )

                total += queue.size

            print(
                '---------------------'
            )

            print(
                'Total seluruh pasien:',
                total
            )

            laporan_service.tampilkan_rata_rata_waktu(
                semua_waktu_tunggu
            )

            laporan_service.tampilkan_big_o()

        # =====================================
        # SIMULASI RANDOM
        # =====================================

        elif pilihan == '6':

            try:

                jumlah = int(
                    input(
                        'Jumlah pasien random: '
                    )
                )

            except ValueError:

                print('Input harus angka')
                continue

            nama_random = np.random.randint(
                1000,
                9999,
                jumlah
            )

            start = time.time()

            for i in range(jumlah):

                nama = (
                    f'Pasien{nama_random[i]}'
                )

                poli = random.choice(
                    POLI
                )

                prioritas = np.random.randint(
                    1,
                    4
                )

                antrean_service.daftar_pasien(
                    queues[poli],
                    counter,
                    nama,
                    poli,
                    prioritas
                )

                counter += 1

            end = time.time()

            print(
                f'{jumlah} pasien '
                f'berhasil dibuat'
            )

            print(
                f'Waktu proses: '
                f'{end - start:.5f} detik'
            )

        # =====================================
        # GRAPH POLI
        # =====================================

        elif pilihan in ['7', 'graph rujukan poli']:

            graph_poli.tampilkan_graph()

            mulai = input(
                'Mulai BFS dari poli: '
            ).strip().capitalize()

            if mulai:

                graph_poli.bfs(
                    mulai
                )

            else:

                print(
                    'Input tidak boleh kosong'
                )

        # =====================================
        # KELUAR
        # =====================================

        elif pilihan in ['8', 'keluar']:

            print('Program selesai')
            break

        else:

            print('Pilihan tidak valid')


if __name__ == '__main__':
    main()