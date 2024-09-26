
# 10% mahis finnair_personnel, 10% mahis kolovastaavalle, 10% mahis rosvolle, 70% mahis voittaa rahaa

import random

from Game.player_profile import own_makkaras, own_money

vege_list = ["Muu-makkara", "Pirkka vegemakkara", "Makukeittiön Kasvismakkara", "VegMe Grillkorv", "Bon Vegan"]



def robber(own_money):
    player_money = own_money
    if player_money > 0:
        stolen_money = player_money * 0.5
        return stolen_money


# Function is going to call the "own_makkaras" list and reduces random amount over the list
def hole_in_charge(own_makkaras):
    own_nakki = own_makkaras
    robbing_makkaras = own_nakki * random.randint(0.4, 0.6)
    new = own_nakki - robbing_makkaras
    return new



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
    return new_money



# !!!!! Need to exchange the money to be a variable !!!!
def money_from_garbage(own_money):
    new_money = own_money
    new_money = random.randint(200, 1000)
    return new_money



#Checkng garbages, saken mustamakkarafunktio
def garbage_can():
    player_money = own_money
    #robber(player_money)
    #finnair_personnel()

    # the possibilities of different outcomes
    outcome  = random.choices(['nothing', 'robber', 'hole_in_charge', 'finnair_personnel'], weights = [70, 10, 10, 10], k=1)[0]
    if outcome == 'nothing':
        print(f"Onneksi olkoon, löysit {money_from_garbage(own_money)} € rahaa!")
    elif outcome == 'robber':
        print(f"Tulit ryöstetyksi! Rosvo vei merkittävän osan rahoistasi, ja sinulle jäi {robber(own_money)} €.")
    elif outcome == 'hole_in_charge':
        print(f"Törmäsit kolovastaavaan! Harmi makkaravarastosi kannalta... Voit tarkistaa jäljellä olevat makkarasi komennon avulla.")
        hole_in_charge()
    elif outcome == 'finnair_personnel':
        print("Terve, olen Finnairin ympäristöedustaja. Meillä on palvelu, "
              "jolla voit kompensoida lentopäästöjäsi. Voit lahjoittaa haluamasi määrän rahaa, ja me annamme sinulle "
              "vastineeksi useamman lahjoituksen jälkeen harvinaisemman Vegemakkaran.")
        finnair_personnel()
    return


# Testing the main function (garbage can function)
print(garbage_can())
print(finnair_personnel())