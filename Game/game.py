from multiprocessing.dummy import current_process

from Game.Playthrough import choose_game

# Get user's screen name:
username = input("Anna käyttäjänimi: ")
print(f"Tervetuloa {username}!")
# Tässä printataan sit se top-taulu.
print("Paina enter aloittaaksesi pelaamisen.")
start = input()
while start != "":
    start = input()
game_id = choose_game(username)
