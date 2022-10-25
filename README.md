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
. In de onderstaande tabel staan van iedere woning eerst de beginwaarden, gevolgd door de besparing
in euros bij het toepassen van een of meerdere maatregelen, en uiteindelijk de beste combinatie van
maatregelen.

De uitkomst is in lijn met de verwachtingen:

- een ketel die al tegen de 0.9 aanzit, wordt niet vervangen.
- dakisolatie is niet nodig als er geen dak is.
- gevel- en dakisolatie zijn in vrijwel alle gevallen nuttig, omdat de isolatiewaardes ver genoeg
  onder het maximum van 0.85 zitten.

|ketel eff.|gevel opp.|gevel isolatie|dak opp.|dak isolatie| ketel  | gevel |  dak  |ketel + gevel|ketel + dak|gevel + dak|ketel + gevel + dak|  beste maatregel  |
|---------:|---------:|-------------:|-------:|-----------:|-------:|------:|------:|------------:|----------:|----------:|------------------:|-------------------|
|    0.6551|     40.29|        0.6231|   54.50|      0.5741| 1384.12|1090.99|1045.83|      3304.59|    3330.16|    2909.88|            6312.66|ketel + gevel + dak|
|    0.8669|     59.99|        0.3220|   56.30|      0.4406| -986.72|1786.71|1126.00|       932.45|     236.09|    4486.12|            3788.78|gevel + dak        |
|    0.5485|     61.38|        0.3957|   54.50|      0.5886| 2480.00|1182.84| 588.44|      5522.63|    4318.95|    2757.24|            8979.52|ketel + gevel + dak|
|    0.5627|     33.77|        0.5478|   52.00|      0.4053|  566.48| 130.60| 154.55|      1342.02|    1592.74|     816.20|            3217.61|ketel + gevel + dak|
|    0.6489|     33.77|        0.3265|   52.00|      0.3065| -607.07|  -7.00|-300.16|      -250.91|    -520.35|     305.22|             685.13|ketel + gevel + dak|
|    0.5442|     84.13|        0.5502|   52.00|      0.4634| 4131.88| 608.44|2219.36|      6678.54|    8652.55|    4107.13|           13315.10|ketel + gevel + dak|
|    0.7261|     36.86|        0.5067|   56.30|      0.3299| -389.68| 303.70| 644.23|       233.85|     745.81|    1757.73|            2373.03|ketel + gevel + dak|
|    0.7735|     36.86|        0.4337|   56.30|      0.5320| -386.24|1262.61| 462.99|      1251.65|     382.66|    2588.22|            3024.25|ketel + gevel + dak|
|    0.7861|     61.99|        0.6007|   54.90|      0.4604|  239.89|1573.88|2945.57|      2293.19|    3810.97|    5957.19|            7510.29|ketel + gevel + dak|
|    0.5684|     87.57|        0.5958|   52.80|      0.4588| 4431.36| 787.77|2886.86|      7109.57|    9772.99|    5086.86|           14687.49|ketel + gevel + dak|
|    0.7426|     37.28|        0.6992|   57.80|      0.5356|  506.85| 692.22|1561.17|      1567.15|    2705.40|    2901.67|            4551.43|ketel + gevel + dak|
|    0.8137|     83.72|        0.6993|   52.00|      0.4556|  407.35| 924.58|5356.23|      1678.42|    6469.14|    7715.66|            9327.16|ketel + gevel + dak|
|    0.8006|     59.99|        0.6474|   56.30|      0.4046|  -19.03|1260.07|3296.35|      1605.88|    3861.09|    6009.60|            7119.53|ketel + gevel + dak|
|    0.8103|     37.28|        0.4886|   52.80|      0.5386| -575.96|1264.49| 774.03|       943.97|     429.79|    2895.69|            2901.76|ketel + gevel + dak|
|    0.7054|     85.77|        0.3888|   52.80|      0.6377| 1735.71|3072.64|2017.72|      6318.35|    4674.10|    6807.14|           11447.07|ketel + gevel + dak|
|    0.8554|     51.41|        0.5931|   50.60|      0.6933| -559.61|2705.84|1514.12|      2362.17|    1099.28|    5157.09|            5007.01|gevel + dak        |
|    0.5708|     29.88|        0.4430|   58.70|      0.5338|  634.42| 599.27|-275.71|      2061.82|    1046.05|     861.59|            3321.77|ketel + gevel + dak|
|    0.8495|     29.34|        0.6195|   58.70|      0.4958| -841.39|1127.73| 967.97|       402.12|     271.24|    2881.98|            2347.73|gevel + dak        |
|    0.7324|     29.88|        0.6918|   58.70|      0.4050|  -93.49| 269.05| 920.48|       428.56|    1373.40|    1735.54|            2566.42|ketel + gevel + dak|
|    0.8188|     33.51|        0.6508|   62.20|      0.5622| -368.24|1628.78|1429.70|      1515.06|    1357.38|    3971.76|            4244.50|ketel + gevel + dak|
|    0.7007|     36.42|        0.4831|   62.20|      0.5853|  514.63|1476.61| 505.70|      2701.06|    1606.28|    2835.40|            4888.35|ketel + gevel + dak|
|    0.5939|     29.34|        0.4839|   58.70|      0.6011|  860.44| 830.41|-137.56|      2542.41|    1408.45|    1242.50|            3923.40|ketel + gevel + dak|
|    0.6772|     29.88|        0.3692|   58.70|      0.3409| -539.04| 251.29|-289.10|        70.25|    -440.36|     600.47|            1017.25|ketel + gevel + dak|
|    0.5783|     29.34|        0.4260|   58.70|      0.3213| -181.10|  38.21|-327.43|       335.44|     125.76|     246.00|            1475.29|ketel + gevel + dak|
|    0.7322|     29.88|        0.3980|   58.70|      0.4515| -489.63| 721.34| -94.07|       588.68|    -269.01|    1317.45|            1657.63|ketel + gevel + dak|
|    0.7736|     63.10|        0.3909|   64.60|      0.3934| -135.87|1566.47|1697.17|      1975.06|    2102.32|    4958.34|            6184.78|ketel + gevel + dak|
|    0.8152|     67.97|        0.6665|   85.50|      0.5420| 1192.34|4428.71|6345.89|      6279.93|    8420.99|   13111.05|           16088.16|ketel + gevel + dak|
|    0.8036|     29.88|        0.5437|   58.70|      0.4809| -606.11| 984.74| 591.58|       597.10|     232.45|    2333.79|            2283.98|gevel + dak        |
|    0.6615|     29.88|        0.4534|   58.70|      0.6028|  336.15|1042.53| -54.05|      2056.29|     791.78|    1611.97|            3360.24|ketel + gevel + dak|
|    0.5843|     29.88|        0.3067|   58.70|      0.5197|  -14.11| 594.46|-623.03|      1353.71|    -180.78|     522.14|            2035.36|ketel + gevel + dak|
|    0.6341|     29.88|        0.6727|   58.70|      0.3319|  198.78|  42.68| 542.73|       610.20|    1584.48|    1115.34|            2748.05|ketel + gevel + dak|
|    0.7219|     29.88|        0.5394|   58.70|      0.4901|  -90.86| 830.87| 367.65|      1151.29|     729.41|    1879.00|            2819.88|ketel + gevel + dak|
|    0.7507|     66.80|        0.3258|   64.60|      0.4553|   83.49|2092.69|1220.76|      2964.15|    1868.08|    5054.43|            6835.87|ketel + gevel + dak|
|    0.7659|     66.80|        0.6525|   64.60|      0.6947| 2323.41|4220.99|2884.49|      7610.54|    5995.42|    8466.96|           12882.32|ketel + gevel + dak|
|    0.6945|     29.56|        0.6358|   58.70|      0.6885|  897.52|1401.72| 194.34|      2959.08|    1583.72|    2118.84|            4322.78|ketel + gevel + dak|
|    0.7982|     29.88|        0.6197|   58.70|      0.5658| -358.51|1291.81| 863.38|      1204.90|     802.31|    2907.51|            3214.04|ketel + gevel + dak|
|    0.5939|     29.56|        0.5996|   58.70|      0.3013|   89.40|   6.64| 192.57|       526.15|    1137.79|     752.97|            2413.77|ketel + gevel + dak|
|    0.7262|     66.84|        0.4947|   64.60|      0.3511|  550.76|1086.39|2553.19|      2344.95|    4101.36|    5324.72|            7983.94|ketel + gevel + dak|
|    0.5974|     56.86|        0.4965|   62.84|      0.6968| 3824.74|2404.89| 609.72|      8253.89|    5538.88|    3893.13|           11291.47|ketel + gevel + dak|
|    0.5754|     25.27|        0.5121|   56.90|      0.3827|   28.84| 143.21|-283.98|       651.95|     387.08|     303.85|            1705.62|ketel + gevel + dak|
|    0.7213|     53.34|        0.5318|   49.32|      0.3595|    7.64| 339.51|1478.70|       801.28|    2158.16|    2837.95|            4224.18|ketel + gevel + dak|
|    0.8353|     67.21|        0.5235|   49.10|      0.6668| -199.17|3057.35|2323.70|      3240.55|    2399.44|    6737.77|            7300.91|ketel + gevel + dak|
|    0.6943|     67.21|        0.3670|   49.10|      0.5743|  721.69|1653.82|1032.17|      3422.71|    2423.12|    3917.36|            6720.22|ketel + gevel + dak|
|    0.6542|     67.21|        0.4432|   49.10|      0.3497|  488.89| 146.45|1343.60|      1397.44|    2798.51|    2650.22|            5303.14|ketel + gevel + dak|
|    0.8621|     53.34|        0.5204|   49.32|      0.4376| -895.18|1173.24|1938.34|       395.22|    1182.48|    4330.42|            3745.25|gevel + dak        |
|    0.7068|     42.81|        0.5543|    0.00|      0.5211| 1879.29|2866.58|   0.00|      5856.98|    1879.29|    2866.58|            5856.98|ketel + gevel      |
|    0.6071|     64.47|        0.3969|    0.00|      0.4104| 3835.41|3452.91|   0.00|      9825.64|    3835.41|    3452.91|            9825.64|ketel + gevel      |
|    0.6022|     42.58|        0.6582|    0.00|      0.4694| 4406.16|2111.72|   0.00|      8151.61|    4406.16|    2111.72|            8151.61|ketel + gevel      |
|    0.8729|     66.24|        0.5516|    0.00|      0.6635| -535.03|5913.58|   0.00|      5619.66|    -535.03|    5913.58|            5619.66|gevel              |
|    0.6466|     40.50|        0.3460|   71.98|      0.3912|  143.53| 847.42| -46.94|      1767.50|     783.45|    1813.45|            3817.38|ketel + gevel + dak|
|    0.5291|     64.16|        0.4527|   71.98|      0.5722| 4760.86|1960.65|1172.88|      9355.00|    8017.18|    4446.73|           14844.99|ketel + gevel + dak|
|    0.5836|     66.47|        0.6960|    0.00|      0.4197| 8632.45|2151.02|   0.00|     12958.36|    8632.45|    2151.02|           12958.36|ketel + gevel      |
|    0.5321|     42.81|        0.4474|    0.00|      0.3488| 3534.35|1861.50|   0.00|      7512.05|    3534.35|    1861.50|            7512.05|ketel + gevel      |
|    0.7436|     66.24|        0.4083|    0.00|      0.3366| 1641.48|4762.84|   0.00|      7796.17|    1641.48|    4762.84|            7796.17|ketel + gevel      |
|    0.6617|     42.58|        0.5134|    0.00|      0.4860| 2299.68|2593.10|   0.00|      6256.00|    2299.68|    2593.10|            6256.00|ketel + gevel      |
|    0.5452|     64.16|        0.4489|   71.98|      0.4815| 3558.13|1460.90|1237.66|      7138.85|    6772.29|    4051.66|           12586.67|ketel + gevel + dak|
|    0.5587|     40.50|        0.3365|   71.98|      0.5225| 1149.79|1152.93|-326.84|      3699.44|    1722.37|    1701.44|            5681.97|ketel + gevel + dak|
|    0.6791|     34.18|        0.5584|    0.00|      0.6866| 1632.20|2161.47|   0.00|      4808.04|    1632.20|    2161.47|            4808.04|ketel + gevel      |
|    0.6898|      9.93|        0.3886|    0.00|      0.5980| -655.21| 642.23|   0.00|       267.44|    -655.21|     642.23|             267.44|gevel              |
|    0.7447|      9.93|        0.5386|    0.00|      0.5523| -642.08| 715.48|   0.00|       280.56|    -642.08|     715.48|             280.56|gevel              |
|    0.8895|     33.49|        0.6429|    0.00|      0.3101|-1048.23|3064.51|   0.00|      2063.50|   -1048.23|    3064.51|            2063.50|gevel              |
|    0.8529|     32.88|        0.6317|    0.00|      0.6565| -542.49|2846.86|   0.00|      2512.56|    -542.49|    2846.86|            2512.56|gevel              |
|    0.8418|     34.18|        0.5233|    0.00|      0.5951| -500.91|2908.66|   0.00|      2674.92|    -500.91|    2908.66|            2674.92|gevel              |
|    0.7448|     32.05|        0.3526|    0.00|      0.5666|  -21.81|2309.72|   0.00|      2956.11|     -21.81|    2309.72|            2956.11|ketel + gevel      |
|    0.5452|      8.49|        0.5527|    0.00|      0.3927|  -81.60| 384.15|   0.00|       707.24|     -81.60|     384.15|             707.24|ketel + gevel      |
|    0.5135|      8.49|        0.5430|    0.00|      0.5497|   -3.16| 348.04|   0.00|       785.69|      -3.16|     348.04|             785.69|ketel + gevel      |
|    0.7637|     32.05|        0.3946|    0.00|      0.3372|  -42.41|2391.23|   0.00|      2935.52|     -42.41|    2391.23|            2935.52|ketel + gevel      |
|    0.7338|     31.44|        0.4318|    0.00|      0.3658|  315.73|2219.23|   0.00|      3236.98|     315.73|    2219.23|            3236.98|ketel + gevel      |
|    0.8462|     32.05|        0.6891|    0.00|      0.5279| -401.17|2034.19|   0.00|      1819.58|    -401.17|    2034.19|            1819.58|gevel              |
|    0.8448|     32.05|        0.3192|    0.00|      0.4254| -820.38|2740.05|   0.00|      2157.55|    -820.38|    2740.05|            2157.55|gevel              |
|    0.8901|      8.49|        0.4505|    0.00|      0.6369|-1174.64| 777.59|   0.00|      -385.79|   -1174.64|     777.59|            -385.79|gevel              |
|    0.6048|      8.49|        0.4672|    0.00|      0.3878| -413.58| 452.17|   0.00|       375.27|    -413.58|     452.17|             375.27|gevel              |
|    0.8728|     32.05|        0.6909|    0.00|      0.5544| -795.16|2092.09|   0.00|      1390.15|    -795.16|    2092.09|            1390.15|gevel              |
|    0.8282|     31.44|        0.5079|    0.00|      0.6509| -429.43|2617.84|   0.00|      2491.82|    -429.43|    2617.84|            2491.82|gevel              |
|    0.7560|     32.05|        0.4795|    0.00|      0.6820|  286.27|2357.94|   0.00|      3264.20|     286.27|    2357.94|            3264.20|ketel + gevel      |
|    0.6226|     29.73|        0.3851|   55.64|      0.6245|  282.33| 895.85|-325.26|      1948.03|     431.80|    1124.09|            2897.56|ketel + gevel + dak|
|    0.5553|     59.66|        0.4196|    0.00|      0.6413| 4596.94|2780.27|   0.00|     10140.25|    4596.94|    2780.27|           10140.25|ketel + gevel      |
|    0.7785|     59.66|        0.6052|    0.00|      0.5954| 1746.61|4569.52|   0.00|      7289.92|    1746.61|    4569.52|            7289.92|ketel + gevel      |
|    0.7909|     29.73|        0.3918|   55.64|      0.4946| -730.26| 906.14| -13.66|       415.67|    -553.95|    1595.58|            1392.03|gevel + dak        |
|    0.7839|     31.44|        0.3097|   55.64|      0.5032| -774.83| 973.91|-249.90|       473.65|    -855.76|    1460.95|            1238.81|gevel + dak        |
|    0.6922|     29.73|        0.6649|   55.64|      0.6105|  674.68| 906.03| 654.58|      2102.65|    1943.41|    2130.14|            4111.90|ketel + gevel + dak|
|    0.8478|     75.81|        0.3947|   61.74|      0.4957| -557.97|3163.10|2664.56|      2930.49|    2365.61|    7960.18|            8117.85|ketel + gevel + dak|
|    0.5652|     29.37|        0.5859|   53.84|      0.5262|  992.65| 441.26|  61.13|      2182.36|    1887.21|     982.70|            3841.73|ketel + gevel + dak|
|    0.5582|     29.37|        0.6188|   53.84|      0.6193| 1583.38| 646.42| 121.62|      3129.34|    2603.83|    1242.34|            4914.60|ketel + gevel + dak|
|    0.6316|     29.37|        0.6650|   53.84|      0.6290| 1184.79| 739.59| 438.55|      2588.04|    2381.58|    1674.75|            4492.45|ketel + gevel + dak|
|    0.7896|     75.81|        0.3459|   61.74|      0.3043| -469.13| 898.99|1891.77|       852.41|    1903.02|    4776.82|            5488.34|ketel + gevel + dak|
|    0.6686|     29.37|        0.6147|   53.84|      0.5779|  546.12| 819.40| 400.45|      1933.61|    1550.88|    1788.04|            3703.17|ketel + gevel + dak|
|    0.8602|     29.37|        0.5847|   53.84|      0.4195| -992.72| 710.90| 791.06|      -210.92|    -102.84|    2232.96|            1443.77|gevel + dak        |
|    0.8436|     29.37|        0.3961|   53.84|      0.5339| -946.70|1091.32|  73.89|       272.51|    -777.92|    1882.10|            1206.09|gevel + dak        |
|    0.6404|     29.37|        0.4735|   53.84|      0.4934|   88.58| 520.23| -57.78|      1153.13|     553.08|    1006.62|            2382.44|ketel + gevel + dak|
|    0.8690|     29.37|        0.6915|   54.04|      0.6724| -892.68|1151.90| 925.27|       329.64|     113.78|    2598.76|            1876.30|gevel + dak        |
|    0.6206|     29.37|        0.6491|   54.04|      0.4823|  665.13| 454.21| 366.98|      1694.02|    1805.50|    1350.53|            3602.04|ketel + gevel + dak|
|    0.7398|     29.37|        0.3282|   54.04|      0.4061| -744.81| 459.07|-315.51|        -8.33|    -836.16|     774.60|             667.96|gevel + dak        |
|    0.8016|     29.37|        0.3332|   54.04|      0.6226| -764.57|1306.09|-212.06|       802.91|    -836.76|    1777.72|            1498.36|gevel + dak        |
|    0.8480|     75.80|        0.3222|   61.73|      0.3445| -836.88|1550.27|1891.62|       938.80|    1265.56|    5574.12|            5304.34|gevel + dak        |
|    0.8823|     75.81|        0.6417|   61.73|      0.4889| -851.18|3301.70|5575.86|      2559.25|    4867.37|   11096.49|           10541.21|gevel + dak        |
|    0.8672|     29.37|        0.6985|   54.04|      0.3260|-1040.78|  90.71|1232.41|      -915.54|     289.32|    1883.33|             995.94|gevel + dak        |
|    0.7235|     29.37|        0.5614|   54.04|      0.3366| -488.75| 216.23| 381.21|       -19.14|     315.06|    1214.53|            1552.32|ketel + gevel + dak|
|    0.5810|     29.37|        0.6962|   54.04|      0.3644|  525.90|-128.25| 373.98|       778.84|    1847.19|     626.72|            2690.32|ketel + gevel + dak|
|    0.7661|     36.86|        0.4784|   56.30|      0.4849| -334.16|1039.43| 636.08|      1067.27|     659.03|    2529.90|            3064.17|ketel + gevel + dak|
|    0.6911|     36.86|        0.3399|   56.30|      0.6824|  150.64|1597.72|-309.61|      2543.08|     172.81|    1934.11|            3406.46|ketel + gevel + dak|
|    0.8038|     36.86|        0.3735|   56.30|      0.4016| -797.82| 768.04| 266.66|       185.57|    -330.88|    1931.16|            1656.22|gevel + dak        |
|    0.5874|     87.97|        0.4057|   57.80|      0.6968| 4836.71|3128.67|1049.82|     10941.12|    7214.16|    5408.28|           15202.81|ketel + gevel + dak|
|    0.5653|     37.28|        0.5349|   52.80|      0.6900| 2066.57|1019.30| -40.41|      4307.20|    2783.65|    1457.31|            5785.93|ketel + gevel + dak|
|    0.5017|     61.44|        0.4755|   52.80|      0.4393| 2425.86| 201.03| 759.61|      4151.97|    4836.17|    1835.35|            8131.28|ketel + gevel + dak|
|    0.6087|     87.97|        0.6482|   57.80|      0.5797| 6279.54|2357.67|3945.61|     10944.84|   12805.52|    7966.42|           19930.07|ketel + gevel + dak|
|    0.7859|     40.29|        0.6981|   54.50|      0.4874|  -54.43| 588.35|1874.34|       783.22|    2290.00|    3167.06|            3934.31|ketel + gevel + dak|
|    0.5560|     59.99|        0.5974|   56.30|      0.3319| 1894.70|  -4.91|1607.30|      2925.77|    5366.87|    2611.63|            8031.48|ketel + gevel + dak|
|    0.6278|     61.38|        0.3525|   54.50|      0.4523|  750.40| 833.74| 627.03|      2690.61|    2239.90|    2589.44|            5798.05|ketel + gevel + dak|
|    0.5481|     33.77|        0.5107|   52.00|      0.5791| 1255.50| 552.09|  20.68|      2769.24|    2124.20|    1089.98|            4487.26|ketel + gevel + dak|
|    0.7032|     33.77|        0.3143|   52.00|      0.5464| -402.84| 867.39|-257.23|       971.88|    -368.27|    1273.79|            1855.77|ketel + gevel + dak|
|    0.5440|     84.13|        0.5323|   52.00|      0.5810| 5270.57|1359.78|2103.83|      9061.63|    9601.78|    4742.57|           15508.74|ketel + gevel + dak|
|    0.8242|     36.86|        0.5773|   56.30|      0.3774| -739.45| 702.43|1245.77|       122.52|     750.37|    2867.36|            2616.05|gevel + dak        |
|    0.5011|     61.43|        0.5934|   57.80|      0.5018| 4466.38| 678.85|1392.01|      7054.94|    8116.88|    3026.99|           12422.75|ketel + gevel + dak|
|    0.8647|     37.28|        0.5365|   52.80|      0.3621|-1018.53| 612.02|1133.79|      -338.86|     215.50|    2660.48|            1847.19|gevel + dak        |
|    0.8577|     36.86|        0.4376|   56.30|      0.5880| -896.62|1779.89| 685.27|      1021.93|    -108.16|    3421.69|            2814.10|gevel + dak        |
|    0.5877|     36.86|        0.3418|   56.30|      0.6119|  621.03| 972.93|-287.59|      2659.63|     928.67|    1340.71|            3970.97|ketel + gevel + dak|
|    0.7891|     36.86|        0.5213|   56.30|      0.5966| -238.12|1593.12| 886.21|      1724.03|     970.52|    3359.33|            3936.37|ketel + gevel + dak|
|    0.8360|     61.99|        0.4932|   54.90|      0.6907| -202.73|3544.20|1631.24|      3745.85|    1658.57|    6393.43|            6918.42|ketel + gevel + dak|
|    0.6811|     87.57|        0.3071|   52.80|      0.4794|  801.48|1605.15|1278.55|      3710.24|    2914.98|    4576.18|            8060.03|ketel + gevel + dak|
|    0.5062|     37.28|        0.6779|   57.80|      0.6218| 3604.88| 524.45| 542.03|      5349.13|    5692.38|    1570.92|            8333.40|ketel + gevel + dak|
|    0.6556|     83.72|        0.4378|   52.00|      0.5190| 2048.75|1636.00|2057.14|      5168.92|    5357.73|    5226.82|           10583.49|ketel + gevel + dak|
|    0.7412|     59.99|        0.4811|   56.30|      0.5254|  622.11|1854.39|1828.78|      3233.90|    3144.46|    5028.39|            7389.78|ketel + gevel + dak|
|    0.7768|     37.28|        0.3236|   52.80|      0.3816| -797.68| 523.90|   9.72|       -25.15|    -577.09|    1355.34|            1147.47|gevel + dak        |
|    0.8123|     85.77|        0.5587|   52.80|      0.4838|  242.94|2379.97|4202.08|      3139.45|    5041.57|    8558.83|           10128.41|ketel + gevel + dak|
|    0.5089|     51.41|        0.5421|   50.60|      0.4587| 2199.13| 192.06| 663.29|      3645.20|    4344.52|    1566.74|            7048.76|ketel + gevel + dak|
|    0.7310|     66.84|        0.4131|   64.60|      0.6220| 1319.09|3403.83|1888.91|      5942.42|    4018.00|    6989.00|           10729.71|ketel + gevel + dak|
|    0.6345|     29.88|        0.6373|   58.70|      0.3617|  242.10| 245.03| 438.48|       939.66|    1477.98|    1281.61|            3023.86|ketel + gevel + dak|
|    0.6691|     29.34|        0.3495|   58.70|      0.4659| -330.22| 621.32|-385.37|       788.89|    -342.26|     855.27|            1609.84|ketel + gevel + dak|
|    0.5904|     29.88|        0.6635|   58.70|      0.4264|  863.90| 269.79| 378.88|      1713.75|    2210.77|    1167.60|            3851.60|ketel + gevel + dak|
|    0.7256|     29.34|        0.3081|   58.70|      0.6452| -397.69|1344.90|-432.90|      1468.00|    -581.89|    1583.56|            2116.78|ketel + gevel + dak|
|    0.7006|     67.97|        0.3184|   85.50|      0.6090| 1819.93|4759.30|1345.78|      8476.05|    4157.41|    8292.94|           13624.30|ketel + gevel + dak|
|    0.6827|     29.88|        0.4203|   58.70|      0.6983|  302.64|1410.22|-441.75|      2427.90|     187.32|    1456.58|            2956.04|ketel + gevel + dak|
|    0.6552|     29.88|        0.3634|   58.70|      0.3510| -464.14| 247.14|-345.39|       187.97|    -390.22|     519.30|            1110.21|ketel + gevel + dak|
|    0.5874|     29.88|        0.4429|   58.70|      0.6466|  909.93| 953.19|-241.45|      2815.85|    1321.12|    1265.37|            4075.36|ketel + gevel + dak|
|    0.5936|     29.88|        0.6486|   58.70|      0.3738|  550.19| 209.13| 346.97|      1299.04|    1833.61|    1115.64|            3430.78|ketel + gevel + dak|
|    0.6142|     29.88|        0.5009|   58.70|      0.3017| -182.21|  36.77| -17.48|       260.93|     474.95|     598.24|            1766.42|ketel + gevel + dak|
|    0.8694|     66.80|        0.6902|   64.60|      0.4252| -679.60|1555.60|5342.44|       996.53|    4907.60|    8509.44|            8251.82|gevel + dak        |
|    0.5042|     66.80|        0.6839|   64.60|      0.4747| 6249.20| 434.28|2383.23|      8492.70|   11771.13|    3788.58|           15747.99|ketel + gevel + dak|
|    0.7588|     29.56|        0.5724|   58.70|      0.4656| -322.65| 819.71| 557.68|       803.59|     611.86|    2084.96|            2577.34|ketel + gevel + dak|
|    0.7143|     29.88|        0.5937|   58.70|      0.4564|  -14.37| 699.88| 531.29|      1084.90|    1036.47|    1904.48|            2984.06|ketel + gevel + dak|
|    0.8755|     29.56|        0.6940|   58.70|      0.4931|-1004.25| 742.75|1365.06|      -217.48|     440.20|    2744.75|            1881.76|gevel + dak        |
|    0.7885|     66.84|        0.4466|   64.60|      0.5481|  382.69|3142.60|2470.89|      4234.05|    3431.13|    7443.23|            9370.87|ketel + gevel + dak|
|    0.7588|     56.86|        0.6471|   62.84|      0.3189|  198.95| 731.48|3143.18|      1362.81|    4219.37|    5331.69|            7111.38|ketel + gevel + dak|
|    0.5326|     25.87|        0.4852|   55.70|      0.4903|  492.02| 286.59|-392.06|      1476.10|     790.20|     306.94|            2471.21|ketel + gevel + dak|
|    0.5785|     65.71|        0.5327|   59.50|      0.6090| 4279.21|1861.08|1749.83|      8197.40|    7828.44|    4826.33|           13637.62|ketel + gevel + dak|
|    0.7904|     65.71|        0.3684|   59.50|      0.3475| -462.79|1045.91|1571.11|       983.38|    1532.55|    4277.68|            4869.72|ketel + gevel + dak|
|    0.7462|     25.87|        0.4133|   55.70|      0.6725| -372.10|1218.43|-332.58|      1246.91|    -486.14|    1398.70|            1751.47|ketel + gevel + dak|
|    0.5051|     25.87|        0.6545|   55.70|      0.6694| 2149.25| 555.40|-236.65|      3705.11|    2816.18|     664.02|            4987.22|ketel + gevel + dak|
|    0.7592|     65.71|        0.4349|   59.50|      0.5151|  457.00|2268.65|1981.46|      3487.61|    3081.80|    5845.26|            8003.39|ketel + gevel + dak|
|    0.7068|     25.87|        0.3485|   55.70|      0.5438| -491.22| 763.77|-438.74|       679.30|    -669.26|     872.37|            1198.19|ketel + gevel + dak|
|    0.5167|     65.71|        0.5852|   59.50|      0.5113| 4824.64| 935.46|1688.69|      7819.23|    8869.86|    3709.72|           13755.43|ketel + gevel + dak|
|    0.6353|     25.87|        0.6602|   55.70|      0.3886|  114.74| 182.64| 231.53|       675.28|    1022.92|     880.97|            2244.75|ketel + gevel + dak|
|    0.5022|     25.87|        0.3904|   55.70|      0.4780|  237.10| 204.97|-633.41|      1178.28|     205.03|     -39.56|            1843.15|ketel + gevel + dak|
|    0.6015|     25.87|        0.6025|   55.70|      0.5552|  733.37| 568.49|  10.65|      1943.60|    1440.51|    1044.89|            3347.68|ketel + gevel + dak|
|    0.7704|     25.87|        0.3034|   55.70|      0.4268| -875.05| 548.71|-487.68|      -112.10|   -1210.45|     657.57|             249.43|gevel + dak        |
|    0.8343|     25.87|        0.3464|   55.70|      0.5543| -955.76|1066.05|-273.50|       251.30|   -1141.13|    1438.60|             762.86|gevel + dak        |
|    0.6878|     65.71|        0.4950|   59.50|      0.6892| 2603.00|3140.02|1387.41|      7279.69|    4877.53|    5689.10|           11074.35|ketel + gevel + dak|
|    0.8522|     65.71|        0.6894|   59.50|      0.5218| -295.79|1910.46|4684.52|      1825.26|    4735.29|    8032.39|            8374.45|ketel + gevel + dak|
|    0.7614|     25.87|        0.3603|   55.70|      0.4789| -736.98| 687.50|-330.33|       207.54|    -873.95|     946.77|             767.51|gevel + dak        |
|    0.8812|     74.26|        0.6962|   36.00|      0.3353|-1042.44|-447.12|3507.06|     -1454.76|    2558.58|    4033.39|            3140.48|gevel + dak        |
|    0.5879|     25.87|        0.4367|   55.70|      0.5123|  151.88| 441.80|-398.41|      1212.78|     281.22|     498.64|            2039.05|ketel + gevel + dak|
|    0.7016|     43.97|        0.5057|   47.44|      0.5022|  212.08| 743.44| 802.41|      1514.02|    1576.88|    2332.28|            3887.68|ketel + gevel + dak|

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
kiezen we voor iedere woning de beste maatregelcombinatie. We sorteren de woning op basis van de
besparing die de gekozen maatregelcombinatie oplevert. Dan selecteren we van deze gesorteerde lijst
met woningen totdat het budget op is.

