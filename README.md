# Tetris

Kurssin Ohjelmistotekniikka harjoitustyöprojekti

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/maijams/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/maijams/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/maijams/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/maijams/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/maijams/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

## Viimeisin release

[Viikon 6 release](https://github.com/maijams/ot-harjoitustyo/releases/tag/viikko5)

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
