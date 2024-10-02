
import random

from Game.sql_querys.money_function import fetch_player_money, update_player_money

hole_in_charge_makkaras=["a","b","c","d"]

def kolo_search():
    outside_airport=input("Haluatko ottaa taxin(50 euroa) vai uberin(1 euroa)?")
    rahat=fetch_player_money(playthrough_id)
    if outside_airport == "taxi":

        own_makkaras.extend(hole_in_charge_makkaras)
        print("löysit hole_in_charge kolon ja sait makkarasi takaisin! :)")
    elif outside_airport == "uber":
        mahdollisuus=random.randint(1,2)
        if mahdollisuus==1:
            new_money=rahat-150
            update_player_money(new_money, game_id)
            print("uber kuljettaja pahoinpiteli sinut, jätti tienvarteen, vei sinulta 100 euroa ja joudit tilaamaan taxin takaisin lentokentälle, joka maksoi 50 euroa!")
        elif mahdollisuus!=1:
            own_makkaras.extend(hole_in_charge_makkaras)
            print("löysit hole_in_charge kolon ja sait makkarasi takaisin! :)")
        return
kolo_search()
