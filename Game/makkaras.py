import mysql.connector

#Tehty toimimaan mun tietokantaan, eli pitäs lisätä funktio mikä antaa oikeudet aina kun pelataan eri koneella
# (eli pitää luoda funktio joka luo käyttäjän, hakee tietokannan ja antaa oikeudet). Toi kannattaa tarkistaa opelta
# onko tarpeellista. Se luo tablen, jonka jälkee se tekee joukon, mihin lisään jo tietokannassa olevat makkarat. Sen
# jälkee se lisää samaa joukkoon makkarat listasta. Tää estää duplikaatit.

#Tiedossa oleva ongelma: Jostai syystä aina uudestaa ajaessa lisää yhden luvun 0, 1, 2, 3...

#tämän koodin tomiakseen pitää antaa KAIKKI oikeudet tehdä muutoksia flight_game databasee
#esim käyttäen tietokantaa nimeltä flight_game "GRANT ALL ON flight_game.* TO (käyttäjänimi)@localhost;" Ja sit
#"flush privileges"
yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='eliasellu',
         password='Koira123',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )

#Luo käyttäjälle makkara tablen. Toimii vain jos käyttäjälle on annettu luvat. Ohjeet ylempänä.
def create_makkara():
    sql = (f"CREATE TABLE if not exists makkara (makkara_name VARCHAR(255) NOT NULL)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

#SQL joka hakee jo makkara taulussa olevat tiedot, ottaa meijän makkaralistan ja joukon avulla estää duplikaatit
#jostai syystä lisää joukkoon yhden numeron aina per ajokerta alkaen 0, 1, 2, 3...
def check_makkaras_duplicates(makkara_name):
    sql =(f" SELECT * from makkara ")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    makkara_check_list = set()
    for i in range(len(result)):
        makkara_check_list.add(result[i]['makkara_name'])
    for i in range(len(makkara_name)):
        makkara_check_list.add(makkara_name[i])
    for i in range(len(makkara_check_list)):
        add_makkara(i)
    print(f"tämä:\n{makkara_check_list}")
    return

#lisää joukon yks kerrallaa listaan. Joukko tulee satunnaisessa järkässä, eli jos ongelma, se pitöä muuttaa.
def add_makkara(makkara_name):
    sql = (f"INSERT ignore INTO makkara (makkara_name) VALUES ('{makkara_name}')")
    kursori = yhteys.cursor()
    kursori.execute(sql)


#tämä poistetaa pääohjelmaan. Testaa vaa että listan lisääminen toimii oikein
def testi():
    sql = (f"SELECT * FROM makkara")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    #print(result)
    return result

testilista = ["Veggienakki", "HK_sininen", "keisarinakki"]

create_makkara()
check_makkaras_duplicates(testilista)
#bring_makkaras(testilista)
testi()
#def fetch_makkara(iso_country):
#    sql = (f"select makkara.name"
#           f" FROM makkara INNER JOIN country")