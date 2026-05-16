class DokterService:

    def tambah_tindakan(self, stack, tindakan):
        stack.push(tindakan)

    def undo_tindakan(self, stack):
        return stack.pop()