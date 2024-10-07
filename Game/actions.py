# Used by game_Senja_try

from Game.game_texts import give_help_str, commands_str, not_command_str
from Game.sql_querys.fetch_player_makkaras import player_makkaras_amount
from Game.sql_querys.money_function import fetch_player_money
from Game.sql_querys.one_player_own_top_5 import fetch_player_top5_list
from Game.sql_querys.score_fetch_and_score_update_querys import player_score_fetch

# Prints the game instruction.
def give_help():
    """Prints the game help text."""
    print(give_help_str)

def give_commands():
    """Prints the game commands."""
    print(commands_str)

def cant_end_now():
    """Prints that the player can't end the game now."""
    print("Voit lopettaa ennen roskiksen kaivamista, tax freehen menemistä tai lentojen katselemista. "
          "Tee siis nykyinen valintasi loppuun.")

def show_money(game_id):
    """Prints the player's money."""
    player_money = fetch_player_money(game_id)
    print(f"Rahaa: {player_money}€")

def show_makkaras(game_id):
    """Prints the player's makkaras."""
    makkaras_length = player_makkaras_amount(game_id)
    print(f"Makkaroita: {makkaras_length}")

def show_score(game_id):
    """Prints the player's score.'"""
    player_score = player_score_fetch(game_id)
    print(f"Pisteitä: {player_score}")

def show_top(screen_name):
    """Prints the player's top 5 scores."""
    player_scores = fetch_player_top5_list(screen_name)
    print("top 5 pelisi:")
    for idx, score in enumerate(player_scores):
        print(f"{idx + 1}. {score} pt")
    print("")

def faulty_command(command):
    """Prints that the given command doesn't exist."""
    print(f'"{command}"{not_command_str}')