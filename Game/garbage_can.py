
# import saken mustamakkarafunktio yhdistettävä tähän funktioon
# import rahamäärä

# 10# mahis finnair_personnel, 10# mahis kolovastaavalle, 10# mahis rosvolle, 70# mahis muulle

import random

from Game.actions import pick_action


#Checkng garbages
def garbage_can ():
    pick_action()
    player_money = 100

    # the possibilities of different outcomes
    outcome  = random.choices(['nothing', 'robber', 'hole_in_charge', 'finnair_personnel'], weights = [70, 10, 10, 10], k=1)[0]


def robber(player_money):
    if player_money > 0:
        stolen_money = random.randint(40, 60) / 100
        new_money = player_money * stolen_money
        return new_money

def hole_in_charge():
    pass
















player_money = 500
player_money = robber(player_money)
print(player_money)