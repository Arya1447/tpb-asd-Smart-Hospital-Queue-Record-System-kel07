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
        poli: Stack()
        for poli in POLI
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
        print('4. Undo Tindakan')
        print('5. Rekam Medis')
        print('6. Keluar')

        pilihan = input('Pilih menu: ').strip().lower()

        
        if pilihan in ['1', 'daftar pasien']:
            nama = input('Nama pasien: ')
            poli = input('Poli (Umum/Jantung/Ortopedi/Anak/Gigi): ').strip().capitalize()
            prioritas = input('Prioritas (Kritis/Prioritas/Reguler): ').strip().upper()
            
            
            if poli not in queues:
                print(f"Error: Poli '{poli}' tidak ditemukan!")
                continue
            if prioritas not in PRIORITAS:
                print(f"Error: Tingkat prioritas '{prioritas}' tidak valid!")
                continue

            antrean_service.daftar_pasien(
                queues[poli],
                counter,
                nama,
                poli,
                PRIORITAS[prioritas]
            )
            print(f'Pasien {nama} berhasil ditambahkan ke poli {poli}.')
            counter += 1

        
        elif pilihan in ['2', 'panggil pasien']:
            poli = input('Poli yang ingin dipanggil: ').strip().capitalize()

            if poli not in queues:
                print(f"Error: Poli '{poli}' tidak ditemukan!")
                continue

            pasien = antrean_service.panggil_pasien(queues[poli])

            if pasien:
                print('Memanggil:', pasien.nama)
            else:
                print(f'Antrean poli {poli} kosong')

        
        elif pilihan in ['3', 'tambah tindakan']:
            poli = input('Poli Tindakan: ').strip().capitalize()
            
            if poli not in dokter_stacks:
                print(f"Error: Poli '{poli}' tidak ditemukan!")
                continue
                
            tindakan = input('Masukkan nama tindakan: ')
            
            
            dokter_service.tambah_tindakan(dokter_stacks[poli], tindakan)
            print(f"Tindakan '{tindakan}' berhasil ditambahkan ke poli {poli}.")

        
        elif pilihan in ['4', 'undo tindakan']:
            poli = input('Undo tindakan dari poli: ').strip().capitalize()

            if poli not in dokter_stacks:
                print(f"Error: Poli '{poli}' tidak ditemukan!")
                continue

            hasil = dokter_service.undo_tindakan(dokter_stacks[poli])
            if hasil:
                print('Undo Berhasil:', hasil)
            else:
                print(f'Tidak ada tindakan yang bisa di-undo di poli {poli}.')

        
        elif pilihan in ['5', 'rekam medis']:
            print('Fitur rekam medis (BST) belum diimplementasikan di service.')

       
        elif pilihan in ['6', 'keluar']:
            print('Program selesai. Terima kasih!')
            break

        else:
            print('Pilihan tidak valid, silakan coba lagi.')

if __name__ == '__main__':
    main()
