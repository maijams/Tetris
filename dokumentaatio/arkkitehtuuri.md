# Arkkitehtuurikuvaus

## Rakenne

Ohjelman pakkausrakenne:

![Screenshot from 2022-12-25 21-58-33](https://user-images.githubusercontent.com/96269683/209480561-9f5eace3-c3ef-46fd-83f8-6f22ddd48f5f.png)

Käyttöliittymään liittyvät tiedostot on pakattu ui-hakemistoon. Sovelluslogiikasta huolehtii services-hakemiston sisältö ja tietokantaan tallentamisesta repositories-hakemiston sisältö. Entities-hakemiston Block-luokka kuvastaa sovelluksen aktiivista muuttujaa ja sisältää myös sovelluslogiikkaa.

## Käyttöliittymä

Käyttöliittymä sisältää pelinäkymän sekä lopetusnäkymän, jossa pelinäkymään tulostuu lista pelin piste-ennätyksistä. Käyttöliittymään liittyvät tiedostot on eristetty [ui](https://github.com/maijams/Tetris/tree/main/src/ui)-hakemistoon, josta ne kutstuvat [services](https://github.com/maijams/Tetris/tree/main/src/services)-hakemiston sovelluslogiikasta vastaavaa luokkaa [Tetris](https://github.com/maijams/Tetris/blob/main/src/services/tetris.py). Kun peli päättyy, ohjelma siirtyy lopetusnäkymään.

## Sovelluslogiikka

Sovelluslogiikasta vastaavat pääasiassa luokat Tetris ja Block. Toimintoja ohjaillaan käyttöliittymän kautta. Block huolehtii putoavan palikan tiedoista ja Tetris pelitilanteesta.

```mermaid
 classDiagram
    Tetris "1" --> "1" Block
class Tetris{
          height
          width
          state
          block
          field
          points
          level
      }
class Block{
          pos_x
          pos_y
          shape
          rotation
          color
      }
```

Luokan Tetris metodeja ovat seuraavat:
- `new_block()`
- `move_down()`
- `move_sideways(direction)`
- `rotate()`
- `collision()`
- `freeze()`
- `remove_rows()`
- `update_level()`

Luokan Block metodeja taas seuraavat:
- `rotate()`
- `reverse_rotate()`
- `figure()`
- `move_down()`
- `move_up()`
- `move_sideways(direction)`
- `set_horizontal_position(pos_x)`


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

Luokka GameLoop kutsuu muita käyttöliittymästä vastaavia luokkia Clock, EventQueue ja Renderer, sekä sovelluslogiikasta vastaavaa luokkaa Tetris ja tietojen pysyväistallennuksesta vastaavaa luokkaa ScoreBoard. Tetris kutsuu aktiivisesta palikasta vastaavaa luokkaa Block ja pelin renderöinnistä vastaava luokka Renderer kutsuu luokkaa ScoreBoard tulostaessaan lopetusnäkymän high score -listan.

## Tietojen pysyväistallennus

Pelin pisteiden tallennuksesta huolehtii repositories-hakemiston luokka [ScoreBoard](https://github.com/maijams/Tetris/blob/main/src/repositories/scoreboard.py). Päättyneen pelin pistemäärä ja päivämäärä tallennetaan SQLite-tietokantatauluun `scoreboard`, mikäli pistemäärä on enemmän kuin nolla pistettä. ScoreBoard sisältää myös metodin tietokantahakua varten. Tietokantataulun alustukseen liittyvät koodi löytyy tiedostosta initialize_database.py ja tietokantayhteyden muodostamisesta vastaa tiedosto database_connection.py

## Päätoiminnallisuudet
### Putoavan palikan kääntäminen

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

### Putoavan palikan liikuttaminen sivusuunnassa

```mermaid
sequenceDiagram
    actor User
    participant GameLoop
    participant Tetris
    participant Block

    User ->> GameLoop: press key "LEFT"
    GameLoop ->> Tetris: move_sideways(-1)
    Tetris ->> Block: move_sideways(-1)
    Block ->> Block: 
    Block -->> Tetris: 
    Tetris -->> GameLoop: 
```


