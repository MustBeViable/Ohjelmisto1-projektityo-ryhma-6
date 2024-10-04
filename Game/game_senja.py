from Game.Game_ascii_art.casual_garbage_can import ascii_carbage_can
from Game.actions import give_help
from Game.airport_selection_function import airportselection
from Game.choose_game import create_or_choose_game
from Game.commands import outside_section_question
from Game.game_texts import garbage_can_question, tax_free_question, fligh_question, yes, no, approve
from Game.garbage_can import garbage_can
from Game.sign_in_up import ask_sign_in_or_up
from Game.sql_querys.create_and_end_game import finish_game_in_database
from Game.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.sql_querys.money_function import fetch_player_money
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location_name
from Game.taxfree import yes_no_taxfree

# Get user's screen name:
username = ask_sign_in_or_up()
print(f"Tervetuloa {username}!")

# Tässä printataan sit se top-taulu ja tiedot edellisestä pelistä.

# Player chooses whether they want to continue their old game or start a new one. Saves the game_id.
game_id = create_or_choose_game(username)

# The game starts when the player presses enter.
print("Paina enter aloittaaksesi pelaamisen.")
start = input()
while start != "":
    start = input()

give_help()
print(f"Olet lentokentällä {fetch_player_location_name(game_id)}."
      f" Sinulla on {fetch_player_money(game_id)}€ ja makkaroita {len(fetch_player_makkaras(game_id))}." )


sections = [{"question": garbage_can_question, "action": garbage_can, "approved answer": [yes], "other answer": [no], "art": ascii_carbage_can},
            {"question": tax_free_question, "action": yes_no_taxfree, "approved answer": [yes], "other answer": [no], "art": ""},
            {"question": fligh_question, "action": airportselection, "approved answer": [approve], "other answer": [], "art": ""}
            ]

game_finished = False
finish_or_give_up = {"finish": False, "give up": False}

while not game_finished:
    for section in sections:
        print(section["art"])
        finish_or_give_up = outside_section_question(section["question"], section["action"], section["approved answer"], section["other answer"], game_id)
        game_finished = finish_or_give_up["finish"]
        if game_finished:
            break

if finish_or_give_up["give up"]:
    finish_game_in_database(game_id)

print("Peli päättyi.")

# Tähän profiili.