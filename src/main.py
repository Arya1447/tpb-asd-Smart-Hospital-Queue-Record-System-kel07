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

np.random.seed(42)
random.seed(42)

POLI = ['Umum', 'Jantung', 'Ortopedi', 'Anak', 'Gigi']

PRIORITAS = {
    'KRITIS': 1,
    'PRIORITAS': 2,
    'REGULER': 3
}


# =====================================
# HAPUS NODE BST
# =====================================

def hapus_rekam_medis(
    root,
    no_rm
):

    if root is None:
        return root

    # KE KIRI
    if no_rm < root.rekord.no_rm:

        root.left = hapus_rekam_medis(
            root.left,
            no_rm
        )

    # KE KANAN
    elif no_rm > root.rekord.no_rm:

        root.right = hapus_rekam_medis(
            root.right,
            no_rm
        )

    # NODE DITEMUKAN
    else:

        # TANPA CHILD KIRI
        if root.left is None:
            return root.right

        # TANPA CHILD KANAN
        if root.right is None:
            return root.left

        # CARI SUCCESSOR
        temp = root.right

        while temp.left:

            temp = temp.left

        root.rekord = temp.rekord

        root.right = hapus_rekam_medis(
            root.right,
            temp.rekord.no_rm
        )

    return root


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

    semua_waktu_tunggu = []

    # =====================================
    # NOMOR RM TERSEDIA KEMBALI
    # =====================================

    nomor_rm_tersedia = []

    counter = 1

    print(
        '=== SMART HOSPITAL QUEUE SYSTEM ==='
    )

    while True:

        print('\nMenu:')
        print('1. Daftar Pasien')
        print('2. Panggil Pasien')
        print('3. Undo Tindakan')
        print('4. Rekam Medis')
        print('5. Laporan')
        print('6. Simulasi Pasien Random')
        print('7. Keluar')
       
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

                print(
                    'Poli tidak tersedia'
                )

                continue

            if prioritas not in PRIORITAS:

                print(
                    'Prioritas tidak valid'
                )

                continue

            # =================================
            # GUNAKAN RM BEKAS JIKA ADA
            # =================================

            if nomor_rm_tersedia:

                nomor_rm = nomor_rm_tersedia.pop(0)

            else:

                nomor_rm = counter
                counter += 1

            antrean_service.daftar_pasien(
                queues[poli],
                nomor_rm,
                nama,
                poli,
                PRIORITAS[prioritas]
            )

            print(
                f'Pasien {nama} berhasil '
                f'ditambahkan ke poli {poli}'
            )

            print(
                f'Nomor RM : {nomor_rm}'
            )

        # =====================================
        # PANGGIL PASIEN
        # =====================================

        elif pilihan in ['2', 'panggil pasien']:

            poli = input(
                'Poli (Umum/Jantung/Ortopedi/Anak/Gigi): '
            ).strip().capitalize()

            if poli not in queues:

                print(
                    'Poli tidak tersedia'
                )

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

                print(
                    '\n=== PASIEN DIPANGGIL ==='
                )

                print(
                    'Nomor RM :',
                    pasien.no_antrian
                )

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
                    'Prioritas :',
                    pasien.prioritas
                )

                print(
                    'Waktu Tunggu :',
                    f'{pasien.waktu_tunggu:.2f} detik'
                )

                # =================================
                # INPUT TINDAKAN
                # =================================

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

                    rekam_medis_service.tambah_rekam_medis(
                        bst_rm,
                        pasien,
                        dokter,
                        tindakan,
                        tanggal
                    )

                    print(
                        f'Tindakan "{tindakan}" '
                        f'berhasil ditambahkan'
                    )

                # =================================
                # RAWAT INAP
                # =================================

                rawat = input(
                    '\nApakah pasien perlu dirawat? (y/n): '
                ).lower()

                if rawat == 'y':

                    graph_poli.route_pasien(
                        pasien
                    )

                else:

                    print(
                        '\nPasien rawat jalan'
                    )

                    print(
                        'Pasien diperbolehkan pulang'
                    )

                # =================================
                # TAMPILKAN REKAM MEDIS
                # =================================

                hasil = bst_rm.search(
                    pasien.no_antrian
                )

                if hasil:

                    rekam_medis_service.tampilkan_rekam_medis(
                        hasil
                    )

            else:

                print(
                    'Antrean kosong'
                )

        # =====================================
        # UNDO TINDAKAN
        # =====================================

        elif pilihan in ['3', 'undo tindakan']:

            try:

                nomor_rm = int(
                    input(
                        'Masukkan nomor RM: '
                    )
                )

            except ValueError:

                print(
                    'Nomor RM harus angka'
                )

                continue

            hasil_rm = bst_rm.search(
                nomor_rm
            )

            if hasil_rm:

                poli_pasien = hasil_rm.poli

                hasil_undo = dokter_service.undo_tindakan(
                    dokter_stacks[poli_pasien]
                )

                if hasil_undo:

                    print(
                        '\nUndo tindakan berhasil'
                    )

                    print(
                        'Tindakan terakhir dibatalkan'
                    )

                    # =============================
                    # HAPUS REKAM MEDIS
                    # =============================

                    bst_rm.root = hapus_rekam_medis(
                        bst_rm.root,
                        nomor_rm
                    )

                    print(
                        'Rekam medis berhasil dihapus'
                    )

                    # =============================
                    # RM BISA DIPAKAI LAGI
                    # =============================

                    nomor_rm_tersedia.append(
                        nomor_rm
                    )

                    nomor_rm_tersedia.sort()

                    print(
                        f'Nomor RM {nomor_rm} '
                        f'bisa digunakan kembali'
                    )

                else:

                    print(
                        'Tidak ada tindakan'
                    )

            else:

                print(
                    'Rekam medis tidak ditemukan'
                )

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

                print(
                    'Nomor RM harus angka'
                )

                continue

            hasil = bst_rm.search(
                nomor_rm
            )

            if hasil:

                rekam_medis_service.tampilkan_rekam_medis(
                    hasil
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

                print(
                    f'\nPoli {poli}'
                )

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

                print(
                    'Input harus angka'
                )

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

                # =============================
                # GUNAKAN RM BEKAS
                # =============================

                if nomor_rm_tersedia:

                    nomor_rm = nomor_rm_tersedia.pop(0)

                else:

                    nomor_rm = counter
                    counter += 1

                antrean_service.daftar_pasien(
                    queues[poli],
                    nomor_rm,
                    nama,
                    poli,
                    prioritas
                )

            end = time.time()

            print(
                f'{jumlah} pasien '
                f'berhasil dibuat'
            )

            print(
                f'Waktu proses: '
                f'{end - start:.5f} detik'
            )

       

        elif pilihan in ['7', 'keluar']:

            print(
                'Program selesai'
            )

            break

        else:

            print(
                'Pilihan tidak valid'
            )


if __name__ == '__main__':
    main()