from Game.actions import give_help, show_money, show_makkaras, cant_end_now, give_commands, show_score, faulty_command
from Game.check_stolen_makkaras import check_if_any_stolen_makkara
from Game.game_texts import help_command, yes, no, end_command, makkaras_command, money_command, approve, \
    give_up_command, commands_command, commands_str, score_command, not_command_str, profile_command, hole_command
from Game.profile import show_profile


class Command:
    def __init__(self, command, action, helptext):
        self.command = command
        self.action = action
        self.helptext = helptext

    def execute_action(self, parameter):
        """Executes the action resulting from the command."""
        action_result = self.action()
        return action_result

class CommandWithParameter(Command):
    def execute_action(self, parameter):
        """Executes the action resulting from the command, giving the parameter to the function."""
        action_result = self.action(parameter)
        return action_result

# Basic commands: Commands that can be given at any point of the game.
basic_commands = [
    Command(commands_command, give_commands, "Näyttää peruskomennot."),
    Command(help_command, give_help, "Näyttää pelin ohjeen."),
    CommandWithParameter(money_command, show_money, "Näyttää rahamääräsi."),
    CommandWithParameter(makkaras_command, show_makkaras, "Näyttää keräämiesi makkaroiden määrän."),
    CommandWithParameter(score_command, show_score, "Näyttää pisteesi."),
    CommandWithParameter(profile_command, show_profile, "Näyttää sijaintisi, rahasi, pisteesi ja makkaroidesi määrän."),
    CommandWithParameter(hole_command, check_if_any_stolen_makkara, "Voit etsiä Koloa, mikäli Kolovastaava on vienyt makkaroitasi sinne.")
]
in_section_end_commands = [Command(end_command, cant_end_now,"Sulkee pelin. Edistyminen tallentuu automaattisesti ja voit palata jatkamaan peliä profiilistasi."),
                           Command(give_up_command, cant_end_now,"Lopettaa pelin. Luovuttamisen jälkeen et voi enää jatkaa kyseistä pelikertaa.")]

in_section_commands = basic_commands + in_section_end_commands


def execute_basic_command(answer, game_id, list_of_basic_commands):
    """Checks if the given command is a basic command. If it is, executes the basic
        action and returns True. If it isn't, returns False."""
    for basic_command in list_of_basic_commands:
        if answer == basic_command.command:
            basic_command.execute_action(game_id)
            return True
    return False

def input_in_section(prompt, game_id):
    """Used inside sections. Asks for a user input. If the user input is a basic command, calls execute_basic_command
    and executes the basic action. Asks for an input until it's no longer a basic command.\n
    Returns the user input."""
    answer = input(f"{prompt}\n").lower().strip()
    command_was_basic_command = execute_basic_command(answer, game_id, in_section_commands)
    if command_was_basic_command:
        answer = input_in_section(prompt, game_id)
    return answer

def input_outside_section(prompt, game_id):
    """Used before sections. Asks for a user input. If the user input is a basic command, calls execute_basic_command
    and executes the basic action. Asks for an input until it's no longer a basic command and
    returns the input."""
    answer = input(prompt).lower()
    command_was_basic_command = execute_basic_command(answer, game_id, basic_commands)
    if command_was_basic_command:
        answer = input_outside_section(prompt, game_id)
    return answer

def execute_section(question, action, accepted_commands, other_commands, game_id):
    """Asks the user the given question until answered one of the given commands, give-up-command or end-command.
    If the user answers yes, executes the given action. If the user answers no, does nothing.\n
    Returns {end: Boolean, give up: Boolean} meaning {end: player wants to end game, give up: player wants to give up}
    """
    answer = input_outside_section(question, game_id)
    while answer not in ([end_command, give_up_command] + accepted_commands + other_commands):
        faulty_command(answer)
        answer = input_outside_section(question, game_id)
    if answer == end_command:
        return {"finish": True, "game over": False}
    if answer == give_up_command:
        return {"finish": True, "game over": True}
    if answer in accepted_commands:
        action(game_id)
    return {"finish": False, "game over": False}