# Vaatimusmäärittely

## Sovelluksen tarkoitus

Harjoitustyön aiheena on Pygame-kirjaston avulla toteutettu klassikkopeli Tetris.  


## Perusversion tarjoama toiminnallisuus

Perusversiossa on toteutettu Tetriksen perinteiset ominaisuudet. Pelin tavoitteena on kerätä mahdollisimman paljon pisteitä muodostamalla ylhäältä putoavien palikoiden avulla täysiä palikkarivejä. Toiminnallisuuksiin kuuluu mm.:

- [x] Pelilaudan koko on perinteinen 10 x 20 ruutua (L x K)
- [x] Pelissä on seitsemän erilaista, neljän ruudun kokoista palikkaa (tetrominoa)
- [x] Palikat putoavat vakionopeudella
- [x] Putoavia palikoita voidaan liikuttaa sivusuunnassa näppäinkomennoilla
- [x] Putoavia palikoita voidaan kääntää näppäinkomennolla
- [x] Palikka pysähtyy sen törmätessä seinään, lattiaan tai toiseen palikkaan
- [x] Rivin täyttyessä palikoista, kyseinen rivi tuhoutuu
- [x] Rivin täyttyessä pelaaja saa pisteitä
- [x] Tuhoamalla useamman rivin kerralla yhden palikan avulla, pelaaja saa ekstrapisteitä
- [x] Peli päättyy jos palikkapino kasvaa pelilaudan korkuiseksi
- [x] Pelin päättyessä pelaajan saama pistetulos tallennetaan tiedostoon
- [x] Pelaaja voi tarkastella aiempien pelien pistekärkeä


## Jatkokehitysideoita

Perusversion jälkeen sovellusta on mahdollista laajentaa esimerkiksi seuraavilla ominaisuuksilla:

- [ ] Pelaaja voi säätää pelilaudan kokoa
- [ ] Peruspalikoiden lisäksi pelissä on myös muita erimuotoisia ja erikokoisia palikoita
- [x] Pelaaja voi nopeuttaa palikoiden putoamista näppäinkomennoilla
- [ ] Pelaaja voi ansaita lisäpisteitä nopeuttamalla palikoiden putoamista
- [ ] Saatujen pisteiden määrä on riippuvainen tuhoutuneiden palikoiden väristä, väreillä voi olla esimerkiksi eri prioriteetit tai pisteitä saa sitä enemmän mitä vähemmän rivissä on erivärisiä palikoita
- [ ] Jos rivejä tuhoutuu kahdella peräkkäisellä palikalla, muodostuu kombo ja pelaaja saa lisäpisteitä
- [ ] Pistemäärän karttuessa pelaaja pääsee etenemään korkeammille leveleille. Palikoiden putoamisnopeus on sitä kovempi mitä korkeammalla levelillä ollaan
