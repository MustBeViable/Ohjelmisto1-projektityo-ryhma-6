
# 10% mahis finnair_personnel, 10% mahis kolovastaavalle, 10% mahis rosvolle, 10 % musta makkara, 60% mahis voittaa rahaa

import random
from os import remove

from Game.game_texts import no, yes, game_id, yhteys
#from Game.game_texts import yhteys
from Game.player_profile import own_makkaras, own_money
from Game.secret_black_sausage import secret_black_sausage_chance, amount, own_secret_black_sausage
from Game.doubling_machine import tuplataanko
from Game.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.sql_querys.money_function import add_money, use_money



def robber(player_money, id):
    if player_money > 0:
        aft_rob = player_money * 0.5
        add_money(aft_rob, id)
        return aft_rob


# Function is calling all the "own_makkaras" list and reduces random amount of the list
def hole_in_charge():
    own_makkaras = fetch_player_makkaras(game_id)
    print("Törmäsit kolovastaavaan!")
    if len(own_makkaras) == 0:
        print("Tällä kertaa sinulla ei ollut makkaraa vietävänä.")
    else:
        # Devided by five (like 20%) and rounded down
        num_to_lose = len(own_makkaras) // 5

        # Varmistetaan, että vähintään yksi makkara otetaan
        if num_to_lose == 0 and len(own_makkaras) > 0:
            num_to_lose = 1

        # A random number of sausages (num_to_lose) is selected to remove
        lost_makkaras = random.sample(own_makkaras, num_to_lose)
        print(lost_makkaras)

        # The selected sausages are removed from original list and added to hole in charge's list
        for makkara in lost_makkaras:
            print(makkara)
            sql = (f"UPDATE makkara_reached SET stolen = True WHERE id IN (SELECT id FROM makkara_reached WHERE id = {makkara})")
            kursori = yhteys.cursor()
            kursori.execute(sql)
        print(hole_in_charge_makkaras)
        print(f"Harmi makkaravarastosi kannalta, sillä kolovastaava vei sinulta makkaroita {len(lost_makkaras)} kpl makkaroista.")
    return


# Player can donate x amount money and get vege sausage
# Player has to donate few times to get one vege sausage
def finnair_personnel():
    donate = int(input("Syötä tähän numeroina, paljonko haluat lahjoittaa rahaa: "))
    new_money = own_money - donate
    don = 0
    while donate > 0:
        don += 1
        if don < 2:
            print("Hyvä päätös! Jatka lahjoitusten tekemistä myös jatkossa niin pitkäjänteisyys palkitaan!")
        if don == 2:
            win = vege_list[0]
            vege_list.remove(win)
            own_makkaras.append(win)
            print(f"Onnittelut hyvistä päätöksistä! Pitkäjänteisyytesi ja lahjoitustesi ansiosta olet saanut harvinaisen {win} -makkaran!")
            #add_makkara_to_rached(win)
        break
    return new_money



# !!!!! Need to exchange the money to be a variable !!!!
def money_from_garbage():
    new_money = random.randint(200, 1000)
    return new_money


#Checkng garbages, saken mustamakkara funktio, kaikki roskiksen toiminnallisuudet
def garbage_can():
    id = 1
    #player_money = own_money
    #robber(player_money)
    #finnair_personnel()

    # the possibilities of different outcomes
    outcome = random.choices(['found_money', 'robber', 'hole_in_charge', 'finnair_personnel'], weights = [0, 0, 100, 0], k=1)[0]
    if outcome == 'found_money':
        new_money = money_from_garbage()
        print(f"Onneksi olkoon, löysit rahaa {new_money} €!")
        vastaus = input(f"Roskiksen keiju tarjoaa mahdollisuuden tuplata tämän rahan! Mitä vastaat? ({yes}/{no}): ").lower()
        tuplataanko(vastaus, new_money)  # eliaksen tuplaus funktio
    elif outcome == 'robber':
        money = use_money(id)
        print(f"Tulit ryöstetyksi! Rosvo vei merkittävän osan rahoistasi ja sinulle jäi {robber(money, id)} €.")
    elif outcome == 'hole_in_charge':
        hole_in_charge()
    elif outcome == 'finnair_personnel':
        print("Terve, olen Finnairin ympäristöedustaja. Meillä on palvelu, "
              "jolla voit kompensoida lentopäästöjäsi. Voit lahjoittaa haluamasi määrän rahaa, ja me annamme sinulle "
              "vastineeksi useamman lahjoituksen jälkeen harvinaisemman Vegemakkaran.")
        finnair_personnel()
    elif outcome == secret_black_sausage_chance:
        secret_black_sausage_chance(amount) #saken mustamakkara funktio
    return


vege_list = ["Muu-makkara", "Pirkka vegemakkara", "Makukeittiön Kasvismakkara", "VegMe Grillkorv", "Bon Vegan"]
hole_in_charge_makkaras = []

# Testing the main function (garbage can function)

#print(finnair_personnel())
garbage_can()
print(own_secret_black_sausage)

#list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
#hole_in_charge(list)

#hole_in_charge(vege_list)
