## Viikko 3

- Pygame-kirjastolla toteutettu graafinen käyttöliittymä piirtää peliruudukon
- Aloitettu ohjelman rungon rakentaminen, lisätty/aloitettu seuraavat luokat:
    - GameLoop, vastaa pelisilmukan toteutuksesta
    - Clock, vastaa pelin ajastuksista
    - EventQueue, vastaa Pygamen tapahtumajonosta
    - Renderer, vastaa pelinäkymän piirtämisestä
    - Block, vastaa palikan toiminnallisuudesta
- Testattu Block-luokan alustusta

## Viikko 4

- Toteutettu seuraavat toiminnallisuudet:
    - Palikat putoavat vakionopeudella
    - Putoavia palikoita voidaan liikuttaa sivusuunnassa näppäinkomennoilla
    - Putoavia palikoita voidaan kääntää näppäinkomennolla
    - Palikka pysähtyy sen törmätessä seinään, lattiaan tai toiseen palikkaan
    - Rivin täyttyessä palikoista, kyseinen rivi tuhoutuu
    - Pelaaja voi nopeuttaa palikoiden putoamista näppäinkomennoilla
- Lisätty luokka Tetris, joka vastaa palikoiden käyttäytymisestä
- Lisätty luokkien Block ja Tetris testausta alustuksien ja metodien toimintaan liittyen

## Viikko 5

- Toteutettu seuraavat toiminnallisuudet:
    - Rivin täyttyessä pelaaja saa pisteitä
    - Tuhoamalla useamman rivin kerralla yhden palikan avulla, pelaaja saa ekstrapisteitä
    - Peli päättyy jos palikkapino kasvaa pelilaudan korkuiseksi
    - Pelin päättyessä pelaajan saama pistetulos tallennetaan tiedostoon
    - Pelaaja voi tarkastella aiempien pelien pistekärkeä
- Lisätty SQLite-tietokannan alustukseen liittyviä tiedostoja
- Lisätty luokkien Block, Tetris & Clock testausta uusien metodien osalta & laajennettu vanhojen testikattavuutta

## Viikko 6

- Toteutettu seuraavat toiminnallisuudet:
    - Uusi palikka ei putoa automaattisesti nopeutetulla vauhdilla vaikka 'nuoli alas' -näppäinkomento olisi jäänyt pohjaan
- Lisätty docstring-kommentit
- Tietokantaan liittyvät toiminnot eriytetty omaan Scoreboard-luokkaansa
- Käyttöliittymään liittyvät tiedostot eriytetty ui-hakemistoon

## Viikot 7 & 8

- Toteutettu seuraavat toiminnallisuudet:
    - Pistemäärän karttuessa pelaaja pääsee etenemään korkeammille leveleille. Palikoiden putoamisnopeus on sitä kovempi mitä korkeammalla levelillä ollaan
    - Pelin voi halutessaan aloittaa koska tahansa alusta (restart-toiminto)
- Korjattu bugi jossa pelin päättyessä viimeinen palikka asettui toisiksi viimeisen palikan päälle
- Lisätty testausta luokille Block, Tetris ja ScoreBoard
- Muutettu arkkitehtuuria jakamalla tiedostot services-, repositories-, ja entities-hakemistoihin