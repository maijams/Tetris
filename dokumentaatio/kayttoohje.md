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

**Pelinäkymä:**
![Screenshot from 2022-12-25 23-54-01](https://user-images.githubusercontent.com/96269683/209482865-6f644341-b4fe-4d64-8b07-6f36d612df05.png)

**Pelin päättyminen:**
![Screenshot from 2022-12-25 23-54-33](https://user-images.githubusercontent.com/96269683/209482868-5e4f4aa4-1ffa-46c6-ac7b-b68452348493.png)

### Pelin uudelleen käynnistäminen

Pelin voi aloittaa alusta milloin tahansa painikkeella "R".

### Pelin lopettaminen

Lopeta peli sulkemalla Pygame-ikkuna oikean yläkulman rastista.
