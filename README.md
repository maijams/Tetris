# Tetris

Kurssin Ohjelmistotekniikka harjoitustyöprojekti

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/maijams/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/maijams/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/maijams/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/maijams/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)


## Pelin asennus 

Riippuvuudet voi asentaa komennolla:
```
poetry install
```
Pelin saa käyntiin komennolla:
```
poetry run invoke start
```
Testikattavuusraportin luominen projektin htmlcov-hakemistoon:
```
poetry run invoke coverage-report
```
Pylint-tarkastuksen suorittaminen:
```
poetry run invoke lint
```