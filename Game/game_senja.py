from Game.actions import give_help, show_top
from Game.choose_game import create_or_choose_game
from Game.commands import execute_section
from Game.profile import show_profile
from Game.section import garbage_can_section, tax_free_section, flight_section
from Game.sign_in_up import ask_sign_in_or_up
from Game.sql_querys.create_and_end_game import finish_game_in_database
from Game.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.sql_querys.money_function import fetch_player_money
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location_name
from Game.sql_querys.top_5_score_fetch_query import top_5_score_fetch_query

# Get user's screen name:
username = ask_sign_in_or_up()
print(f"Tervetuloa {username}!")

show_top(username)
top_5_score_fetch_query()

# Player chooses whether they want to continue their old game or start a new one. Saves the game_id.
game_id = create_or_choose_game(username)

# Prints the game instruction
give_help()
print(f"Olet lentokentällä {fetch_player_location_name(game_id)}."
      f" Sinulla on {fetch_player_money(game_id)}€ ja makkaroita {len(fetch_player_makkaras(game_id))}." )

# The game starts when the player presses enter.
start = input("Paina enter aloittaaksesi pelaamisen.")
while start != "":
    start = input("Paina enter aloittaaksesi pelaamisen.")

sections = [garbage_can_section,
            tax_free_section,
            flight_section
            ]

finish_or_give_up = {"finish": False, "game over": False}

while not finish_or_give_up["finish"]:
    for section in sections:
        if section.check_condition(game_id):
            print(section.art)
            finish_or_give_up = execute_section(section.question, section.action, section.approved_answer, section.other_answer, game_id)
        else:
            finish_or_give_up = {"finish": True, "game over": True}
            print(section.condition_explanation)
        if finish_or_give_up["finish"]:
            break

print("Peli päättyi.\n")
show_profile(game_id)
if finish_or_give_up["game over"]:
    finish_game_in_database(game_id)
    print(f"Pelisi on lopetettu etkä voi enää jatkaa sitä.")
show_top(username)