import mysql.connector

from Game.sql_querys.create_and_end_game import create_game, finish_game_in_database, fetch_unfinished_playthrough
from Game.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location, fetch_player_location_name
from Game.sql_querys.score_fetch_and_score_update_querys import player_score_fetch
from game_texts import yhteys


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


def continue_or_new_str(game_id):
    """'Haluatko jatkaa keskeneräistä pelikertaasi?
       (sijainti: location
       pisteitä: score
       makkaroita: n kpl)
       Jos aloitat uuden peli, edellinen pelisi päättyy.
        Jos haluat jatkaa, paina {old}. Jos haluat aloittaa uuden pelin, paina {new}.'"""
    text = (f"Haluatko jatkaa keskeneräistä pelikertaasi? "
            f"(sijainti: {fetch_player_location_name(game_id)}, "
            f"pisteitä: {player_score_fetch(game_id)}, "
            f"makkaroita: {len(fetch_player_makkaras(game_id))} kpl)\n"
            f"Jos aloitat uuden peli, edellinen pelisi päättyy, etkä voi enää jatkaa sitä.\n"
            f"Jos haluat jatkaa, paina {old}. Jos haluat aloittaa uuden pelin, paina {new}. ")
    return text

no_unfinished_game = "Sinulla ei ole keskeneräisiä pelejä. Luodaan sinulle uusi peli."

def create_or_choose_game(screen_name):
    """Checks if the given screen_name has an unfinished game.
    If they do, asks if they want to continue or create a new game.
    If they choose to continue, returns the id of that old game.
    If they decide to create a new game, or they don't have an unfinished game,
    creates a new game and returns its id. If they create a new game,
    the unfinished game will be marked as finished."""

    unfinished_game_list = fetch_unfinished_playthrough(screen_name)
    if len(unfinished_game_list) != 0:
        current_game_id = choose_old_or_new_game(screen_name, unfinished_game_list)
    else:
        print(no_unfinished_game)
        current_game_id = create_game(screen_name)
    return current_game_id

def choose_old_or_new_game(screen_name, unfinished_game_list):
    """Asks the player if they want to continue their old game or start a new game
    and returns the id of the game. Creates a new game if needed and marks the old
    game as finished."""
    current_game_id = None
    unfinished_game_id = unfinished_game_list[0][0]
    user_input = input(continue_or_new_str(unfinished_game_id)).lower()
    while user_input not in [old, new]:
        user_input = input(continue_or_new_str(unfinished_game_id)).lower()
    if user_input == old:
        current_game_id = unfinished_game_id
    if user_input == new:
        current_game_id = create_game(screen_name)
        finish_game_in_database(unfinished_game_id)
    return current_game_id