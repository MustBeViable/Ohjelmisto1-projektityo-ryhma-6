import mysql.connector

from game_texts import yhteys, game_id

# yhteiset komennot, siirretään muualle
old = "j"
new = "u"

def lower_input(prompt):
    result = input(prompt).lower()
    return result

# Alkuarvot, siirretään muualle
start_money = "1000"
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
# If they create a new game, the unfinished game will be marked as finished.
def choose_game(screen_name):
    current_game_id = None
    sql = (f"SELECT id FROM playthrough WHERE screen_name = '{screen_name}' AND status = '{unfinished}'")
    unfinished_game_list = sql_connection(sql)
    if len(unfinished_game_list) != 0:
        unfinished_game_id = unfinished_game_list[0][0]
        old_or_new = lower_input(f"Jos haluat jatkaa, paina {old}. Jos haluat aloittaa uuden pelin, paina {new}.")
        while old_or_new not in [old, new]:
            old_or_new = lower_input(f"Jos haluat jatkaa, paina {old}. Jos haluat aloittaa uuden pelin, paina {new}.")
        if old_or_new == old:
            current_game_id = unfinished_game_id
            print(f"old{ current_game_id}")
        elif old_or_new == new:
            current_game_id = create_game(screen_name)
            print(f"new {current_game_id}")
            finish_game_in_database(unfinished_game_id)
        else:
            pass
    else:
        current_game_id = create_game(screen_name)
    return current_game_id


# Creates the game to the database with given screen name. Returns the ID of the new game.
def create_game(screen_name):
    sql_create = (f"INSERT INTO playthrough (score, money, screen_name, status, location) VALUES ('0', {start_money}, '{screen_name}', '{unfinished}', '{start_location}')")
    kursori = yhteys.cursor()
    kursori.execute(sql_create)
    sql_id = (f"SELECT id FROM playthrough WHERE screen_name = '{screen_name}' AND status = '{unfinished}' ORDER BY id DESC")
    sql_connection(sql_id)
    new_id = sql_connection(sql_id)[0][0]
    print(f"new id {new_id}")
    return new_id

def finish_game_in_database(finish_id):
    sql = (f"UPDATE playthrough SET status = '{finished}' WHERE id = '{finish_id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

'''# testi create_game
k_e = input("Luo uusi käyttäjä? k/e")
if k_e == "k":
    testname = input("Anna testikäyttäjälle nimi: ")
    create_game(testname)
    sql1 = (f"SELECT * FROM playthrough")
    test1 = sql_connection(sql1)
    print("uusi pelikerta oli:")
    print(test1[-1])
    print("kaikki pelikerrat: ")
    print(test1)'''

# testi choose_game
testi_id = choose_game(input("Syötä testikäyttäjän nimi: "))
print(f"palauttaa: {testi_id}")

sql2 = (f"SELECT * FROM playthrough")
test2 = sql_connection(sql2)
print("Kaikki pelit: ")
print(test2)


""""
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
    return"""