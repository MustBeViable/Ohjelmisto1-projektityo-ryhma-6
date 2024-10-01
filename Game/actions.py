# All the commands that the user can give and all the texts that the user can see are stored
# as string variables in game_texts.py.
from Game.game_texts import give_help_str, not_command_yes_no_str, yes, no, end_command, help_command


# Prints the game instruction.
def give_help():
    print(give_help_str)

# Prints that the given command does not exist.
def faulty_command_yes_or_no(command):
    print(f'"{command}"{not_command_yes_no_str}')

def ask_yes_or_no(question):
    answer = input(question).lower()
    while answer not in [yes, no, end_command]:
        if answer == help_command:
            give_help()
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

class Question:
    def __init__(self, question, command):
        self.question = question
        self.command = command


'''def pick_action():
    command = input().lower()
    if command == help_command:
        give_help()
    elif command == fly_command:
        show_airports()
    else:
        faulty_command(command)
    return'''


# Test
#print("Peli on käynnissä. Aloita antamalla ensimmäinen komento.")
#pick_action()

#monke