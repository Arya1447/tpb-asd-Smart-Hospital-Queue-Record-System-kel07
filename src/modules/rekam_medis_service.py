from models.rekam_medis import RekamMedis


class RekamMedisService:

    def tambah_rekam_medis(
        self,
        bst_rm,
        pasien,
        dokter,
        tindakan,
        tanggal
    ):

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

    def tampilkan_rekam_medis(
        self,
        hasil
    ):

        print('\n=== REKAM MEDIS ===')

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