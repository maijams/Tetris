# Käyttöohje

## Asennus

Lataa viimeisin release tai kloonaa projekti koneellesi.

Asenna riippuvuudet ohjelman juurihakemistossa komennolla:
```
poetry install
```
## Pelin käynnistäminen

Pelin saa käyntiin komennolla:
```
poetry run invoke start
```

## Pelaaminen

Peli noudattaa klassikkopelin Tetris säännöstöä. Tavoitteena on kerätä mahdollisimman paljon pisteitä sijoittamalla pelissä putoavat palikat siten että ne muodostavat mahdollisimman paljon täysiä vaakarivejä. Kun vaakarivi täyttyy palikoista, kyseinen rivi tuhoutuu ja pelaaja saa pisteitä. Peli päättyy jos palikkapino pääsee kasvamaan peliruudukon korkuiseksi. Pelin päätyttyä ruudulle ilmestyy top 10 high score -taulukko.

### Näppäinkomennot

- nuoli vasen = liikuta palikkaa vasemmalle
- nuoli oikea = liikuta palikkaa oikealle
- nuoli ylös = käännä palikkaa
- nuoli alas = nopeuta palikan putoamista

### Pelin lopettaminen

Lopeta peli sulkemalla Pygame-ikkuna oikean yläkulman rastista.
