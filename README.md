Tässä tiedostossa esitellään pelin toiminta, tunnetut bugit ja jatkokehitysideat.

Ennen pelin käynnistämistä ensimmmäisen kerran tietokanta täytyy päivittää ajantasalle. Tietokannan pohjan saa luotua, kun uuteen tietokantaan tuo tiedoston jotain.sql.
Tämän jälkeen Game.game_texts-tiedostoon yhteys-muuttujaan täytyy vaihtaa juuri luodun tietokannan nimi, oma käyttäjätunnus ja salasana.
Puuttuvat taulut saa luotua tietokantaan ajamalla data_base_creation.py-tiedoston.

Peli käynnistetään ajamalla tiedosto Game.game.py. 
Peliä pelataan terminaalissa.


Aika ei riittänyt aivan kaiken tekemään täydelliseksi ja siksi pelissä on kehitettävää.

Tiedossa olevat bugit ja ongelmat:

1. Kun kolovastaava vie tai palauttaa makkaroita, käyttäjän pisteet eivät muutu. Pisteiden tulisi vähentyä makkaroiden lähtemisen myötä.
   Korjataan lisäämällä pelaajan pisteiden päivitys funktioihin, jotka päivittävät pelaajan makkaroiden stolen-tilan muutosta.

3. Uuden komennon luomminen vaatii komennon kirjoittamista manuaalisesti kolmeen eri paikkaan (kaksi kertaa tiedostoon game_texts ja kerran tiedostoon commands).
   Tämä on hyvin työlästä.
   Korjattaisiin mahdollisesti lisäämällä helptext comento-olion attribuutiksi. 

4. commands.py-tiedostossa on sekavasti funktioita, mutta niitä ei ehditty järjestää järkevästi circular import -virheiden takia.

5. Pelin rungosta puuttuu paljon kommentteja, koska ne unohtuivat.
   Korjattaisiin kommentoimalla runko.

Ominaisuudet, joita ei ehditty toteuttaa lainkaan:

1. Tietyn maan makkarasta saa enemmän pisteitä, kun sen ostaa ensimmäisen kerran.
2. Roskiksesta voi löytää mustamakkaran palasia, joista muodostuu kokonainen makkara.
3. Pelaaja voi komennolla nähdä luettelon kaikista keräämistään makkaroista.