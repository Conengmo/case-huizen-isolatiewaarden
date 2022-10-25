from dataclasses import replace
from typing import List

import numpy as np
from pytablewriter import MarkdownTableWriter
from tqdm import tqdm

from lib import Huis, load_data


BUDGET = 100_000


def main():
    huizen: List[Huis] = load_data()

    besparingen = np.empty((len(huizen), 3))
    for i, huis in enumerate(huizen):
        bereken_besparing(huis, besparingen, i)

    _budget = BUDGET
    maatregelen = np.zeros((len(huizen), 3), dtype=bool)
    totale_besparing = 0
    pbar = tqdm()
    while _budget > 0:
        pbar.update()
        pbar.set_description(str(_budget))

        # welk huis en maatregel heeft de hoogste besparing?
        idx_tuple = np.unravel_index(np.argmax(besparingen, axis=None), besparingen.shape)
        idx_winnende_huis = int(idx_tuple[0])
        winnende_huis = huizen[idx_winnende_huis]
        # maar alleen als de besparing positief is
        if besparingen[idx_tuple] <= 0:
            print('exit early')
            break

        # pas de maatregel toe
        kosten_vooraf = winnende_huis.kosten
        maatregel_idx = idx_tuple[1]
        if maatregel_idx == 0:
            winnende_huis.vervang_ketel()
        elif maatregel_idx == 1:
            winnende_huis.toepassen_gevelisolatie()
        elif maatregel_idx == 2:
            winnende_huis.toepassen_dakisolatie()

        # werk het budget bij
        kosten_maatregel = winnende_huis.kosten - kosten_vooraf
        _budget -= kosten_maatregel

        # sla de winnende maatregel op in de output matrix
        maatregelen[idx_tuple] = True
        totale_besparing += besparingen[idx_tuple]

        # update de besparingen van het winnende huis (de rest is nog hetzelfde)
        bereken_besparing(winnende_huis, besparingen, idx_winnende_huis)
        # maar neem huizen + maatregelen die al hebben gewonnen niet meer mee
        besparingen[maatregelen] = 0

    pbar.close()

    print('totale besparing:', totale_besparing)

    header = [
        "",
        "ketel eff.",
        "gevel opp.",
        "gevel isolatie",
        "dak opp.",
        "dak isolatie",
        "ketel",
        "gevel",
        "dak",
    ]
    values_matrix = []
    # gebruik de oorspronkelijke woningdata voor de output
    for i, huis in enumerate(load_data()):
        values = [
            i + 1,
            round(huis.ketel_efficientie, 4),
            round(huis.gevel_oppervlak, 2),
            round(huis.gevel_isolatiewaarde, 4),
            round(huis.dak_oppervlak, 2),
            round(huis.dak_isolatiewaarde, 4),
            *['ja' if maatregelen[i, j] else '' for j in range(0, 3)]
        ]
        values_matrix.append(values)
    writer = MarkdownTableWriter(
        headers=header,
        value_matrix=values_matrix,
    )
    writer.write_table()


def bereken_besparing(huis: Huis, besparingen_matrix: np.ndarray, i: int):
    scenario = replace(huis)
    scenario.vervang_ketel()
    besparingen_matrix[i, 0] = scenario.bereken_netto_besparing()

    scenario = replace(huis)
    scenario.toepassen_gevelisolatie()
    besparingen_matrix[i, 1] = scenario.bereken_netto_besparing()

    scenario = replace(huis)
    scenario.toepassen_dakisolatie()
    besparingen_matrix[i, 2] = scenario.bereken_netto_besparing()


if __name__ == "__main__":
    main()
