import numpy as np
import time
import random

from dataclasses import dataclass
from typing import Optional, List

# Seed random WAJIB sama sesuai instruksi dosen
np.random.seed(42)
random.seed(42)

POLI = ['Umum', 'Jantung', 'Ortopedi', 'Anak', 'Gigi']

PRIORITAS = {
    'KRITIS': 1,
    'PRIORITAS': 2,
    'REGULER': 3
}


# ─────────────────────────────────────────────────────────
# DATA PASIEN
# ─────────────────────────────────────────────────────────

@dataclass
class Pasien:
    no_antrian: int
    nama: str
    poli: str
    prioritas: int
    waktu_daftar: float
    waktu_tunggu: float = 0.0


# ─────────────────────────────────────────────────────────
# REKAM MEDIS
# ─────────────────────────────────────────────────────────

@dataclass
class RekorMedis:
    no_rm: int
    nama: str
    riwayat: List[str]


# ─────────────────────────────────────────────────────────
# NODE LINKED LIST
# ─────────────────────────────────────────────────────────

class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional['LLNode'] = None


# ─────────────────────────────────────────────────────────
# PRIORITY QUEUE
# ─────────────────────────────────────────────────────────

class PriorityQueue:
    """
    Priority Queue berbasis Singly Linked List.
    Prioritas kecil = lebih penting.
    """

    def __init__(self):
        self.head: Optional[LLNode] = None
        self._size: int = 0

    def enqueue(self, pasien: Pasien) -> None:
        """
        Big-O: O(n)
        """
        # TODO: implementasikan
        pass

    def dequeue(self) -> Optional[Pasien]:
        """
        Big-O: O(1)
        """
        # TODO: implementasikan
        pass

    def peek(self) -> Optional[Pasien]:
        """
        Big-O: O(1)
        """
        # TODO: implementasikan
        pass

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size


# ─────────────────────────────────────────────────────────
# STACK
# ─────────────────────────────────────────────────────────

class Stack:
    """
    Stack berbasis Singly Linked List (LIFO)
    """

    def __init__(self):
        self.top: Optional[LLNode] = None
        self._size: int = 0

    def push(self, tindakan: str) -> None:
        """
        Big-O: O(1)
        """
        # TODO: implementasikan
        pass

    def pop(self) -> Optional[str]:
        """
        Big-O: O(1)
        """
        # TODO: implementasikan
        pass

    def peek(self) -> Optional[str]:
        """
        Big-O: O(1)
        """
        # TODO: implementasikan
        pass


# ─────────────────────────────────────────────────────────
# BST NODE
# ─────────────────────────────────────────────────────────

class BSTNode:
    def __init__(self, rekord: RekorMedis):
        self.rekord = rekord
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None


# ─────────────────────────────────────────────────────────
# BST REKAM MEDIS
# ─────────────────────────────────────────────────────────

class BSTRekamMedis:

    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, rekord: RekorMedis) -> None:
        """
        Big-O rata-rata: O(log n)
        Worst-case: O(n)
        """
        # TODO: implementasikan
        pass

    def search(self, no_rm: int) -> Optional[RekorMedis]:
        """
        Big-O rata-rata: O(log n)
        Worst-case: O(n)
        """
        # TODO: implementasikan
        pass

    def inorder(self) -> List[RekorMedis]:
        """
        Big-O: O(n)
        """
        # TODO: implementasikan
        pass


# ─────────────────────────────────────────────────────────
# MAIN CLI
# ─────────────────────────────────────────────────────────

def main():

    queues = {poli: PriorityQueue() for poli in POLI}

    dokter_stacks = {
        i: Stack() for i in range(len(POLI))
    }

    bst_rm = BSTRekamMedis()

    counter = 0

    print("Smart Hospital Queue System")
    print("Ketik BANTUAN untuk daftar perintah")

    # TODO:
    # Implementasi CLI


if __name__ == '__main__':
    main()