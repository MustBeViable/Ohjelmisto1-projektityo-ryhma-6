
# 10% mahis finnair_personnel, 10% mahis kolovastaavalle, 10% mahis rosvolle, 70% mahis muulle

import random

from Game.player_profile import own_makkaras, own_money


#Checkng garbages, saken mustamakkarafunktio
def garbage_can ():
    own_makkaras()
    player_money = own_money

    # the possibilities of different outcomes
    outcome  = random.choices(['nothing', 'robber', 'hole_in_charge', 'finnair_personnel'], weights = [70, 10, 10, 10], k=1)[0]


def robber(own_money):
    player_money = own_money
    if player_money > 0:
        stolen_money = random.randint(40, 60) / 100
        new_money = player_money * stolen_money
        return new_money


def hole_in_charge():
    pass

def finnair_personnel():
    pass

#Testing that the robber function works
print(robber(own_money))
