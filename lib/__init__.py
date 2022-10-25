import csv
from dataclasses import dataclass
from typing import List

LOOPTIJD_JAREN = 10
BESPARING_PER_ISOLATIEWAARDE_PER_JAAR = 2687


@dataclass
class Huis:
    ketel_efficientie: float
    gevel_oppervlak: float
    gevel_isolatiewaarde: float
    dak_oppervlak: float
    dak_isolatiewaarde: float
    isolatiewaarde_oorspronkelijk: float = None  # type: ignore
    kosten: float = 0.0

    def __post_init__(self):
        self.isolatiewaarde_oorspronkelijk = self.isolatiewaarde

    @property
    def isolatiewaarde(self) -> float:
        muur = self.gevel_oppervlak * self.gevel_isolatiewaarde / 40
        dak = (
            self.dak_oppervlak * self.dak_isolatiewaarde / 50
            if self.dak_oppervlak
            else 1
        )
        return muur * dak * self.ketel_efficientie

    def vervang_ketel(self):
        self.ketel_efficientie = 0.9
        self.kosten += 1200

    def toepassen_gevelisolatie(self):
        self.gevel_isolatiewaarde = min(0.85, self.gevel_isolatiewaarde + 0.2)
        self.kosten += 28 * self.gevel_oppervlak

    def toepassen_dakisolatie(self):
        self.dak_isolatiewaarde = min(0.85, self.dak_isolatiewaarde + 0.2)
        self.kosten += 25 * self.dak_oppervlak

    def bereken_netto_besparing(self) -> float:
        isolatiewaarde_delta = self.isolatiewaarde - self.isolatiewaarde_oorspronkelijk
        besparing = (
            isolatiewaarde_delta
            * BESPARING_PER_ISOLATIEWAARDE_PER_JAAR
            * LOOPTIJD_JAREN
        )
        return round(besparing - self.kosten, 2)


def load_data() -> List[Huis]:
    with open("../data/woningen.csv") as f:
        reader = csv.DictReader(f)
        huizen = [
            Huis(
                ketel_efficientie=float(d["Effiecientie ketel"]),
                gevel_oppervlak=float(d["Geveloppervlak"]),
                gevel_isolatiewaarde=float(d["Isolatiewaarde gevel"]),
                dak_oppervlak=float(d["Dakoppervlak"]),
                dak_isolatiewaarde=float(d["Isolatiewaarde dak"]),
            )
            for d in reader
        ]
    return huizen
