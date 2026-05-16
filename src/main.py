from data_structures.priority_queue import PriorityQueue
from data_structures.stack import Stack
from data_structures.bst import BSTRekamMedis

from modules.antrean_pasien import AntreanPasien
from modules.dokter_service import DokterService


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
        i: Stack()
        for i in range(len(POLI))
    }

    bst_rm = BSTRekamMedis()

    antrean_service = AntreanPasien()
    dokter_service = DokterService()

    counter = 1
    print('=== SMART HOSPITAL QUEUE SYSTEM ===')

    while True:

        print('\nMenu:')
        print('1. Daftar Pasien')
        print('2. Panggil Pasien')
        print('3. Tambah Tindakan')
        print('4. undo tindakan')
        print('5. Rekam Medis')
        print('6. Keluar')

        pilihan = input('Pilih menu: ')

        if pilihan == '1' or pilihan == 'Daftar Pasien' or pilihan == 'daftar pasien':

            nama = input('Nama pasien: ')
            poli = input('Poli: ')
            prioritas = input('Prioritas: ').upper()
            
            antrean_service.daftar_pasien(
                queues[poli],
                counter,
                nama,
                poli,
                PRIORITAS[prioritas]
            )

            print('Pasien berhasil ditambahkan')

            counter += 1

        elif pilihan == '2' or pilihan == 'panggil pasien' or pilihan == 'Panggil Pasien':
            poli = input('Poli: ')

            pasien = antrean_service.panggil_pasien(
                queues[poli]
            )

            if pasien:
                print('Memanggil:', pasien.nama)
            else:
                print('Antrean kosong')

        elif pilihan == '3' or pilihan == 'Tambah Tindakan' or pilihan == 'tambah tindakan':

            hasil = dokter_service.undo_tindakan(
                dokter_stacks[0]
            )

            print('Undo:', hasil)

        elif pilihan == '4' or pilihan == 'keluar'
            print('Program selesai')
            break

        else:
            print('Pilihan tidak valid')


if __name__ == '__main__':
    main()