
# 10% mahis finnair_personnel, 10% mahis kolovastaavalle, 10% mahis rosvolle, 70% mahis voittaa rahaa

import random
from os import remove

from Game.player_profile import own_makkaras, own_money
from secret_black_sausage import secret_black_sausage_chance

def robber(own_money):
    player_money = own_money
    if player_money > 0:
        stolen_money = player_money * 0.5
        return stolen_money


# Function is calling all the "own_makkaras" list and reduces random amount of the list
def hole_in_charge(own_makkaras):
    if len(own_makkaras) == 0:
        print("Sinulla ei ollut makkaraa vietävänä.")
    else:
        # Devided by five (like 20%) and rounded down
        num_to_lose = len(own_makkaras) // 5

        # Varmistetaan, että vähintään yksi makkara otetaan, jos tulos on nolla
        if num_to_lose == 0 and len(own_makkaras) > 0:
            num_to_lose = 1

        # A random number of sausages (num_to_lose) is selected to remove
        lost_makkaras = random.sample(own_makkaras, num_to_lose)

        # The selected sausages are removed from original list and added to hole in charge's list
        for makkara in lost_makkaras:
            own_makkaras.remove(makkara)
            hole_in_charge_makkaras.append(makkara)
        print(hole_in_charge_makkaras)

        print(f"Kolovastaava vei sinulta seuraavat makkarat: {', '.join(lost_makkaras)}.")

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
def money_from_garbage(own_money):
    new_money = own_money
    new_money = random.randint(200, 1000)
    return new_money



#Checkng garbages, saken mustamakkarafunktio
def garbage_can():
    #secret_black_sausage_chance()
    player_money = own_money
    #robber(player_money)
    #finnair_personnel()

    # the possibilities of different outcomes
    outcome = random.choices(['nothing', 'robber', 'hole_in_charge', 'finnair_personnel'], weights = [70, 10, 10, 10], k=1)[0]
    if outcome == 'nothing':
        print(f"Onneksi olkoon, löysit {money_from_garbage(own_money)} € rahaa!")
    elif outcome == 'robber':
        print(f"Tulit ryöstetyksi! Rosvo vei merkittävän osan rahoistasi, ja sinulle jäi {robber(own_money)} €.")
    elif outcome == 'hole_in_charge':
        print(f"Törmäsit kolovastaavaan! Harmi makkaravarastosi kannalta... Makkaravarastostasi on lähtenyt {hole_in_charge(own_makkaras)} makkaraa.")
    elif outcome == 'finnair_personnel':
        print("Terve, olen Finnairin ympäristöedustaja. Meillä on palvelu, "
              "jolla voit kompensoida lentopäästöjäsi. Voit lahjoittaa haluamasi määrän rahaa, ja me annamme sinulle "
              "vastineeksi useamman lahjoituksen jälkeen harvinaisemman Vegemakkaran.")
        finnair_personnel()
    return


# Testing the main function (garbage can function)
#print(finnair_personnel())
#garbage_can()

vege_list = ["Muu-makkara", "Pirkka vegemakkara", "Makukeittiön Kasvismakkara", "VegMe Grillkorv", "Bon Vegan"]
hole_in_charge_makkaras = []

#list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
#hole_in_charge(list)

hole_in_charge(vege_list)