
import random


from Game.sql_querys.money_function import fetch_player_money, update_player_money
from Game.sql_querys.return_stolen_makkaras import return_player_makkaras



def kolo_search(game_id):

    """What happens when u search kolo"""

    outside_airport=input("Kirjoita taxi jos haluat ottaa taxin(50 euroa) tai kirjoita uber jos haluat uberin(1 euroa)?")
    while outside_airport != "taxi" and outside_airport != "uber":
        outside_airport = input("Kirjoita taxi jos haluat ottaa taxin(50 euroa) tai kirjoita uber jos haluat uberin(1 euroa)?")

    if outside_airport == "taxi":
        return_player_makkaras(id)
        new_money = fetch_player_money(game_id) - 150
        update_player_money(new_money, game_id)
        print("löysit hole_in_charge kolon ja sait makkarasi takaisin! :)")
    elif outside_airport == "uber":
        mahdollisuus=random.randint(1,2)
        if mahdollisuus==1:
            new_money=fetch_player_money(game_id)-150
            update_player_money(new_money, game_id)
            print("Uber kuljettaja pahoinpiteli sinut, jätti tienvarteen, vei sinulta 100 euroa ja joudit tilaamaan taxin takaisin lentokentälle, joka maksoi 50 euroa!")
        elif mahdollisuus!=1:
            return_player_makkaras(id)
            print("löysit hole_in_charge kolon ja sait makkarasi takaisin! :)")
            return
kolo_search(1)
