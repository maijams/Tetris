# Arkkitehtuurikuvaus

## Rakenne

Käyttöliittymään liittyvät tiedostot on pakattu ui-hakemistoon. Sovelluslogiikkaan ja tietokantaan liittyvät tiedostot löytyvät src-hakemiston juuresta.

![Screenshot from 2022-12-13 23-59-51](https://user-images.githubusercontent.com/96269683/207453188-f25a476f-1b72-4f36-b904-a55f6995d420.png)


## Käyttöliittymä

Käyttöliittymä koostuu ainakin toistaiseksi yhdestä näkymästä. Näkymän toteutukseen liittyvät tiedostot sijaitsevat ui-hakemistossa.

## Sovelluslogiikka

Sovelluslogiikasta vastaavat pääasiassa luokat Tetris ja Block. Toimintoja ohjaillaan käyttöliittymän kautta.

## Luokkakaavio


```mermaid
 classDiagram
    GameLoop "1" --> "1" Tetris
    GameLoop "1" --> "1" Renderer
    GameLoop "1" --> "1" ScoreBoard
    GameLoop "1" --> "1" EventQueue
    GameLoop "1" --> "1" Clock
    Renderer "1" --> "1" Tetris
    Renderer "1" --> "1" ScoreBoard
    Tetris "1" --> "1" Block
```

## Tietojen pysyväistallennus

Pelin pisteiden tallennuksesta huolehtii luokka ScoreBoard. Pistemäärä ja päivämäärä tallennetaan SQLite-tietokantaan scoreboard. ScoreBoard sisältää myös metodin tietokantahakua varten. Tietokantataulun alustukseen liittyvät koodi löytyy tiedostosta initialize_database.py.


## Päätoiminnallisuudet
### Sekvenssikaavio palikan kääntämisestä

```mermaid
sequenceDiagram
    actor User
    participant GameLoop
    participant Tetris
    participant Block

    User ->> GameLoop: press key "UP"
    GameLoop ->> Tetris: rotate()
    Tetris ->> Block: rotate()
    Block ->> Block: 
    Block -->> Tetris: 
    Tetris -->> GameLoop: 
```
