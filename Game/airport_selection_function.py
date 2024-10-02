from Game.sql_querys.money_function import fetch_player_money, update_player_money
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location, update_player_location, \
    fetch_player_location_name
from game_texts import yhteys, price_multiplier

#This function tests if player input for next airport is placed correctly
def check_player_input():
    next_location = input(
        "Valitse haluamasi uusi lentokenttä syöttämällä sen järjestysluku(älä syötä yli 20 tai 0 tai pienempi): ")
    while next_location is not int and next_location not in range(1,21):
        try:
            next_location = int(next_location)
        except:
            next_location = input(
                "Syötit väärin! Valitse uudelleen haluamasi uusi lentokenttä syöttämällä sen järjestysluku: ")
            continue
        else:
            next_location = int(next_location)
        while next_location not in range(1, 21):
            next_location = input(
                "Syötit väärin! Valitse uudelleen haluamasi uusi lentokenttä syöttämällä sen järjestysluku: ")
            break
    return next_location


#Tää funktio hakee 20 random kenttää ja saa sen nimen, maan ja leveys/pituuspiirit geopyy varten
def airportselection(game_id):
    sql = (f" Select airport.name as name, country.name as country, ident "
           f" from airport, country "
           f" where country.iso_country = airport.iso_country"
           f" and airport.type = 'large_airport'"
           f" and airport.name not like 'CLICK%'"
           f" order by rand()"
           f" limit 20 ")
    #kursori = yhteys.cursor(dictionary=true), muuttaa tuplen sijasta dictionaryks. Eli lista, jonka sisällä dictionary
    #kantsii käyttä jos useampi select (vaikka select name, ident, id...) ja muuttamalla select arvoja ei muuta printtiä
    #näi voi callaa avaimilla mm result['name']
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    #tää for loop käy jokaisen dictionaryn listan sisältä ja ajaa distance funktion (selvittää etäisyyttä ks. alempaa)
    # Kun se o saanu etäisyyden se lisää arvon avaimeen 'distance'.
    #ident = fetch_player_location(identification)
    player_current_ident = current_coordinates(game_id)
    for i in range(len(result)):
        dist = distance(result[i]['ident'], player_current_ident)
        result[i]['distance'] = dist

    #tää luo uuden listan jossa lista on sortattu distance avaimella suuruus järjestykee (key=lambda lambda x määrittää
    # tavan millä järjestely tehdään. x['distance'] tarkoittaa, että jokaiselle alkion (tässä tapauksessa sanakirjan)
    # osalta otetaan. järjestelyavaimeksi sen 'distance'-arvo. X viittaayhtee sanakirjaan ja x['distance'] sen sanakirjan
    # distance avaimen arvoon.) "key=lambda tarjoaa joustavan ja yksinkertaisen tavan järjestää tai käsitellä listan
    # elementtejä räätälöidyn avaimen perusteella."
    result_sorted = sorted(result, key=lambda x: x['distance'])
    #tässä printtaan saadut tulokset uudesta listasta ja järjestän ne indeksi+1 perusteella, jotta saan tulosteen alkamaan
    # 1 ja päättymään 20. Enamurate lisää iterointiin indeksin, jossa sit käydään listan elementtejä läpi (jossa airport
    # on elementti) läpi i indeksin avulla. Samalla saadaan ulos elementin että indeksin. (1 sanakirja= erillisen
    # lentokentän nimi, maakoodi ja etäisyys avain/arvo pareina).
    money = fetch_player_money(game_id)
    print("Seuraavat lähdöt: (lennon nro, maa, lentokenttä, hinta (€):")
    for i, airport in enumerate(result_sorted):
        print(f"{i + 1:17.0f}. {airport['country']}: {airport['name']}  ({price_multiplier + i  * price_multiplier}) €)")
    print(f"Sinulla on {money}€. ")
    next_location = check_player_input()
    if money < next_location*price_multiplier:
        print("Rahasi ei riitä tälle kentälle.")
        next_location = check_player_input()
    next_airport = result_sorted[next_location-1]["ident"]
    price = (next_location)*price_multiplier
    money -= price
    update_player_money(money, game_id)
    update_player_location(game_id, next_airport)
    location_name = fetch_player_location_name(game_id)
    print(f"Saavuit lentokentälle {location_name}.")
    return next_airport

#tää funktio saa ylemmän funktion lentokenttien nimet ja laskee sen etäisyyden nykyiseen lentokenttään (käytin baselinenä
#nummelan lentokenttää. Ei tartte ku laittaa päivittää current_airport pelaajan nykyisee sijaintii.
def distance(next_place, icao):
    from geopy import distance
    sql = (f" select latitude_deg, longitude_deg "
           f" from airport "
           f" where ident = '{next_place}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    #nummelan tilalle laitetaa se kenttä mis pelaaja o sil hetkel.
    #current_airport = "EFNU"
    #current_airport = current_coordinates(current_airport)
    dist = distance.distance(icao, result[0]).km
    return dist

def current_coordinates(chosen_ICAO):
    sql = (f" select latitude_deg, longitude_deg "
           f" from airport "
           f" where ident = '{chosen_ICAO}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    return result

airportselection(1)
'''
airportselection(test_playthrough.location)

print(test_playthrough.location)
airportselection(test_playthrough.location)
print(test_playthrough.location)
'''