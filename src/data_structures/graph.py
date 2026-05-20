class Graph:

    def __init__(self):

        # =================================
        # ROUTING PASIEN KRITIS
        # =================================

        self.routing = {

            'Jantung': 'ICCU',

            'Umum': 'ICU',

            'Ortopedi': 'Trauma Center',

            'Anak': 'PICU',

            'Gigi': 'IGD Gigi'
        }

        # =================================
        # KAMAR REGULER
        # =================================

        self.kamar_reguler = {

            'Reguler-1': 0,
            'Reguler-2': 0,
            'Reguler-3': 0
        }

        # =================================
        # KAMAR PRIORITAS
        # =================================

        self.kamar_prioritas = {

            'Priority-1': 0,
            'Priority-2': 0,
            'Priority-3': 0
        }

    # =====================================
    # TAMPILKAN GRAPH
    # =====================================

    def tampilkan_graph(self):

        print(
            '\n=== GRAPH ROUTING RUMAH SAKIT ==='
        )

        for poli, tujuan in self.routing.items():

            print(
                f'{poli} -> {tujuan}'
            )

    # =====================================
    # ROUTING PASIEN
    # =====================================

    def route_pasien(
        self,
        pasien
    ):

        print(
            '\n=== SISTEM RAWAT INAP ==='
        )

        # =================================
        # PASIEN KRITIS
        # =================================

        if pasien.prioritas == 1:

            tujuan = self.routing.get(
                pasien.poli
            )

            print(
                '\nPasien KRITIS'
            )

            print(
                f'Pasien dirujuk ke {tujuan}'
            )

        # =================================
        # PASIEN PRIORITAS
        # =================================

        elif pasien.prioritas == 2:

            print(
                '\nPasien PRIORITAS'
            )

            self.cari_kamar_prioritas()

        # =================================
        # PASIEN REGULER
        # =================================

        else:

            print(
                '\nPasien REGULER'
            )

            self.cari_kamar_reguler()

    # =====================================
    # CARI KAMAR REGULER
    # =====================================

    def cari_kamar_reguler(self):

        for kamar in self.kamar_reguler:

            if self.kamar_reguler[kamar] < 4:

                self.kamar_reguler[
                    kamar
                ] += 1

                print(
                    f'Pasien masuk ke {kamar}'
                )

                print(
                    'Isi kamar:',
                    f'{self.kamar_reguler[kamar]}/4'
                )

                return

        print(
            '\nKamar penuh'
        )

        print(
            'Silahkan rujuk '
            'ke rumah sakit lainnya'
        )

    # =====================================
    # CARI KAMAR PRIORITAS
    # =====================================

    def cari_kamar_prioritas(self):

        for kamar in self.kamar_prioritas:

            if self.kamar_prioritas[kamar] < 4:

                self.kamar_prioritas[
                    kamar
                ] += 1

                print(
                    f'Pasien masuk ke {kamar}'
                )

                print(
                    'Isi kamar:',
                    f'{self.kamar_prioritas[kamar]}/4'
                )

                return

        print(
            '\nKamar penuh'
        )

        print(
            'Silahkan rujuk '
            'ke rumah sakit lainnya'
        )