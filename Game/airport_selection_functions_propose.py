import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='eliasellu',
         password='Koira123',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )
#Tää funktio hakee 20 random kenttää ja saa sen nimen, maan ja leveys/pituuspiirit geopyy varten
def airportselection(valiaikainen):
    sql = (f" Select name "
           f" from airport "
           f" where type = 'large_airport'"
           f" order by rand()"
           f" limit 20 ")
    #kursori = yhteys.cursor(dictionary=true), muuttaa tuplen sijasta dictionaryks. Eli lista, jonka sisällä dictionary
    #kantsii käyttä jos useampi select (vaikka select name, ident, id...) ja muuttamalla select arvoja ei muuta printtiä
    #näi voi callaa avaimilla mm result['name']
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    print(result[0])
    print(result[1])
    for i in range(len(result)):
        print(result[i]["name"])
    return result
airportselection(0)
#tää funktio määrittää hinnan etäisyyksien perusteella
#def distance():
    #tähän sit jotai geopyjutskaa
    #mm. dist = distance.distance(CURRENT_AIRPORT, AIRPORT_FROM_LIST).km (jos haluu kilsoina)

#ICAO1 = input("Insert first ICAO code: ")
#ICAO2 = input("Insert second ICAO code: ")
#airport1 = cordinate(ICAO1)
#airport2 = cordinate(ICAO2)
#dist = distance.distance(airport1, airport2).km
#print(f"Lentokenttien etäisyys on {dist:.2f} km.")