import mysql.connector

from Game.airport_selection_function import current_coordinates
from game_texts import yhteys

# Tää tiedosto ei sit toimi

# Tulee inputista
screen_name = input()

# yhteiset komennot, siirretään muualle
old = "j"
new = "u"
unfinished = "unfinished"

# Yleinen muuttuja
game_id = 0


def check_if_player_has_unfinished_game(name):
    sql = (f"SELECT id FROM game WHERE screen_name = {name} and status = {unfinished}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    unfinished_game_id = result[0]
    # check if empty
    if not unfinished_game_id:
        pass
    else:
        choose_old_or_new_game(unfinished_game_id)
    return result

def choose_old_or_new_game(old_id):
    old_or_new = input(f"Jos haluat jatkaa, paina {old}. Jos haluat aloittaa uuden pelin, paina {new}.")
    current_game_id = old_id
    if old_or_new == old:
        current_game_id = fetch_game_id(old_id)
    elif old_or_new == new:
        current_game_id = create_game(screen_name)
    else:
        choose_old_or_new_game(old_id)
    return current_game_id

def create_game(screen_name):
    sql = (f"INSERT INTO game (id, score, money, screen_name, status, location) VALUES ('{new_makkara_name}', '{game_id}')")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return id

#testi, poista
test_game_id = 5
game_id = test_game_id

def fetch_game_id(given_id):
    sql = (f"SELECT id FROM game WHERE id = {given_id}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    return result

def fetch_own_location():
    sql = (f"SELECT location FROM game WHERE id = {game_id}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    return result

def add_makkara_to_reached(new_makkara_name):
    sql = (f"INSERT INTO makkara_reached (makkara_name, game_id) VALUES ('{new_makkara_name}', '{game_id}')")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

# Fetches names of the sausages tha player has collected
def fetch_reached_makkaras():
    sql = (f"SELECT name FROM makkara_reached WHERE id = {game_id}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return