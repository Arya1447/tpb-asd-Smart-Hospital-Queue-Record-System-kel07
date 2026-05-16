class RekamMedisService:

    def tambah_rekam_medis(self, bst, data):
        bst.insert(data)

    def cari_rekam_medis(self, bst, no_rm):
        return bst.search(no_rm)