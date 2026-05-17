class LaporanService:

    def tampilkan_total_pasien(
        self,
        poli,
        queue
    ):

        print(
            f'Total pasien poli {poli}: '
            f'{queue.size}'
        )

    def tampilkan_rata_rata_waktu(
        self,
        daftar_waktu
    ):

        if len(daftar_waktu) == 0:

            print(
                'Rata-rata waktu tunggu: 0 detik'
            )

            return

        rata_rata = (
            sum(daftar_waktu)
            / len(daftar_waktu)
        )

        print(
            'Rata-rata waktu tunggu:',
            f'{rata_rata:.2f} detik'
        )

    def tampilkan_big_o(self):

        print(
            'Kompleksitas enqueue '
            'Priority Queue: O(n)'
        )

        print(
            'Kompleksitas dequeue '
            'Priority Queue: O(1)'
        )

        print(
            'Kompleksitas search BST: '
            'O(log n)'
        )