# Used by game

from Game.game_texts import give_help_str, not_command_yes_no_str, yes, no, end_command, help_command, money_command, \
    makkaras_command, not_command_str
from Game.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.sql_querys.money_function import fetch_player_money


# Prints the game instruction.
def give_help():
    print(give_help_str)

def show_money(game_id):
    player_money = fetch_player_money(game_id)
    print(f"Rahaa {player_money}€.")

def show_makkaras(game_id):
    player_makkaras = fetch_player_makkaras(game_id)
    makkaras_length = len(player_makkaras)
    print(f"Makkaraa: {makkaras_length} ")

# Prints that the given command does not exist.
def faulty_command_yes_or_no(command):
    print(f'"{command}"{not_command_yes_no_str}')

def faulty_command(command):
    print(f'"{command}"{not_command_str}')

def ask_for_command(question, game_id):
    """Asks user the question given as a parameter. Returns a dictionary with values
    "yes": Boolean and "finished": Boolean. "yes" tells whether the user answered yes or no
    too the question and "finished" tells whether the user gave finish command or not.
    """
    answer = input(question).lower()
    while answer not in [yes, no, end_command]:
        if answer == help_command:
            give_help()
            answer = input(question).lower()
        elif answer == money_command:
            show_money(game_id)
            answer = input(question).lower()
        elif answer == makkaras_command:
            show_makkaras(game_id)
            answer = input(question).lower()
        else:
            faulty_command_yes_or_no(answer)
            answer = input(question).lower()
    if answer == yes:
        return {"yes": True, "finished": False}
    elif answer == no:
        return {"yes": False, "finished": False}
    elif answer == end_command:
        return {"yes": False, "finished": True}


def create_yes_no_question(question):
    input(question)

def ask_input(prompt, game_id):
    answer = input(prompt).lower()
    if answer == help_command:
        give_help()
        answer = ask_input(prompt, game_id)
    if answer == money_command:
        show_money(game_id)
        answer = ask_input(prompt, game_id)
    if answer == makkaras_command:
        show_makkaras(game_id)
        answer = ask_input(prompt, game_id)
    return answer

#print(ask_input("Mitäs haluat tehdä? ", 3))

# Test
#print("Peli on käynnissä. Aloita antamalla ensimmäinen komento.")
#pick_action()

def command_to_action(game_id, answer):
            if answer == help_command:
                give_help()
            elif answer == money_command:
                show_money(game_id)
            elif answer == makkaras_command:
                show_makkaras(game_id)
            else:
                faulty_command_yes_or_no(answer)
            return answer