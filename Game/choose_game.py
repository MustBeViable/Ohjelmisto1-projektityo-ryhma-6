import mysql.connector

from Game.sql_querys.create_and_end_game import create_game, finish_game_in_database, fetch_unfinished_playthrough
from game_texts import yhteys, game_id

def sql_connection(sql_text):
    kursori = yhteys.cursor()
    kursori.execute(sql_text)
    result = kursori.fetchall()
    return result

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

continue_or_new_str = f"Jos haluat jatkaa, paina {old}. Jos haluat aloittaa uuden pelin, paina {new}."


# Checks if the player has an unfinished game. If they do, asks if they want to continue or create a new game.
# If they choose to continue, returns the id of that old game.
# If they decide to create a new game, or they don't have an unfinished game, creates a new game and returns its id.
# If they create a new game, the unfinished game will be marked as finished.
def choose_game(screen_name):
    current_game_id = None
    unfinished_game_list = fetch_unfinished_playthrough(screen_name)
    if len(unfinished_game_list) != 0:
        unfinished_game_id = unfinished_game_list[0][0]
        old_or_new = lower_input(continue_or_new_str)
        while old_or_new not in [old, new]:
            old_or_new = lower_input(continue_or_new_str)
        if old_or_new == old:
            current_game_id = unfinished_game_id
        elif old_or_new == new:
            current_game_id = create_game(screen_name)
            finish_game_in_database(unfinished_game_id)
        else:
            pass
    else:
        current_game_id = create_game(screen_name)
    return current_game_id


# testi choose_game
'''testi_id = choose_game(input("Syötä testikäyttäjän nimi: "))
print(f"palauttaa: {testi_id}")

sql2 = (f"SELECT * FROM playthrough")
test2 = sql_connection(sql2)
print("Kaikki pelit: ")
print(test2)
'''