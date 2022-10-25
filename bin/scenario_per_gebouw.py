from dataclasses import replace
from typing import List

import numpy as np
from pytablewriter import MarkdownTableWriter

from lib import Huis, load_data


def main():
    huizen: List[Huis] = load_data()
    header = [
        "ketel eff.",
        "gevel opp.",
        "gevel isolatie",
        "dak opp.",
        "dak isolatie",
        "ketel",
        "gevel",
        "dak",
        "ketel + gevel",
        "ketel + dak",
        "gevel + dak",
        "ketel + gevel + dak",
        "beste maatregel",
    ]
    values_matrix = []
    for huis in huizen:
        values = [
            round(huis.ketel_efficientie, 4),
            round(huis.gevel_oppervlak, 2),
            round(huis.gevel_isolatiewaarde, 4),
            round(huis.dak_oppervlak, 2),
            round(huis.dak_isolatiewaarde, 4),
        ]
        scenario = replace(huis)
        scenario.vervang_ketel()
        values.append(scenario.bereken_netto_besparing())

        scenario = replace(huis)
        scenario.toepassen_gevelisolatie()
        values.append(scenario.bereken_netto_besparing())

        scenario = replace(huis)
        scenario.toepassen_dakisolatie()
        values.append(scenario.bereken_netto_besparing())

        scenario = replace(huis)
        scenario.vervang_ketel()
        scenario.toepassen_gevelisolatie()
        values.append(scenario.bereken_netto_besparing())

        scenario = replace(huis)
        scenario.vervang_ketel()
        scenario.toepassen_dakisolatie()
        values.append(scenario.bereken_netto_besparing())

        scenario = replace(huis)
        scenario.toepassen_gevelisolatie()
        scenario.toepassen_dakisolatie()
        values.append(scenario.bereken_netto_besparing())

        scenario = replace(huis)
        scenario.vervang_ketel()
        scenario.toepassen_gevelisolatie()
        scenario.toepassen_dakisolatie()
        values.append(scenario.bereken_netto_besparing())

        idx_winnende_maatregel = np.argmax(values[5:])
        if values[idx_winnende_maatregel + 5] < 0:
            values.append("niks")
        else:
            values.append(header[idx_winnende_maatregel + 5])

        values_matrix.append(values)

    writer = MarkdownTableWriter(
        headers=header,
        value_matrix=values_matrix,
    )
    writer.write_table()


if __name__ == "__main__":
    main()
