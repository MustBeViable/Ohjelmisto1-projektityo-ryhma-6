Tässä tiedostossa esitellään pelin toiminta, tunnetut bugit ja jatkokehitysideat.

Ennen pelin käynnistämistä ensimmmäisen kerran tietokanta täytyy päivittää ajantasalle. Tietokannan pohjan saa luotua, kun uuteen tietokantaan tuo tiedoston jotain.sql.
Tämän jälkeen Game.game_texts-tiedostoon yhteys-muuttujaan täytyy vaihtaa juuri luodun tietokannan nimi, oma käyttäjätunnus ja salasana.
Puuttuvat taulut saa luotua tietokantaan ajamalla data_base_creation.py-tiedoston.

Peli käynnistetään ajamalla tiedosto Game.game.py. 
Peliä pelataan terminaalissa.


Aika ei riittänyt aivan kaiken tekemään täydelliseksi ja siksi pelissä on kehitettävää.

Tiedossa olevat bugit ja ongelmat:

Kun kolovastaava vie tai palauttaa makkaroita, käyttäjän pisteet eivät muutu. Pisteiden tulisi vähentyä makkaroiden lähtemisen myötä.
Korjataan lisäämällä pelaajan pisteiden päivitys funktioihin, jotka päivittävät pelaajan makkaroiden stolen-tilan muutosta.

Uuden komennon luomminen vaatii komennon kirjoittamista manuaalisesti kolmeen eri paikkaan (kaksi kertaa tiedostoon game_texts ja kerran tiedostoon commands).
Tämmä on hyvin työlästä.
Korjattaisiin mahdollisesti lisäämällä helptext comento-olion attribuutiksi. 


Ominaisuudet, joita ei ehditty toteuttaa lainkaan:

Tietyn maan makkarasta saa enemmän pisteitä, kun sen ostaa ensimmäisen kerran.
Roskiksesta voi löytää mustamakkaran palasia, joista muodostuu kokonainen makkara.
Pelaaja voi komennolla nähdä luettelon kaikista keräämistään makkaroista.
