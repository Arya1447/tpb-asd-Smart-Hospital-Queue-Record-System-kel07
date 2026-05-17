import numpy as np
import time
import random

from data_structures.priority_queue import PriorityQueue
from data_structures.stack import Stack
from data_structures.bst import BSTRekamMedis

from modules.antrean_pasien import AntreanPasien
from modules.dokter_service import DokterService
from modules.laporan_service import LaporanService

from models.rekam_medis import RekamMedis

# Seed random supaya hasil konsisten
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

    antrean_service = AntreanPasien()
    dokter_service = DokterService()
    laporan_service = LaporanService()

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
        print('7. Keluar')

        pilihan = input('Pilih menu: ')

        # =====================================
        # DAFTAR PASIEN
        # =====================================
        if pilihan == '1' or pilihan.lower() == 'daftar pasien':

            nama = input('Nama pasien: ')
            poli = input('Poli: ')
            prioritas = input('Prioritas: ').upper()

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

            print('Pasien berhasil ditambahkan')

            counter += 1

        # =====================================
        # PANGGIL PASIEN + TINDAKAN
        # =====================================
        elif pilihan == '2' or pilihan.lower() == 'panggil pasien':

            poli = input('Poli: ')

            if poli not in queues:
                print('Poli tidak tersedia')
                continue

            pasien = antrean_service.panggil_pasien(
                queues[poli]
            )

            if pasien:

                print('Memanggil:', pasien.nama)

                tindakan = input('Masukkan tindakan: ')

                dokter_service.tambah_tindakan(
                    dokter_stacks[poli],
                    pasien,
                    tindakan
                )

                rm_lama = bst_rm.search(pasien.no_antrian)

                if rm_lama:
                    rm_lama.riwayat.append(tindakan)

                else:
                    rm = RekamMedis(
                        pasien.no_antrian,
                        pasien.nama,
                        pasien.poli,
                        [tindakan]
                    )

                    bst_rm.insert(rm)

                print('\n=== REKAM MEDIS ===')
                print('No RM :', pasien.no_antrian)
                print('Nama  :', pasien.nama)
                print('Poli  :', pasien.poli)
                print('Tindakan :', tindakan)
                print('Tindakan berhasil disimpan')

            else:
                print('Antrean kosong')

        # =====================================
        # UNDO TINDAKAN
        # =====================================
        elif pilihan == '3' or pilihan.lower() == 'undo tindakan':

            poli = input('Poli: ')

            if poli not in dokter_stacks:
                print('Poli tidak tersedia')
                continue

            nomor_rm = int(input('Nomor RM: '))

            rm = bst_rm.search(nomor_rm)

            if rm is None:
                print('Rekam medis tidak ditemukan')
                continue

            hasil_undo = dokter_service.undo_tindakan(
                dokter_stacks[poli]
            )

            if hasil_undo:

                if rm.riwayat:

                    tindakan_dihapus = rm.riwayat.pop()

                    print('Undo berhasil')
                    print('No RM :', rm.no_rm)
                    print('Nama  :', rm.nama)
                    print('Tindakan dihapus :', tindakan_dihapus)

                else:
                    print('Riwayat tindakan kosong')

            else:
                print('Tidak ada tindakan')

        # =====================================
        # REKAM MEDIS
        # =====================================
        elif pilihan == '4' or pilihan.lower() == 'rekam medis':

            nomor_rm = int(input('Masukkan nomor RM: '))

            hasil = bst_rm.search(nomor_rm)

            if hasil:

                print('\n=== REKAM MEDIS ===')
                print('No RM :', hasil.no_rm)
                print('Nama  :', hasil.nama)
                print('Poli  :', hasil.poli)

                print('Riwayat Tindakan:')

                for item in hasil.riwayat:
                    print('-', item)

            else:
                print('Rekam medis tidak ditemukan')

        # =====================================
        # LAPORAN
        # =====================================
        elif pilihan == '5' or pilihan.lower() == 'laporan':

            print('\n=== LAPORAN PASIEN ===')

            total = 0

            for poli, queue in queues.items():

                print(f'{poli}: {queue.size} pasien')

                total += queue.size

            print('---------------------')
            print('Total seluruh pasien:', total)

        # =====================================
        # SIMULASI RANDOM PASIEN
        # =====================================
        elif pilihan == '6':

            jumlah = int(input('Jumlah pasien random: '))

            nama_random = np.random.randint(
                1000,
                9999,
                jumlah
            )

            start = time.time()

            for i in range(jumlah):

                nama = f'Pasien{nama_random[i]}'

                poli = random.choice(POLI)

                prioritas = np.random.randint(1, 4)

                antrean_service.daftar_pasien(
                    queues[poli],
                    counter,
                    nama,
                    poli,
                    prioritas
                )

                counter += 1

            end = time.time()

            print(f'{jumlah} pasien berhasil dibuat')
            print(f'Waktu proses: {end - start:.5f} detik')

        # =====================================
        # KELUAR
        # =====================================
        elif pilihan == '7' or pilihan.lower() == 'keluar':

            print('Program selesai')
            break

        else:
            print('Pilihan tidak valid')


if __name__ == '__main__':
    main()