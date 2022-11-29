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
