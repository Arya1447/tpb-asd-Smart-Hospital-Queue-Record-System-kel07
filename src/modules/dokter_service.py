class DokterService:

    def __init__(self):

        self.dokter_poli = {
            'Umum': 'Dr. Andi',
            'Jantung': 'Dr. Budi',
            'Ortopedi': 'Dr. Candra',
            'Anak': 'Dr. Sinta',
            'Gigi': 'Dr. Rina'
        }

    def get_dokter(self, poli):

        return self.dokter_poli[poli]

    def tambah_tindakan(
        self,
        stack,
        pasien,
        dokter,
        tindakan
    ):

        data = {
            "pasien": pasien.nama,
            "dokter": dokter,
            "tindakan": tindakan
        }

        stack.push(data)

    def undo_tindakan(self, stack):

        return stack.pop()