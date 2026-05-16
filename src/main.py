from data_structures.priority_queue import PriorityQueue
from data_structures.stack import Stack
from data_structures.bst import BSTRekamMedis
from modules.antrean_pasien import AntreanPasien
from modules.dokter_service import DokterService
from modules.laporan_service import LaporanService
from modules.rekam_medis_service import RekamMedisService

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

    laporan_service = LaporanService()
    bst_rm = BSTRekamMedis()
    antrean_service = AntreanPasien()
    dokter_service = DokterService()
    rekam_medis_service = RekamMedisService()
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
                try:
                    print('Memanggil:', pasien.nama)
                except AttributeError:
                    print('Memanggil:', pasien)
            else:
                print(f'Antrean poli {poli} kosong')
            print("--- Status Antrean Saat Ini ---")
            laporan_service.tampilkan_total_pasien(queues[poli])

        
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
            print('\nSub-Menu Rekam Medis:')
            print('A. Tambah Rekam Medis')
            print('B. Cari Rekam Medis')
            sub_pilihan = input('Pilih opsi (A/B): ').strip().upper()

            if sub_pilihan == 'A':
            
                data_rm = input('Masukkan data rekam medis (misal: "RM001 - Budi - Sakit Gigi"): ')
                rekam_medis_service.tambah_rekam_medis(bst_rm, data_rm)
                print('Data rekam medis berhasil dimasukkan ke dalam BST.')

            elif sub_pilihan == 'B':
                no_rm = input('Masukkan nomor/keyword rekam medis yang dicari: ')
                hasil_cari = rekam_medis_service.cari_rekam_medis(bst_rm, no_rm)
                
                if hasil_cari:
                    print('Data Rekam Medis Ditemukan:', hasil_cari)
                else:
                    print('Data Rekam Medis tidak ditemukan.')
            else:
                print('Opsi tidak valid.')

if __name__ == '__main__':
    main()
