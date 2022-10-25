from collections import namedtuple
from dataclasses import replace
from typing import Dict, List, Tuple

from pytablewriter import MarkdownTableWriter

from lib import Huis, load_data

BUDGET = 100_000


HuisMaatregel = namedtuple(
    "HuisMaatregel", ["idx_huis", "idx_maatregel", "besparing", "kosten"]
)


def main():
    huizen: List[Huis] = load_data()

    alle_maatregelen = []
    winnende_maatregelen_per_huis = []
    for idx_huis, huis in enumerate(huizen):
        maatregel_combinaties = get_maatregel_combinaties(idx_huis, huis)
        alle_maatregelen.append(maatregel_combinaties)
        winnende_maatregelen_per_huis.append(
            max(maatregel_combinaties, key=lambda x: x.besparing)
        )

    winnende_maatregelen_per_huis = sorted(
        winnende_maatregelen_per_huis, key=lambda x: x.besparing, reverse=True
    )

    totale_kosten = 0
    totale_besparing = 0
    geselecteerde_huizen_en_maatregelen: Dict[int, int] = {}
    for maatregel in winnende_maatregelen_per_huis:
        if maatregel.besparing <= 0:
            break
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

    header = [
        "",
        "ketel eff.",
        "gevel opp.",
        "gevel isolatie",
        "dak opp.",
        "dak isolatie",
        "gekozen",
        "iso.w. voor",
        "iso.w. na",
    ]
    maatregel_strs = [
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
            idx_huis + 1,
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
    writer = MarkdownTableWriter(
        headers=header,
        value_matrix=values_matrix,
    )
    writer.write_table()


def get_maatregel_combinaties(idx_huis: int, huis: Huis) -> List[HuisMaatregel]:
    maatregel_combinaties: List[HuisMaatregel] = []
    for idx_maatregel in range(7):
        scenario = replace(huis)
        pas_maatregel_toe(scenario, idx_maatregel)
        maatregel_combinaties.append(
            HuisMaatregel(
                idx_huis,
                idx_maatregel,
                scenario.bereken_netto_besparing(),
                scenario.kosten,
            )
        )
    return maatregel_combinaties


def pas_maatregel_toe(huis: Huis, maatregel_idx: int):
    if maatregel_idx == 0:
        huis.vervang_ketel()
    elif maatregel_idx == 1:
        huis.toepassen_gevelisolatie()
    elif maatregel_idx == 2:
        huis.toepassen_dakisolatie()
    elif maatregel_idx == 3:
        huis.vervang_ketel()
        huis.toepassen_gevelisolatie()
    elif maatregel_idx == 4:
        huis.vervang_ketel()
        huis.toepassen_dakisolatie()
    elif maatregel_idx == 5:
        huis.toepassen_gevelisolatie()
        huis.toepassen_dakisolatie()
    elif maatregel_idx == 6:
        huis.vervang_ketel()
        huis.toepassen_gevelisolatie()
        huis.toepassen_dakisolatie()


if __name__ == "__main__":
    main()