### Resultaten

In [bin/budget_verdelen.py](https://github.com/Conengmo/case-huizen-isolatiewaarden/blob/main/bin/budget_verdelen.py)
is de beschreven methode geimplementeerd. Ik heb een budget aangenomen van € 100,000. De resultaten
zijn in de tabel hieronder te zien. De eerste kolommen bevatten de woningdata. Daarna volgen de
netto besparingen per maatregelcombinatie. De laatste kolom bevat welke maatregelen zijn gekozen
binnen het budget.

De totale netto besparing is € 290,106 na aftrek van € 99,926 aan kosten.

Huizen met grote gevels en daken krijgen eerder een isolatieupgrade, dat lijkt intuitief.

Wat opvalt is dat met de huidige formule grotere getallen lijken te worden bevoordeeld. Hierdoor
worden huizen die al goed presteren nog verder geupgrade ten koste van huizen die een mindere
uitgangspositie hebben.

Woning nummer 71 heeft maar een hele kleine upgrade gehad, dat komt omdat deze als laatste is
geselecteerd om het budget nog zoveel mogelijk vol te maken.

|   |ketel eff.|gevel opp.|gevel isolatie|dak opp.|dak isolatie|      gekozen      |iso.w. voor|iso.w. na|
|--:|---------:|---------:|-------------:|-------:|-----------:|-------------------|----------:|--------:|
|  1|    0.6551|     40.29|        0.6231|   54.50|      0.5741|                   |       0.26|         |
|  2|    0.8669|     59.99|        0.3220|   56.30|      0.4406|                   |       0.21|         |
|  3|    0.5485|     61.38|        0.3957|   54.50|      0.5886|                   |       0.21|         |
|  4|    0.5627|     33.77|        0.5478|   52.00|      0.4053|                   |       0.11|         |
|  5|    0.6489|     33.77|        0.3265|   52.00|      0.3065|                   |       0.06|         |
|  6|    0.5442|     84.13|        0.5502|   52.00|      0.4634|ketel + gevel + dak|       0.30|     0.98|
|  7|    0.7261|     36.86|        0.5067|   56.30|      0.3299|                   |       0.13|         |
|  8|    0.7735|     36.86|        0.4337|   56.30|      0.5320|                   |       0.19|         |
|  9|    0.7861|     61.99|        0.6007|   54.90|      0.4604|                   |       0.37|         |
| 10|    0.5684|     87.57|        0.5958|   52.80|      0.4588|ketel + gevel + dak|       0.36|     1.09|
| 11|    0.7426|     37.28|        0.6992|   57.80|      0.5356|                   |       0.30|         |
| 12|    0.8137|     83.72|        0.6993|   52.00|      0.4556|                   |       0.56|         |
| 13|    0.8006|     59.99|        0.6474|   56.30|      0.4046|                   |       0.35|         |
| 14|    0.8103|     37.28|        0.4886|   52.80|      0.5386|                   |       0.21|         |
| 15|    0.7054|     85.77|        0.3888|   52.80|      0.6377|ketel + gevel + dak|       0.40|     1.01|
| 16|    0.8554|     51.41|        0.5931|   50.60|      0.6933|                   |       0.46|         |
| 17|    0.5708|     29.88|        0.4430|   58.70|      0.5338|                   |       0.12|         |
| 18|    0.8495|     29.34|        0.6195|   58.70|      0.4958|                   |       0.22|         |
| 19|    0.7324|     29.88|        0.6918|   58.70|      0.4050|                   |       0.18|         |
| 20|    0.8188|     33.51|        0.6508|   62.20|      0.5622|                   |       0.31|         |
| 21|    0.7007|     36.42|        0.4831|   62.20|      0.5853|                   |       0.22|         |
| 22|    0.5939|     29.34|        0.4839|   58.70|      0.6011|                   |       0.15|         |
| 23|    0.6772|     29.88|        0.3692|   58.70|      0.3409|                   |       0.07|         |
| 24|    0.5783|     29.34|        0.4260|   58.70|      0.3213|                   |       0.07|         |
| 25|    0.7322|     29.88|        0.3980|   58.70|      0.4515|                   |       0.12|         |
| 26|    0.7736|     63.10|        0.3909|   64.60|      0.3934|                   |       0.24|         |
| 27|    0.8152|     67.97|        0.6665|   85.50|      0.5420|ketel + gevel + dak|       0.86|     1.65|
| 28|    0.8036|     29.88|        0.5437|   58.70|      0.4809|                   |       0.18|         |
| 29|    0.6615|     29.88|        0.4534|   58.70|      0.6028|                   |       0.16|         |
| 30|    0.5843|     29.88|        0.3067|   58.70|      0.5197|                   |       0.08|         |
| 31|    0.6341|     29.88|        0.6727|   58.70|      0.3319|                   |       0.12|         |
| 32|    0.7219|     29.88|        0.5394|   58.70|      0.4901|                   |       0.17|         |
| 33|    0.7507|     66.80|        0.3258|   64.60|      0.4553|                   |       0.24|         |
| 34|    0.7659|     66.80|        0.6525|   64.60|      0.6947|ketel + gevel + dak|       0.75|     1.40|
| 35|    0.6945|     29.56|        0.6358|   58.70|      0.6885|                   |       0.26|         |
| 36|    0.7982|     29.88|        0.6197|   58.70|      0.5658|                   |       0.25|         |
| 37|    0.5939|     29.56|        0.5996|   58.70|      0.3013|                   |       0.09|         |
| 38|    0.7262|     66.84|        0.4947|   64.60|      0.3511|                   |       0.27|         |
| 39|    0.5974|     56.86|        0.4965|   62.84|      0.6968|ketel + gevel + dak|       0.37|     0.95|
| 40|    0.5754|     25.27|        0.5121|   56.90|      0.3827|                   |       0.08|         |
| 41|    0.7213|     53.34|        0.5318|   49.32|      0.3595|                   |       0.18|         |
| 42|    0.8353|     67.21|        0.5235|   49.10|      0.6668|                   |       0.48|         |
| 43|    0.6943|     67.21|        0.3670|   49.10|      0.5743|                   |       0.24|         |
| 44|    0.6542|     67.21|        0.4432|   49.10|      0.3497|                   |       0.17|         |
| 45|    0.8621|     53.34|        0.5204|   49.32|      0.4376|                   |       0.26|         |
| 46|    0.7068|     42.81|        0.5543|    0.00|      0.5211|                   |       0.42|         |
| 47|    0.6071|     64.47|        0.3969|    0.00|      0.4104|                   |       0.39|         |
| 48|    0.6022|     42.58|        0.6582|    0.00|      0.4694|                   |       0.42|         |
| 49|    0.8729|     66.24|        0.5516|    0.00|      0.6635|gevel              |       0.80|     1.09|
| 50|    0.6466|     40.50|        0.3460|   71.98|      0.3912|                   |       0.13|         |
| 51|    0.5291|     64.16|        0.4527|   71.98|      0.5722|ketel + gevel + dak|       0.32|     1.05|
| 52|    0.5836|     66.47|        0.6960|    0.00|      0.4197|ketel + gevel      |       0.68|     1.27|
| 53|    0.5321|     42.81|        0.4474|    0.00|      0.3488|                   |       0.25|         |
| 54|    0.7436|     66.24|        0.4083|    0.00|      0.3366|                   |       0.50|         |
| 55|    0.6617|     42.58|        0.5134|    0.00|      0.4860|                   |       0.36|         |
| 56|    0.5452|     64.16|        0.4489|   71.98|      0.4815|ketel + gevel + dak|       0.27|     0.92|
| 57|    0.5587|     40.50|        0.3365|   71.98|      0.5225|                   |       0.14|         |
| 58|    0.6791|     34.18|        0.5584|    0.00|      0.6866|                   |       0.32|         |
| 59|    0.6898|      9.93|        0.3886|    0.00|      0.5980|                   |       0.07|         |
| 60|    0.7447|      9.93|        0.5386|    0.00|      0.5523|                   |       0.10|         |
| 61|    0.8895|     33.49|        0.6429|    0.00|      0.3101|                   |       0.48|         |
| 62|    0.8529|     32.88|        0.6317|    0.00|      0.6565|                   |       0.44|         |
| 63|    0.8418|     34.18|        0.5233|    0.00|      0.5951|                   |       0.38|         |
| 64|    0.7448|     32.05|        0.3526|    0.00|      0.5666|                   |       0.21|         |
| 65|    0.5452|      8.49|        0.5527|    0.00|      0.3927|                   |       0.06|         |
| 66|    0.5135|      8.49|        0.5430|    0.00|      0.5497|                   |       0.06|         |
| 67|    0.7637|     32.05|        0.3946|    0.00|      0.3372|                   |       0.24|         |
| 68|    0.7338|     31.44|        0.4318|    0.00|      0.3658|                   |       0.25|         |
| 69|    0.8462|     32.05|        0.6891|    0.00|      0.5279|                   |       0.47|         |
| 70|    0.8448|     32.05|        0.3192|    0.00|      0.4254|                   |       0.22|         |
| 71|    0.8901|      8.49|        0.4505|    0.00|      0.6369|gevel              |       0.09|     0.12|
| 72|    0.6048|      8.49|        0.4672|    0.00|      0.3878|                   |       0.06|         |
| 73|    0.8728|     32.05|        0.6909|    0.00|      0.5544|                   |       0.48|         |
| 74|    0.8282|     31.44|        0.5079|    0.00|      0.6509|                   |       0.33|         |
| 75|    0.7560|     32.05|        0.4795|    0.00|      0.6820|                   |       0.29|         |
| 76|    0.6226|     29.73|        0.3851|   55.64|      0.6245|                   |       0.12|         |
| 77|    0.5553|     59.66|        0.4196|    0.00|      0.6413|                   |       0.35|         |
| 78|    0.7785|     59.66|        0.6052|    0.00|      0.5954|                   |       0.70|         |
| 79|    0.7909|     29.73|        0.3918|   55.64|      0.4946|                   |       0.13|         |
| 80|    0.7839|     31.44|        0.3097|   55.64|      0.5032|                   |       0.11|         |
| 81|    0.6922|     29.73|        0.6649|   55.64|      0.6105|                   |       0.23|         |
| 82|    0.8478|     75.81|        0.3947|   61.74|      0.4957|                   |       0.39|         |
| 83|    0.5652|     29.37|        0.5859|   53.84|      0.5262|                   |       0.14|         |
| 84|    0.5582|     29.37|        0.6188|   53.84|      0.6193|                   |       0.17|         |
| 85|    0.6316|     29.37|        0.6650|   53.84|      0.6290|                   |       0.21|         |
| 86|    0.7896|     75.81|        0.3459|   61.74|      0.3043|                   |       0.19|         |
| 87|    0.6686|     29.37|        0.6147|   53.84|      0.5779|                   |       0.19|         |
| 88|    0.8602|     29.37|        0.5847|   53.84|      0.4195|                   |       0.17|         |
| 89|    0.8436|     29.37|        0.3961|   53.84|      0.5339|                   |       0.14|         |
| 90|    0.6404|     29.37|        0.4735|   53.84|      0.4934|                   |       0.12|         |
| 91|    0.8690|     29.37|        0.6915|   54.04|      0.6724|                   |       0.32|         |
| 92|    0.6206|     29.37|        0.6491|   54.04|      0.4823|                   |       0.15|         |
| 93|    0.7398|     29.37|        0.3282|   54.04|      0.4061|                   |       0.08|         |
| 94|    0.8016|     29.37|        0.3332|   54.04|      0.6226|                   |       0.13|         |
| 95|    0.8480|     75.80|        0.3222|   61.73|      0.3445|                   |       0.22|         |
| 96|    0.8823|     75.81|        0.6417|   61.73|      0.4889|gevel + dak        |       0.65|     1.20|
| 97|    0.8672|     29.37|        0.6985|   54.04|      0.3260|                   |       0.16|         |
| 98|    0.7235|     29.37|        0.5614|   54.04|      0.3366|                   |       0.11|         |
| 99|    0.5810|     29.37|        0.6962|   54.04|      0.3644|                   |       0.12|         |
|100|    0.7661|     36.86|        0.4784|   56.30|      0.4849|                   |       0.18|         |
|101|    0.6911|     36.86|        0.3399|   56.30|      0.6824|                   |       0.17|         |
|102|    0.8038|     36.86|        0.3735|   56.30|      0.4016|                   |       0.13|         |
|103|    0.5874|     87.97|        0.4057|   57.80|      0.6968|ketel + gevel + dak|       0.42|     1.18|
|104|    0.5653|     37.28|        0.5349|   52.80|      0.6900|                   |       0.21|         |
|105|    0.5017|     61.44|        0.4755|   52.80|      0.4393|                   |       0.17|         |
|106|    0.6087|     87.97|        0.6482|   57.80|      0.5797|ketel + gevel + dak|       0.58|     1.51|
|107|    0.7859|     40.29|        0.6981|   54.50|      0.4874|                   |       0.29|         |
|108|    0.5560|     59.99|        0.5974|   56.30|      0.3319|                   |       0.19|         |
|109|    0.6278|     61.38|        0.3525|   54.50|      0.4523|                   |       0.17|         |
|110|    0.5481|     33.77|        0.5107|   52.00|      0.5791|                   |       0.14|         |
|111|    0.7032|     33.77|        0.3143|   52.00|      0.5464|                   |       0.11|         |
|112|    0.5440|     84.13|        0.5323|   52.00|      0.5810|ketel + gevel + dak|       0.37|     1.13|
|113|    0.8242|     36.86|        0.5773|   56.30|      0.3774|                   |       0.19|         |
|114|    0.5011|     61.43|        0.5934|   57.80|      0.5018|ketel + gevel + dak|       0.26|     0.89|
|115|    0.8647|     37.28|        0.5365|   52.80|      0.3621|                   |       0.17|         |
|116|    0.8577|     36.86|        0.4376|   56.30|      0.5880|                   |       0.23|         |
|117|    0.5877|     36.86|        0.3418|   56.30|      0.6119|                   |       0.13|         |
|118|    0.7891|     36.86|        0.5213|   56.30|      0.5966|                   |       0.25|         |
|119|    0.8360|     61.99|        0.4932|   54.90|      0.6907|                   |       0.48|         |
|120|    0.6811|     87.57|        0.3071|   52.80|      0.4794|                   |       0.23|         |
|121|    0.5062|     37.28|        0.6779|   57.80|      0.6218|                   |       0.23|         |
|122|    0.6556|     83.72|        0.4378|   52.00|      0.5190|ketel + gevel + dak|       0.32|     0.90|
|123|    0.7412|     59.99|        0.4811|   56.30|      0.5254|                   |       0.32|         |
|124|    0.7768|     37.28|        0.3236|   52.80|      0.3816|                   |       0.09|         |
|125|    0.8123|     85.77|        0.5587|   52.80|      0.4838|                   |       0.50|         |
|126|    0.5089|     51.41|        0.5421|   50.60|      0.4587|                   |       0.16|         |
|127|    0.7310|     66.84|        0.4131|   64.60|      0.6220|ketel + gevel + dak|       0.41|     0.98|
|128|    0.6345|     29.88|        0.6373|   58.70|      0.3617|                   |       0.13|         |
|129|    0.6691|     29.34|        0.3495|   58.70|      0.4659|                   |       0.09|         |
|130|    0.5904|     29.88|        0.6635|   58.70|      0.4264|                   |       0.15|         |
|131|    0.7256|     29.34|        0.3081|   58.70|      0.6452|                   |       0.12|         |
|132|    0.7006|     67.97|        0.3184|   85.50|      0.6090|ketel + gevel + dak|       0.39|     1.10|
|133|    0.6827|     29.88|        0.4203|   58.70|      0.6983|                   |       0.18|         |
|134|    0.6552|     29.88|        0.3634|   58.70|      0.3510|                   |       0.07|         |
|135|    0.5874|     29.88|        0.4429|   58.70|      0.6466|                   |       0.15|         |
|136|    0.5936|     29.88|        0.6486|   58.70|      0.3738|                   |       0.13|         |
|137|    0.6142|     29.88|        0.5009|   58.70|      0.3017|                   |       0.08|         |
|138|    0.8694|     66.80|        0.6902|   64.60|      0.4252|                   |       0.55|         |
|139|    0.5042|     66.80|        0.6839|   64.60|      0.4747|ketel + gevel + dak|       0.35|     1.11|
|140|    0.7588|     29.56|        0.5724|   58.70|      0.4656|                   |       0.18|         |
|141|    0.7143|     29.88|        0.5937|   58.70|      0.4564|                   |       0.17|         |
|142|    0.8755|     29.56|        0.6940|   58.70|      0.4931|                   |       0.26|         |
|143|    0.7885|     66.84|        0.4466|   64.60|      0.5481|                   |       0.42|         |
|144|    0.7588|     56.86|        0.6471|   62.84|      0.3189|                   |       0.28|         |
|145|    0.5326|     25.87|        0.4852|   55.70|      0.4903|                   |       0.09|         |
|146|    0.5785|     65.71|        0.5327|   59.50|      0.6090|ketel + gevel + dak|       0.37|     1.04|
|147|    0.7904|     65.71|        0.3684|   59.50|      0.3475|                   |       0.20|         |
|148|    0.7462|     25.87|        0.4133|   55.70|      0.6725|                   |       0.15|         |
|149|    0.5051|     25.87|        0.6545|   55.70|      0.6694|                   |       0.16|         |
|150|    0.7592|     65.71|        0.4349|   59.50|      0.5151|                   |       0.33|         |
|151|    0.7068|     25.87|        0.3485|   55.70|      0.5438|                   |       0.10|         |
|152|    0.5167|     65.71|        0.5852|   59.50|      0.5113|ketel + gevel + dak|       0.30|     0.98|
|153|    0.6353|     25.87|        0.6602|   55.70|      0.3886|                   |       0.12|         |
|154|    0.5022|     25.87|        0.3904|   55.70|      0.4780|                   |       0.07|         |
|155|    0.6015|     25.87|        0.6025|   55.70|      0.5552|                   |       0.14|         |
|156|    0.7704|     25.87|        0.3034|   55.70|      0.4268|                   |       0.07|         |
|157|    0.8343|     25.87|        0.3464|   55.70|      0.5543|                   |       0.12|         |
|158|    0.6878|     65.71|        0.4950|   59.50|      0.6892|ketel + gevel + dak|       0.46|     1.04|
|159|    0.8522|     65.71|        0.6894|   59.50|      0.5218|                   |       0.60|         |
|160|    0.7614|     25.87|        0.3603|   55.70|      0.4789|                   |       0.09|         |
|161|    0.8812|     74.26|        0.6962|   36.00|      0.3353|                   |       0.27|         |
|162|    0.5879|     25.87|        0.4367|   55.70|      0.5123|                   |       0.09|         |
|163|    0.7016|     43.97|        0.5057|   47.44|      0.5022|                   |       0.19|         |


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
