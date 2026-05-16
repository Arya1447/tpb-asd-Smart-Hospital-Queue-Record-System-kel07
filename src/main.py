def main():
    queues = {poli: PriorityQueue() for poli in POLI}
    dokter_stacks = {i: Stack() for i in range(len(POLI))}
    bst_rm = BSTRekamMedis()
    counter = 0

    # TODO: implementasikan loop CLI
    print('Smart Hospital Queue System Ketik BANTUAN untuk daftar perintah')

if __name__ == '__main__':
    main()
