import mysql.connector
from game_texts import yhteys
from game_creation_lists.all_lists_etc import *


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
    sql = (f" CREATE TABLE makkara (id int NOT NULL auto_increment,"
           f" name VARCHAR(255) NOT NULL,"
           f" country varchar(255) NOT NULL,"
           f" score int NOT NULL,"
           f" primary key (id))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def add_makkaras_to_table(makkara, country, score):
    sql = (f"INSERT INTO makkara (name, country, score) VALUES ('{makkara}', '{country}', {score})")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


def create_makkara_reached():
    sql = (f" CREATE TABLE makkara_reached (id int NOT NULL auto_increment,"
           f" game_id int NOT NULL,"
           f" makkara_id int NOT NULL,"
           f" primary key (id))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def create_playthrough():
    sql = (f" CREATE TABLE playthrough (id int NOT NULL auto_increment,"
           f" score int NOT NULL,"
           f" money int NOT NULL,"
           f" screen_name VARCHAR(255) NOT NULL,"
           f" status VARCHAR(255) NOT NULL,"
           f" location varchar(40) NOT NULL,"
           f" mustamakkara int NOT NULL,"
           f" hole_airport varchar(255),"
           f" primary key (id))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


def create_makkaras_in_hole():
    sql = (f" CREATE TABLE makkaras_in_hole (playthrough_id int NOT NULL,"
           f" stolen_makkara_id int NOT NULL,"
           f" primary key (stolen_makkara_id))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def foreign_keys_makkara_reached():
    sql = (f" ALTER TABLE makkara_reached"
           f" ADD CONSTRAINT FK_game_id FOREIGN KEY (game_id) REFERENCES playthrough(id),"
           f" ADD CONSTRAINT FK_makkara_id foreign key (makkara_id) references makkara(id)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
#Constraintin lisäämällä teet elämästä huomattavasti helpompaa kun poistat FK yhdistelmiä. Nimi voi olla muute hankala
def foreign_keys_playthrough():
    sql = (f" ALTER TABLE playthrough "
           f" ADD CONSTRAINT FK_location"
           f" FOREIGN KEY (location) REFERENCES airport(ident),"
           f" ADD CONSTRAINT FK_hole_airport"
           f" FOREIGN KEY (hole_airport) REFERENCES airport(ident)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def foreign_keys_makkara():
    sql = (f" ALTER TABLE makkara"
           f" ADD CONSTRAINT FK_iso_country"
           f" FOREIGN KEY (country) REFERENCES country(iso_country)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def foreign_keys_makkaras_in_hole():
    sql = (f" ALTER TABLE makkaras_in_hole"
           f" ADD CONSTRAINT FK_makkara_reached_id"
           f" FOREIGN KEY (makkara_reached) REFERENCES makkara_reached(id)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def create_koloherra():
    sgl = (f" INSERT INTO playthrough (score, money, screen_name, status, location, mustamakkara)"
           f" VALUES (0, 1000, 'koloherra', 'unfinished', 'EFNU', 0)")
    kursori = yhteys.cursor()
    kursori.execute(sgl)
    return

def create_example_makkara_reached():
    sql = (f" INSERT INTO makkara_reached (game_id, makkara_id)"
           f" VALUES (1, 100)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def create_example_makkaras_in_hole(playthrough_id, stolen_makkara_id):
    sql = (f" INSERT INTO makkaras_in_hole (playthrough_id, stolen_makkara_id)"
           f" VALUES ({playthrough_id}, {stolen_makkara_id})")
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
#final_test arvoksi taululuontien määrä
final_test = 4
if test1 == 0:
    create_table_makkara()
    for i in range(len(iso_country_list)):
        add_makkaras_to_table(list(makkaras_dictionary.values())[i],iso_country_list[i],score_value_makkara[i])
    final_test -= 1
    print("t1")
    print(final_test)
makkara_reached = "makkara_reached"
test2 = table_check(makkara_reached)
if test2 == 0:
    create_makkara_reached()
    final_test -= 1
    print("t2")
    print(final_test)
playthrough = "playthrough"
test3 = table_check(playthrough)
if test3 == 0:
    create_playthrough()
    final_test -= 1
    print("t3")
    print(final_test)
makkaras_in_hole = "makkaras_in_hole"
test4 = table_check(makkaras_in_hole)
if test4 == 0:
    create_makkaras_in_hole()
    print("t4")
    final_test -= 1
if final_test == 0:
    foreign_keys_makkara_reached()
    print("fk makkara reached tehty")
    foreign_keys_playthrough()
    print("fk playthrough tehty")
    foreign_keys_makkara()
    print("fk makkara tehty")

    create_koloherra()
    print("t5")
    create_example_makkara_reached()
    create_example_makkaras_in_hole(1, 1)
    create_example_makkaras_in_hole(1,2)
    print("t6")