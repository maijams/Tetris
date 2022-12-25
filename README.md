# Tetris

Kurssin Ohjelmistotekniikka harjoitustyöprojekti

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/maijams/Tetris/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/maijams/Tetris/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/maijams/Tetris/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/maijams/Tetris/blob/main/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/maijams/Tetris/blob/main/dokumentaatio/testaus.md)

[Käyttöohje](https://github.com/maijams/Tetris/blob/main/dokumentaatio/kayttoohje.md)

## Viimeisin release

[Viikon 6 release](https://github.com/maijams/Tetris/releases/tag/viikko6)

## Asennus

1. Lataa viimeisin release tai kloonaa projekti koneellesi.

2. Asenna riippuvuudet ohjelman juurihakemistossa komennolla:
```
poetry install
```

3. Pelin saa käyntiin komennolla:
```
poetry run invoke start
```

## Testaus

Testikattavuusraportin generoiminen projektin htmlcov-hakemistoon:
```
poetry run invoke coverage-report
```
## Pylint
Pylint-tarkastuksen suorittaminen:
```
poetry run invoke lint
```
