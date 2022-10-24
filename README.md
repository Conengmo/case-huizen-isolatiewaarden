# case-huizen-isolatiewaarden

In dit document beschrijf ik de case die ik heb gemaakt over maatregelen voor de energie-efficiëntie
van gebouwen.


## Verkenning

Ik begin met de opdracht lezen en begrijpen. Vervolgens met het maken van een Notebook om de data te
verkennen. Zie notebooks/verkenning.ipynb. Ik maak plots van de verdeling van elk signaal.

### Opmerkelijke data: nulwaarden

Sommige dakoppervlaktes zijn nul. Dit lijkt geen fout te zijn, deze waardes komen ook in de csv
voor. Ik neem aan dat dit appartementen op een beneden- of middenverdieping zijn. We zullen de
formule voor totale isolatiewaarden hier robust voor moeten maken.

### Conclusie dataverkenning

Er lijken op het eerste gezicht geen gekkigheden in de data te zitten. Er lijkt niet te hoeven
worden schoongemaakt.


## Missende kennis: besparing

Bij het lezen van de opdracht is al snel duidelijk dat een gegeven mist: wat voor besparing een
verandering van de totale isolatiewaarde oplevert. Hier zullen we een aanname over moeten doen.
