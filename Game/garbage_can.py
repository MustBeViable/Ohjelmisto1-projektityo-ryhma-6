
# 10% mahis finnair_personnel, 10% mahis kolovastaavalle, 10% mahis rosvolle, 70% mahis voittaa rahaa

import random

from Game.player_profile import own_makkaras, own_money

testi = ["vege1", "vege2", "vege3", "vege4", "vege5"]


def robber(own_money):
    player_money = own_money
    if player_money > 0:
        stolen_money = player_money * 0.5
        return stolen_money

# Function is going to call the "own_makkaras" list and reduces random amount over the list
def hole_in_charge():
    pass


# Player can donate x amount money and get vege sausage
def finnair_personnel():
    donate = int(input("Syötä tähän numeroina, paljonko haluat lahjoittaa rahaa? "))
    for d in donate:

    own_makkaras.append(donate)



def money_from_garbage(own_money):
    new_money = own_money
    new_money = random.randint(200, 1000)
    return new_money

#Checkng garbages, saken mustamakkarafunktio
def garbage_can():
    player_money = own_money
    robber(player_money)
    finnair_personnel()
    # the possibilities of different outcomes
    outcome  = random.choices(['nothing', 'robber', 'hole_in_charge', 'finnair_personnel'], weights = [70, 10, 10, 10], k=1)[0]
    if outcome == 'nothing':
        print(f"Onneksi olkoon, löysit {money_from_garbage(own_money)} € rahaa!")
    elif outcome == 'robber':
        print(f"Tulit ryöstetyksi! Rosvo vei merkittävän osan rahoistasi, ja sinulle jäi {robber(own_money)} €.")
    elif outcome == hole_in_charge():
        print(f"Törmäsit kolovastaavaan! Harmi makkaravarastosi kannalta... Voit tarkistaa jäljellä olevat makkarasi komennon avulla.")
    elif outcome == finnair_personnel():
        print("Terve, olen Finnairin ympäristöedustaja. Meillä on palvelu, "
              "jolla voit kompensoida lentopäästöjäsi. Voit lahjoittaa haluamasi määrän rahaa, ja me annamme sinulle "
              "vastineeksi useamman lahjoituksen jälkeen harvinaisemman Vegemakkaran.")
    return



# Testing the main function (garbage can function)
print(garbage_can())