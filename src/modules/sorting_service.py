class SortingService:

    @staticmethod
    def bubble_sort_pasien(data):

        n = len(data)

        for i in range(n):

            for j in range(0, n - i - 1):

                if data[j] > data[j + 1]:

                    data[j], data[j + 1] = (
                        data[j + 1],
                        data[j]
                    )

        return data


    @staticmethod
    def tampilkan_sorting(data):

        print('\nData Sebelum Sorting:')
        print(data)

        hasil = SortingService.bubble_sort_pasien(
            data.copy()
        )

        print('\nData Setelah Sorting:')
        print(hasil)