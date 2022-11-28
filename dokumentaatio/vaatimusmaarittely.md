# Vaatimusmäärittely

## Sovelluksen tarkoitus

Harjoitustyön aiheena on Pygame-kirjaston avulla toteutettu klassikkopeli Tetris.  


## Perusversion tarjoama toiminnallisuus

Perusversiossa on toteutettu Tetriksen perinteiset ominaisuudet. Pelin tavoitteena on kerätä mahdollisimman paljon pisteitä muodostamalla ylhäältä putoavien palikoiden avulla täysiä palikkarivejä. Toiminnallisuuksiin kuuluu mm.:

[x] Pelilaudan koko on perinteinen 10 x 20 ruutua (L x K)
[x] Pelissä on seitsemän erilaista, neljän ruudun kokoista palikkaa (tetrominoa)
[x] Palikat putoavat vakionopeudella
[x] Putoavia palikoita voidaan liikuttaa sivusuunnassa ja kääntää näppäinkomennoilla
[ ] Rivin täyttyessä kyseinen rivi tuhoutuu ja pelaaja saa pisteitä
- Tuhoamalla useamman rivin kerralla yhden palikan avulla, pelaaja saa ekstrapisteitä
- Peli päättyy jos palikkapino kasvaa pelilaudan korkuiseksi
- Pelin päättyessä pelaajan saama pistetulos tallennetaan tiedostoon ja pelaaja voi tarkastella aiempien pelien pistekärkeä


## Jatkokehitysideoita

Perusversion jälkeen sovellusta on mahdollista laajentaa esimerkiksi seuraavilla ominaisuuksilla:

- Pelaaja voi säätää pelilaudan kokoa
- Peruspalikoiden lisäksi pelissä on myös muita erimuotoisia ja erikokoisia palikoita
- Pelaaja voi nopeuttaa palikoiden putoamista näppäinkomennoilla ja ansaita samalla lisäpisteitä
- Saatujen pisteiden määrä on riippuvainen tuhoutuneiden palikoiden väristä, väreillä voi olla esimerkiksi eri prioriteetit tai pisteitä saa sitä enemmän mitä vähemmän rivissä on erivärisiä palikoita
- Jos rivejä tuhoutuu kahdella peräkkäisellä palikalla, muodostuu kombo ja pelaaja saa lisäpisteitä
- Pistemäärän karttuessa pelaaja pääsee etenemään korkeammille leveleille. Palikoiden putoamisnopeus on sitä kovempi mitä korkeammalla levelillä ollaan
