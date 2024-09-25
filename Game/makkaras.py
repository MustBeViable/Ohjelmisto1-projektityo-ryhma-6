import mysql.connector

from game_texts import yhteys

#Tehty toimimaan mun tietokantaan, eli pitäs lisätä funktio mikä antaa oikeudet aina kun pelataan eri koneella
# (eli pitää luoda funktio joka luo käyttäjän, hakee tietokannan ja antaa oikeudet). Toi kannattaa tarkistaa opelta
# onko tarpeellista. Se luo tablen, jonka jälkee se tekee joukon, mihin lisään jo tietokannassa olevat makkarat. Sen
# jälkee se lisää samaa joukkoon makkarat listasta. Tää estää duplikaatit.

#Tiedossa oleva ongelma: Jostai syystä aina uudestaa ajaessa lisää yhden luvun 0, 1, 2, 3...

#tämän koodin tomiakseen pitää antaa KAIKKI oikeudet tehdä muutoksia flight_game databasee
#esim käyttäen tietokantaa nimeltä flight_game "GRANT ALL ON flight_game.* TO (käyttäjänimi)@localhost;" Ja sit
#"flush privileges"



def table_check():
    sql = (f"show tables;")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    check_list = []
    for i in range(len(result)):
        check_list.append(result[i][0])
    if "makkara" in check_list:
        print("Makkarat löytyy.")
    else:
        testilista = ["Veggienakki", "HK_sininen", "keisarinakki"]
        create_tables()
        for i in range(len(testilista)):
            add_makkara(i)
    return

#Luo käyttäjälle makkara tablen. Toimii vain jos käyttäjälle on annettu luvat. Ohjeet ylempänä.
def create_tables():
    sql = (f"CREATE TABLE makkara (name VARCHAR(255) NOT NULL)")
    sql1 = (f"CREATE TABLE makkara_located (country_id VARCHAR(255) NOT NULL, makkara_name VARCHAR(255) NOT NULL)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    kursori.execute(sql1)
    return

#lisää joukon yks kerrallaa listaan. Joukko tulee satunnaisessa järkässä, eli jos ongelma, se pitöä muuttaa.
def add_makkara(makkara_name):
    sql = (f"INSERT INTO makkara (makkara_name) VALUES ('{makkara_name}')")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


#tämä poistetaa pääohjelmaan. Testaa vaa että listan lisääminen toimii oikein
def testi():
    sql = (f"SELECT * FROM makkara")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    print(result)
    return result

table_check()


#create_makkara()
#check_makkaras_duplicates(testilista)
#bring_makkaras(testilista)
#testi()
#def fetch_makkara(iso_country):
#    sql = (f"select makkara.name"
#           f" FROM makkara INNER JOIN country")