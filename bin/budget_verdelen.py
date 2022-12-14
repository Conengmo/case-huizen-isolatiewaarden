import csv
from collections import namedtuple
from dataclasses import replace
from typing import Dict, List

from lib import Huis, load_data

BUDGET = 100_000


HuisMaatregel = namedtuple(
    "HuisMaatregel", ["idx_huis", "idx_maatregel", "besparing", "kosten", "criterium"]
)


def main():
    huizen: List[Huis] = load_data()

    alle_maatregelen = []
    winnende_maatregelen_per_huis = []
    for idx_huis, huis in enumerate(huizen):
        maatregel_combinaties = get_maatregel_combinaties(idx_huis, huis)
        alle_maatregelen.append(maatregel_combinaties)
        winnende_maatregelen_per_huis.append(
            max(maatregel_combinaties, key=lambda x: x.criterium)
        )

    winnende_maatregelen_per_huis = sorted(
        winnende_maatregelen_per_huis, key=lambda x: x.criterium, reverse=True
    )

    totale_kosten = 0
    totale_besparing = 0
    geselecteerde_huizen_en_maatregelen: Dict[int, int] = {}
    for maatregel in winnende_maatregelen_per_huis:
        if maatregel.besparing - maatregel.kosten <= 0:
            continue
        if totale_kosten + maatregel.kosten > BUDGET:
            # we stoppen nog niet met zoeken, misschien is een volgende maatregel goedkoper
            continue
        totale_kosten += maatregel.kosten
        totale_besparing += maatregel.besparing
        geselecteerde_huizen_en_maatregelen[
            maatregel.idx_huis
        ] = maatregel.idx_maatregel

    print("totale besparing:", totale_besparing)
    print("totale kosten:", totale_kosten)
    print("geholpen huizen:", len(geselecteerde_huizen_en_maatregelen))

    header = [
        "ketel eff.",
        "gevel opp.",
        "gevel isolatie",
        "dak opp.",
        "dak isolatie",
        "gekozen",
        "isolatiew. voor",
        "isolatiew. na",
    ]
    maatregel_strs = [
        "",
        "ketel",
        "gevel",
        "dak",
        "ketel + gevel",
        "ketel + dak",
        "gevel + dak",
        "ketel + gevel + dak",
    ]
    values_matrix = []
    for idx_huis, huis in enumerate(huizen):
        values = [
            round(huis.ketel_efficientie, 4),
            round(huis.gevel_oppervlak, 2),
            round(huis.gevel_isolatiewaarde, 4),
            round(huis.dak_oppervlak, 2),
            round(huis.dak_isolatiewaarde, 4),
        ]
        if idx_maatregel := geselecteerde_huizen_en_maatregelen.get(idx_huis):
            pas_maatregel_toe(huis, idx_maatregel)
            values.extend(
                [
                    maatregel_strs[idx_maatregel],
                    round(huis.isolatiewaarde_oorspronkelijk, 2),
                    round(huis.isolatiewaarde, 2),
                ]
            )
        else:
            values.extend(
                [
                    "",
                    round(huis.isolatiewaarde_oorspronkelijk, 2),
                    "",
                ]
            )
        values_matrix.append(values)

    with open('../data/budget_verdeeld.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(header)
        writer.writerows(values_matrix)


def get_maatregel_combinaties(idx_huis: int, huis: Huis) -> List[HuisMaatregel]:
    maatregel_combinaties: List[HuisMaatregel] = []
    for idx_maatregel in range(8):
        scenario = replace(huis)
        pas_maatregel_toe(scenario, idx_maatregel)
        bruto_besparing = scenario.bereken_bruto_besparing()
        maatregel_combinaties.append(
            HuisMaatregel(
                idx_huis,
                idx_maatregel,
                bruto_besparing,
                scenario.kosten,
                (bruto_besparing / scenario.kosten) if bruto_besparing and scenario.kosten else 1,
            )
        )
    return maatregel_combinaties


def pas_maatregel_toe(huis: Huis, maatregel_idx: int):
    if maatregel_idx == 0:
        pass
    elif maatregel_idx == 1:
        huis.vervang_ketel()
    elif maatregel_idx == 2:
        huis.toepassen_gevelisolatie()
    elif maatregel_idx == 3:
        huis.toepassen_dakisolatie()
    elif maatregel_idx == 4:
        huis.vervang_ketel()
        huis.toepassen_gevelisolatie()
    elif maatregel_idx == 5:
        huis.vervang_ketel()
        huis.toepassen_dakisolatie()
    elif maatregel_idx == 6:
        huis.toepassen_gevelisolatie()
        huis.toepassen_dakisolatie()
    elif maatregel_idx == 7:
        huis.vervang_ketel()
        huis.toepassen_gevelisolatie()
        huis.toepassen_dakisolatie()


if __name__ == "__main__":
    main()
