# All the commands that the user can give and all the texts that the user can see are stored
# as string variables in game_texts. They are all imported to this file.
from Game.game_texts import *


# The function asks for a command from the user with the prompt given to the function as a parameter.
# The prompt can be for example "Anna komento."
# The function executes the action connected to the command and returns ???
# After executing the commmand, the function repeats itself asking for a new commmand. (Should it?)

def pick_action(prompt):
    command = input(prompt).lower()
    if command == ask_help:
        print(give_help)
        pass
    else:
        print(not_command)
    pick_action(give_commmand)
    return


# Test
test_prompt = give_commmand
pick_action(test_prompt)

