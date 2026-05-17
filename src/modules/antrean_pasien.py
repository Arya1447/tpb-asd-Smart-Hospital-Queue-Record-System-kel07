import time
from models.pasien import Pasien


class AntreanPasien:

    def daftar_pasien(
        self,
        queue,
        nomor,
        nama,
        poli,
        prioritas
    ):

        pasien = Pasien(
            nomor,
            nama,
            poli,
            prioritas,
            time.time()
        )

        queue.enqueue(pasien)

    def panggil_pasien(self, queue):

        return queue.dequeue()