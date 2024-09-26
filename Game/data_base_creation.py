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

def table_check(table_name):
    sql = (f"show tables;")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    check_list = []
    for i in range(len(result)):
        check_list.append(result[i][0])
    if table_name in check_list:
        value = 1
    else:
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
    sql = (f"CREATE TABLE makkara_located (id int NOT NULL auto_increment,"
           f"game_id VARCHAR(255) NOT NULL,"
           f" makkara_id VARCHAR(255) NOT NULL,"
           f"primary key (id))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def create_playthrough():
    sql = (f"CREATE TABLE playthrough (id int NOT NULL auto_increment,"
           f"score int NOT NULL,"
           f"money VARCHAR(255) NOT NULL,"
           f"screen_name VARCHAR(255) NOT NULL,"
           f"status VARCHAR(255) NOT NULL,"
           f"location VARCHAR(255) NOT NULL,"
           f"primary key (id))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

'''test_list = ["makkara", "makkara_reached", "playthrough"]
tests_ran = 0

while tests_ran != len(test_list):
    table_name = test_list[tests_ran]
    
    '''
makkara = "makkara"
test1 = table_check(makkara)
if test1 == 0:
    create_table_makkara()
    for i in range(len(iso_country_list)):
        add_makkaras_to_table(list(makkaras_dictionary.values())[i],iso_country_list[i],score_value_makkara[i])
makkara_reached = "makkara_reached"
test2 = table_check(makkara_reached)
if test2 == 0:
    create_makkara_reached()
playthrough = "playthrough"
test3 = table_check(playthrough)
if test3 == 0:
    create_playthrough()