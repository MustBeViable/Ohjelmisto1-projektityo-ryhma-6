from gc import garbage
import time
from Game.actions import ask_for_command, Question
from Game.airport_selection_function import airportselection
from Game.choose_game import choose_game
from Game.game_texts import garbage_can_question, tax_free_question, fligh_question
from Game.garbage_can import garbage_can
from Game.sign_in_up import ask_sign_in_or_up
from Game.sql_querys.money_function import fetch_player_money
from Game.yesno_taxfree import yes_no_taxfree

# Get user's screen name:
username = ask_sign_in_or_up()
print(f"Tervetuloa {username}!")
# Tässä printataan sit se top-taulu ja tiedot edellisestä pelistä.

# Player chooses whether they want to continue their old game or start a new one. Saves the game_id.
game_id = choose_game(username)

# Tähän ehkä tieto siitä pelistä minkä pelaaja valitsi tai jotain.
print(f"game id: {game_id}")

# The game starts when the player presses enter.
print("Paina enter aloittaaksesi pelaamisen.")
start = input()
while start != "":
    start = input()

# Tähän alkuprompti.

game_finished = False

#actions = [Question(garbage_can_question, garbage_can()),Question(tax_free_question, "Ostit makkaran."),Question(fligh_question, airportselection(game_id))]

while not game_finished:

    if ask_for_command(garbage_can_question, game_id)["yes"]:
        garbage_can(game_id)
    if ask_for_command(tax_free_question, game_id)["yes"]:
        yes_no_taxfree(game_id)
    if fetch_player_money(game_id) >= 50:
        print(fligh_question)
        time.sleep(2)
        airportselection(game_id)
    else:
        print("Rahasi eivät riitä enää lentämiseen.")
        game_finished = True


print("Peli päättyi.")