from multiprocessing.dummy import current_process

from Game.choose_game import choose_game

# siirrä muualle
end_command = "lopeta"
finished = False

# Get user's screen name:
username = input("Anna käyttäjänimi: ")
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

# Tähän pelin koodi?
'''while not finished:
    print("Haluatko kaivaa roskista?")
'''
print("Peli päättyi.")

def ask_yes_or_no():
    pass