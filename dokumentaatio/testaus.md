# Testausdokumentti

Ohjelmalle on tehty unittestilla automatisoitua yksikkö- & integraatiotestausta. Tämän lisäksi pelin toimintaa on testattu manuaalisesti.

## Yksikkö- ja integraatiotestaus

### Testikattavuus

Testattujen tiedostojen osalta testauksen haaraumakattavuus on 97%.

![Screenshot from 2022-12-25 23-42-12](https://user-images.githubusercontent.com/96269683/209482819-7e704a6b-445e-4161-ae65-459a60cc30c3.png)

Käyttöliittymään liittyvät tiedostot on jätetty testikattavuuden ulkopuolelle, suoraan testattiin luokkia Block, Tetris ja ScoreBoard. Tietokantaan liittyviä tiedostoja initialize_database.py sekä database_connection.py ei testattu suoraan vaan testaus tapahtui integroidusti ScoreBoard-luokan kautta. 

## Järjestelmätestaus

Järjestelmätestausta on tehty manuaalisesti. Määrittelydokumentiin suoritetuiksi merkatut toiminnallisuudet on testattu ohjelman käytön yhteydessä.
