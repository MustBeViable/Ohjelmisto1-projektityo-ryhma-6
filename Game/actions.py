# All the commands that the user can give and all the texts that the user can see are stored
# as string variables in game_texts.py.
from Game.game_texts import give_help_str, help_command, not_command_str, give_commmand_str, fly_command

# Prints the game instruction and asks for a new command.
def give_help():
    print(give_help_str)
    pick_action()

# Prints that the given command does not exist and asks for a new one.
def faulty_command(command):
    print(f'"{command}"{not_command_str}')
    pick_action()

# Joku tällanen tulee tähän mut katotaan sit sit myöhemmin tää oli vaan esimerkki
def show_airports():
    pass

# The function asks for a command from the user with the prompt given to the function as a parameter.
# The prompt can be for example "Olet Nummelan lentokentällä. Mitä haluat tehdä?"
# The function executes the action connected to the command and returns ??? pitäs varmaan palauttaa jotain
def pick_action():
    command = input("").lower()
    if command == help_command:
        give_help()
    elif command == fly_command:
        show_airports()
    else:
        faulty_command(command)
    return



# Test
test_prompt = give_commmand_str
print("Peli on käynnissä. Aloita antamalla ensimmäinen komento.")
pick_action()