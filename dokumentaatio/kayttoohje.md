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

Pelinäkymä:
![Screenshot from 2022-12-13 23-10-25](https://user-images.githubusercontent.com/96269683/207453381-26fecb87-c7a3-4b31-9676-6aab4b8372e5.png)

Pelin päättyminen:
![Screenshot from 2022-12-13 23-11-13](https://user-images.githubusercontent.com/96269683/207453444-fd4388b6-f848-4b02-a5a4-ce0a6149d806.png)


### Näppäinkomennot

- nuoli vasen = liikuta palikkaa vasemmalle
- nuoli oikea = liikuta palikkaa oikealle
- nuoli ylös = käännä palikkaa
- nuoli alas = nopeuta palikan putoamista

### Pelin lopettaminen

Lopeta peli sulkemalla Pygame-ikkuna oikean yläkulman rastista.
