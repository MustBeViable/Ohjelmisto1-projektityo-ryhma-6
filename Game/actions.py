# Used by game_Senja_try

from Game.game_texts import give_help_str, not_command_yes_no_str, yes, no, end_command, help_command, money_command, \
    makkaras_command, commands_str, not_command_str
from Game.search_of_kolo import kolo_search
from Game.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.sql_querys.money_function import fetch_player_money
from Game.sql_querys.score_fetch_and_score_update_querys import player_score_fetch


# Prints the game instruction.
def give_help():
    print(give_help_str)

def give_commands():
    print(commands_str)

def cant_end_now():
    print("Voit lopettaa ennen roskiksen kaivamista, tax freehen menemistä tai lentojen katselemista. "
          "Tee siis nykyinen valintasi loppuun.")

def show_money(game_id):
    player_money = fetch_player_money(game_id)
    print(f"Rahaa: {player_money}€")

def show_makkaras(game_id):
    player_makkaras = fetch_player_makkaras(game_id)
    makkaras_length = len(player_makkaras)
    print(f"Makkaroita: {makkaras_length}")

def show_score(game_id):
    player_score = player_score_fetch(game_id)
    print(f"Pisteitä: {player_score}")

# Prints that the given command does not exist.
def faulty_command_yes_or_no(command):
    print(f'"{command}"{not_command_yes_no_str}')

def faulty_command(command):
    print(f'"{command}"{not_command_str}')

'''def ask_for_command(question, game_id):
    """Asks user the question given as a parameter. Returns a dictionary with values
    "yes": Boolean and "finished": Boolean. "yes" tells whether the user answered yes or no
    too the question and "finished" tells whether the user gave finish command or not.
    """
    answer = input_outside_section(question, game_id)
    while answer not in [yes, no, end_command]:
            faulty_command_yes_or_no(answer)
            answer = input(question).lower()
    if answer == yes:
        return {"yes": True, "finished": False}
    elif answer == no:
        return {"yes": False, "finished": False}
    elif answer == end_command:
        return {"yes": False, "finished": True}

'''