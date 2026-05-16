from dataclasses import dataclass
from typing import List


@dataclass
class RekamMedis:
    no_rm: int
    nama: str
    riwayat: List[str]