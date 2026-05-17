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