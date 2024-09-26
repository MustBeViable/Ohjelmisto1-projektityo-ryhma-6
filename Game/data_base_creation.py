import mysql.connector
from game_texts import yhteys
from game_creation_lists.all_lists_etc import *
from game_creation_lists import *

#Tehty toimimaan mun tietokantaan, eli pitäs lisätä funktio mikä antaa oikeudet aina kun pelataan eri koneella
# (eli pitää luoda funktio joka luo käyttäjän, hakee tietokannan ja antaa oikeudet). Toi kannattaa tarkistaa opelta
# onko tarpeellista. Se luo tablen, jonka jälkee se tekee joukon, mihin lisään jo tietokannassa olevat makkarat. Sen
# jälkee se lisää samaa joukkoon makkarat listasta. Tää estää duplikaatit.

#Tiedossa oleva ongelma: Jostai syystä aina uudestaa ajaessa lisää yhden luvun 0, 1, 2, 3...

#tämän koodin tomiakseen pitää antaa KAIKKI oikeudet tehdä muutoksia flight_game databasee
#esim käyttäen tietokantaa nimeltä flight_game "GRANT ALL ON flight_game.* TO (käyttäjänimi)@localhost;" Ja sit
#"flush privileges"


#ei toimi for some somethingsomething reason oikein, ku laittaa valuet ja ytekee if statementin alas
def table_check():
    sql = (f"show tables;")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    check_list = []
    for i in range(len(result)):
        check_list.append(result[i][0])
        print("testi check list")
        print(check_list)
    if "makkara" in check_list:
        print("Makkarat löytyy.")
        value = 1
    else:
        create_table_makkara()
        print("t2")
        value = 0
    return value

#Luo käyttäjälle makkara tablen. Toimii vain jos käyttäjälle on annettu luvat. Ohjeet ylempänä.
def create_table_makkara():
    sql = (f"CREATE TABLE makkara (id int NOT NULL auto_increment,"
           f"name VARCHAR(255) NOT NULL,"
           f"country varchar(255) NOT NULL,"
           f"score int NOT NULL,"
           f"primary key (id))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def add_makkaras_to_table(makkara, country, score):
    sql = (f"INSERT INTO makkara (name, country, score) VALUES ('{makkara}', '{country}', {score})")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


def create_makkara_reached():
    sql1 = (f"CREATE TABLE makkara_located (country_id VARCHAR(255) NOT NULL, makkara_name VARCHAR(255) NOT NULL,"
            f" FOREIGN KEY (makkara_name) REFERENCES makkara(name), FOREIGN KEY country(name) REFERENCES country(name))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


table_check()
print(table_check())
if table_check() == 0:
    for i in range(len(iso_country_list)):
        add_makkaras_to_table(list(makkaras_dictionary.values())[i],iso_country_list[i],score_value_makkara[i])

#create_makkara()
#check_makkaras_duplicates(testilista)
#bring_makkaras(testilista)
#testi()
#def fetch_makkara(iso_country):
#    sql = (f"select makkara.name"
#           f" FROM makkara INNER JOIN country")