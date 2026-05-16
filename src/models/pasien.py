from dataclasses import dataclass


@dataclass
class Pasien:
    no_antrian: int
    nama: str
    poli: str
    prioritas: int