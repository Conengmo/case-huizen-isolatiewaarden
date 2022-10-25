# case-huizen-isolatiewaarden

In dit document beschrijf ik de case die ik heb gemaakt over maatregelen voor de energie-efficiëntie
van gebouwen.


## Verkenning

Ik begin met de opdracht lezen en begrijpen. Vervolgens met het maken van een Notebook om de data te
verkennen.
Zie [notebooks/verkenning.ipynb](https://github.com/Conengmo/case-huizen-isolatiewaarden/blob/main/notebooks/verkenning.ipynb)
. Ik maak plots van de verdeling van elk signaal.

### Opmerkelijke data: nulwaarden

Sommige dakoppervlaktes zijn nul. Dit lijkt geen fout te zijn, deze waardes komen ook in de csv
voor. Ik neem aan dat dit appartementen op een beneden- of middenverdieping zijn. We zullen de
formule voor totale isolatiewaarden hier robust voor moeten maken. Dit kunnen we doen door aan te
nemen dat het dak geen invloed heeft op de uiteindelijke isolatiewaarde, oftewel dat de dakcomponent
in de formule 1 is als er geen dak is.

### Conclusie dataverkenning

Er lijken op het eerste gezicht geen gekkigheden in de data te zitten. Er lijkt niet te hoeven
worden schoongemaakt.


## Missende kennis: besparing

Bij het lezen van de opdracht is al snel duidelijk dat een gegeven mist: wat voor besparing een
verandering van de totale isolatiewaarde oplevert. Oftewel, wat is de factor waarmee de
isolatiewaarde in euro's kan worden uitgedrukt. Zonder deze waarde weten we niet of een maatregel
uberhaubt de moeite waard is. Voor dit onderzoek zullen we een aanname doen.

Een andere dimensie is tijd, over hoeveel jaar kijken we? Dit is belangrijk voor het bepalen of een
maatregel financieel positief uitpakt.

We zouden de besparing per maatregel kunnen uitsplitsen, maar aangezien dit deel van het onderzoek
behoorlijk giswerk wordt, gaat dat de accuraatheid denk ik niet helpen.

### Bronnen zoeken over besparing

Allereerst kijken over op internet iets te vinden is over besparingen:

- https://www.isolatie-info.nl/spouwmuurisolatie/besparing beschrijft een besparing van € 2,50 per
  m2 spouwmuurisolatie per jaar.
- https://www.essent.nl/content/particulier/energie-besparen/isolatie/index.html gebruikt Milieu
  Centraal als bron en noemt een gemiddelde besparing van € 800 per jaar voor spouwmuurisolatie en €
  800 euro per jaar voor dakisolatie.

Milieu Centraal zie ik als een betrouwbare partij, dus hun waarden zal ik aanhouden.

Wat betreft cv-ketels vind ik het volgende:

- https://www.gaslicht.com/energiebesparing/zuinige-cv-ketel noemt 10 % besparing bij een nieuwe,
  zuinige ketel.
- https://www.energieinhuis.nl/oplossingen/hr-cv-ketels noemt "tot wel 30 %" besparing.
- http://www.hoe-koop-ik.nl/cv-ketel/cv-ketel-kosten/besparing-cv-ketel noemt 15 tot 20 % besparing,
  wat € 300 per jaar zou moeten schelen.
- https://www.bespaarinfo.nl/hr-ketel/ noemt een besparing van 20 % of € 300 tot € 400 per jaar.

Geen idee wie van deze gezaghebbend is. Ik maak een schatting van € 200 besparing per jaar, wat
lager dan de meer ronkende getallen die genoemd worden.

In totaal kan er bij een gemiddeld huis dus € 800 + € 800 + € 200 bespaard worden als we alle drie
de maatregelen toepassen.

### Verband isolatiewaarde en besparing

Nu is de vraag wat het verband is tussen een verschil in isolatiewaarde en een besparing in euro.
Als de isolatiewaarde met 0.1 omhoog gaat, hoeveel euro bespaart dat per jaar? En als het verschil
0.2 is, wat dan? Ik kan hier zo snel niks over vinden en neem voor het gemak aan dat het een lineair
verband is.

Ik heb een paar waarden van internet geplukt over gemiddelde besparingen en ga die correleren aan de
totale isolatiewaarde die uit de formule uit de opdracht rolt. Ik neem aan dat de besparing geldt
als we een gemiddeld huis naar de hoogste isolatiewaarde brengen. Dus ik pak de mediaan
isolatiewaarde (0,19) en de top isolatiewaarde (0,86) en correleer het verschil daar tussen met de
besparing in euro's. De aanname is dus dat als we de isolatiewaarde van een huis met 0,67 verhogen,
we € 1800 per jaar besparen. Of andersom: € 2687 / jaar / isolatiewaarde.

### Tijdsfactor

Nu nog een aanname over de looptijd van de maatregel om iets te kunnen zeggen over de totale
besparing. Ik neem aan dat institutionele woningbezitters meer naar de lange termijn kijken. Maar
die is niet oneindig lang. We hopen dat een maatregel zich binnen korte tijd terugverdiend.
CV-ketels worden over 10 tot 15 jaar afgeschreven als ik het goed heb en ook muren en daken moeten
ooit weer onderhouden of vervangen worden. Laat ik een conservatieve schatting maken en zeggen dat
de maatregelen binnen 10 jaar hun aanschaf moeten hebben terugverdiend.

### Conclusie besparingsfactor

Op basis van een aantal twijfelachtige aannamens komen we tot een besparing per isolatiewaarde
delta: € 26,870.

### Alternatief voor besparing: alleen isolatiewaarde

In plaats van te kijken wat voor een besparing een verandering in isolatiewaarde oplevert, kunnen we
ook alleen naar de verandering in isolatiewaarde kijken. We kunnen een aanname doen over hoeveel
verandering in isolatiewaarde de moeite waard is. Bijvoorbeeld dat een stijging van 0.2 in absolute
zin de moeite waard is, minder niet. Of dat we zeggen dat een huis van het 50e percentiel naar het
80e percentiel de moeite waard is. Het nadeel van deze aanpak is dat we de kosten van de maatregelen
dan buiten beschouwing laten.


## Maatregelen per woning bepalen

De eerste vraag is wat per woning de meest voordelige maatregelen zijn om te nemen en hoeveel dat
oplevert aan besparing.

### Afhankelijkheid maatregelen

De drie maatregelen zijn onafhankelijk van elkaar, maar de manier waarop ze gecombineerd worden in
de totale isolatiewaarde is dat niet. De waarden worden daar vermenigvuldigd in plaats van
opgegeteld. Aangezien we de besparing berekenen aan de hand van de totale isolatiewaarde, zullen we
de maatregelen als afhankelijk beschouwen.

Dit lijkt tot op zekere hoogte ook realistisch. Bijvoorbeeld, in een huis dat meer warmte verliest
moet de ketel harder stoken, en is het effect van een hogere ketelefficientie groter dan in een
beter geisoleerd huis.

### Uitkomst

We kunnen nu de besparing berekenen voor elke combinatie van maatregelen. Voor het gebruikte script
zie [bin/scenario_per_gebouw.py](https://github.com/Conengmo/case-huizen-isolatiewaarden/blob/main/bin/scenario_per_gebouw.py)
.

De resultaten zijn te vinden
in [data/scenario_per_gebouw.csv](https://github.com/Conengmo/case-huizen-isolatiewaarden/blob/main/data/scenario_per_gebouw.csv)
. Van iedere woning staan eerst de beginwaarden, gevolgd door de besparing in euros bij het
toepassen van een of meerdere maatregelen, en uiteindelijk de beste combinatie van maatregelen.

De uitkomst is in lijn met de verwachtingen:

- een ketel die al tegen de 0.9 aanzit, wordt niet vervangen.
- dakisolatie is niet nodig als er geen dak is.
- gevel- en dakisolatie zijn in vrijwel alle gevallen nuttig, omdat de isolatiewaardes ver genoeg
  onder het maximum van 0.85 zitten.

### Discussie

Hebben we een goede waarde geschat voor de relatie tussen isolatiewaarde en besparing? Dat is lastig
te zeggen. Als we die waarde verlagen, worden minder maatregelen rendabel. Zouden we hem verhogen,
dan wordt in meer gevallen de ketel vervangen interessant.

Uiteindelijk kan je ook je vraagtekens zetten bij de formule die ketel, gevel en dak samenbrengt.
Maar aangezien die voor deze casus een gegeven is, zullen we daar niet verder op ingaan.


## Budget toepassen op volledig woningenbestand

Vraag 2 is hoe we een bepaald budget het beste kunnen toepassen.

### Probleemmodel

Dit kunnen we zien als een discreet optimalisatieprobleem: we hebben een aantal booleans als input (
de maatregelen) en een cost function als output (de totale besparing over alle woningen). Meer
specifiek kunnen we dit probleem zien als een binary tree. We hebben 163 woningen en 3 maatregelen
per woning, dus 489 unieke maatregelen. Dat maakt dat de tree 2^489 branches heeft. De oplossing die
we zoeken is de branch die de hoogste besparing oplevert.

Er is een versimpeling die we kunnen aanbrengen. De woningen zijn onafhankelijk van elkaar, ook bij
het berekenen van de besparing. Hierdoor kunnen we het probleem reduceren tot 163 woningen maal 2^3
maatregelcombinaties is 1304 combinaties. Dit is een werkbaar getal, zodat we in iedere stap elke
combinatie kunnen berekenen. Heuristieken of optimalisatiealgoritmen zullen niet nodig zijn.

### Algoritme

Voor iedere woning berekenen we de besparing bij ieder van de 8 maatregelcombinaties. Vervolgens
kiezen we voor iedere woning de beste maatregelcombinatie. We sorteren de woningen op basis van de
besparing die de gekozen maatregelcombinatie oplevert. Dan selecteren we van deze gesorteerde lijst
met woningen totdat het budget op is.

### Resultaten

In [bin/budget_verdelen.py](https://github.com/Conengmo/case-huizen-isolatiewaarden/blob/main/bin/budget_verdelen.py)
is de beschreven methode geimplementeerd. Ik heb een budget aangenomen van € 100,000. De resultaten
zijn te vinden
in [data/budget_verdeeld.csv](https://github.com/Conengmo/case-huizen-isolatiewaarden/blob/main/data/budget_verdeeld.csv)
. De eerste kolommen bevatten de woningdata. Daarna volgt welke maatregelen voor elke woning zijn
gekozen binnen het budget. Vervolgens de totale isolatiewaarde bij aanvang en na toepassing van de
maatregelen.

De totale netto besparing is € 290,106 na aftrek van € 99,926 aan kosten.

Huizen met grote gevels en daken krijgen eerder een isolatieupgrade, dat lijkt intuitief.

Wat opvalt is dat met de huidige formule grotere getallen lijken te worden bevoordeeld. Hierdoor
worden huizen die al goed presteren nog verder geupgrade ten koste van huizen die een mindere
uitgangspositie hebben.

Woning nummer 71 heeft maar een hele kleine upgrade gehad, dat komt omdat deze als laatste is
geselecteerd om het budget nog zoveel mogelijk vol te maken.


### Discussie

We maken het budget niet helemaal op met deze aanpak. Het is mogelijk dat een andere selectie van
minder optimale maatregelen uiteindelijk tot een hogere besparing had geleid. Maar het lijkt me niet
aannemelijk.

Ook hier is de accuraatheid van de uitkomst afhankelijk van de aannames die we hebben gedaan. De
twee verbeteringen die ik het eerste zou adviseren zijn een nauwkeuriger model voor de wisselwerking
tussen ketel en isolatie en een beter model voor wat de verschillende maatregelen aan besparing
opleveren.

De uitkomst is niet eerlijk, sommige woningen krijgen alle drie de maatregelen terwijl anderen niks
krijgen. Om tot een eerlijkere verdeling van het budget te komen, zouden we de kostfunctie kunnen
aanpassen. Bijvoorbeeld door lagere isolatiewaardes te prioriteren of meerdere maatregelen per
woning te ontmoedigen.
