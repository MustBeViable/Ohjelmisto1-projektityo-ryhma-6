import mysql.connector

from game_texts import yhteys

# yhteiset komennot, siirretään muualle
old = "j"
new = "u"

# Yleinen muuttuja, siirretään muualle
game_id = 0

# Alkuarvot, siirretään muualle
start_money = 1000
unfinished = "unfinished"
finished = "finished"
start_location = "EFNU"

def sql_connection(sql_text):
    kursori = yhteys.cursor()
    kursori.execute(sql_text)
    result = kursori.fetchall()
    return result

# Checks if the player has an unfinished game. If they do, asks if they want to continue or create a new game.
# If they choose to continue, returns the id of that old game.
# If they decide to create a new game, or they don't have an unfinished game, creates a new game and returns its id.
# If they create a bew game, the unfinished game will be marked as finished.
def choose_game(name):
    sql = (f"SELECT id FROM game WHERE screen_name = {name} and status = {unfinished}")
    unfinished_game_id = sql_connection(sql)[0]
    current_game_id = None
    if unfinished_game_id:
        old_or_new = input(f"Jos haluat jatkaa, paina {old}. Jos haluat aloittaa uuden pelin, paina {new}.")
        while old_or_new not in [old, new]:
            old_or_new = input(f"Jos haluat jatkaa, paina {old}. Jos haluat aloittaa uuden pelin, paina {new}.")
        if old_or_new == old:
            current_game_id = unfinished_game_id
        elif old_or_new == new:
            current_game_id = create_game(name)
            finish_game_in_database(unfinished_game_id)
        else:
            pass
    else:
        current_game_id = create_game(name)
    return current_game_id


# Creates the game to the database with given screen name. Returns the ID of the new game.
def create_game(screen_name):
    sql = (f"INSERT INTO game (id, score, money, screen_name, status, location) VALUES ('0', {start_money}, {screen_name}, {unfinished}, {start_location})")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return id

def finish_game_in_database(game_id):
    sql = (f"UPDATE game SET status = {finished} WHERE id = {game_id}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

#testi, poista
test_game_id = 5
game_id = test_game_id


def fetch_own_location():
    sql = (f"SELECT location FROM game WHERE id = {game_id}")
    result = sql_connection(sql)
    return result

def add_makkara_to_reached(new_makkara_name):
    sql = (f"INSERT INTO makkara_reached (makkara_name, game_id) VALUES ('{new_makkara_name}', '{game_id}')")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

# Fetches names of the sausages tha player has collected.
def fetch_reached_makkaras():
    sql = (f"SELECT name FROM makkara_reached WHERE id = {game_id}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return