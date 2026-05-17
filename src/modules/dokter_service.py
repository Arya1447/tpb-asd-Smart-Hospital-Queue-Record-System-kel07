class DokterService:

    def tambah_tindakan(self, stack, pasien, tindakan):

        data = {
            "pasien": pasien,
            "tindakan": tindakan
        }

        stack.push(tindakan)

    def undo_tindakan(self, stack):
        return stack.pop()