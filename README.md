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

Op basis van een aantal twijfelachtige aannamens komen we tot een besparing per isolatiewaarde: € 26
870.


## Alternatief voor besparing: alleen isolatiewaarde

In plaats van te kijken wat voor een besparing een verandering in isolatiewaarde oplevert, kunnen we
ook alleen naar de verandering in isolatiewaarde kijken. We kunnen een aanname doen over hoeveel
verandering in isolatiewaarde de moeite waard is. Bijvoorbeeld dat een stijging van 0.2 in absolute
zin de moeite waard is, minder niet. Of dat we zeggen dat een huis van het 50e percentiel naar het
80e percentiel de moeite waard is. Het nadeel van deze aanpak is dat we de kosten van de maatregelen
dan buiten beschouwing laten.
