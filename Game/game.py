from Game.actions import ask_yes_or_no, Question
from Game.choose_game import choose_game
from Game.game_texts import dumpster_question, tax_free_question, fligh_question
from Game.sign_in_up import ask_sign_in_or_up

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

while not game_finished:
    for action in [Question(dumpster_question, "Kaivoit roskista."),
                   Question(tax_free_question, "Ostit makkaran."),
                   Question(fligh_question, "Lensit toiselle lentokentälle.")]:
        answer = ask_yes_or_no(action.question)
        if answer["finished"]:
            game_finished = True
            break
        if answer["yes"]:
            print(action.command)

print("Peli päättyi.")