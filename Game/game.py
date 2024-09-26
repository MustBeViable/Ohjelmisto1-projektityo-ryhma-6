from multiprocessing.dummy import current_process

from Game.Playthrough import choose_game

# siirrä muualle
end_command = "lopeta"

# Get user's screen name:
username = input("Anna käyttäjänimi: ")
print(f"Tervetuloa {username}!")
# Tässä printataan sit se top-taulu ja tiedot edellisestä pelistä.

# Player chooses whether they want to continue their old game or start a new one. Save the game_id.
game_id = choose_game(username)

# Tähän ehkä tieto siitä pelistä minkä pelaaja valitsi tai jotain.

# The game starts when the player presses enter.
print("Paina enter aloittaaksesi pelaamisen.")
start = input()
while start != "":
    start = input()

# Tähän alkuprompti.

# Tähän pelin koodi?