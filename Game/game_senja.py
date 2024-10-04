from Game.actions import give_help
from Game.choose_game import create_or_choose_game
from Game.commands import outside_section_question
from Game.profile import show_profile
from Game.section import garbage_can_section, tax_free_section, flight_section
from Game.sign_in_up import ask_sign_in_or_up
from Game.sql_querys.create_and_end_game import finish_game_in_database
from Game.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.sql_querys.money_function import fetch_player_money
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location_name

# Get user's screen name:
username = ask_sign_in_or_up()
print(f"Tervetuloa {username}!")

# Tässä printataan sit se top-taulu ja tiedot edellisestä pelistä.

# Player chooses whether they want to continue their old game or start a new one. Saves the game_id.
game_id = create_or_choose_game(username)

# The game starts when the player presses enter.
start = input("Paina enter aloittaaksesi pelaamisen.")
while start != "":
    start = input("Paina enter aloittaaksesi pelaamisen.")

give_help()
print(f"Olet lentokentällä {fetch_player_location_name(game_id)}."
      f" Sinulla on {fetch_player_money(game_id)}€ ja makkaroita {len(fetch_player_makkaras(game_id))}." )


sections = [garbage_can_section,
            tax_free_section,
            flight_section
            ]

#game_finished = False
finish_or_give_up = {"finish": False, "game over": False}

while not finish_or_give_up["finish"]:
    for section in sections:
        if section.check_condition(game_id):
            print(section.art)
            finish_or_give_up = outside_section_question(section.question, section.action, section.approved_answer, section.other_answer, game_id)
        else:
            finish_or_give_up = {"finish": True, "game over": True}
            print(section.condition_explanation)
        print(finish_or_give_up)
        if finish_or_give_up["finish"]:
            break

print("Peli päättyi.")

print(finish_or_give_up)
print(finish_or_give_up["game over"])
if finish_or_give_up["game over"]:
    finish_game_in_database(game_id)



# Tähän profiili.