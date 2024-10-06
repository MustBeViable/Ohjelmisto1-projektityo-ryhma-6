from Game.actions import give_help, show_money, show_makkaras, cant_end_now, give_commands, show_score, faulty_command, \
    end_game, give_up_game
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
basic_commands = [Command(help_command, give_help, "Näyttää ohjeen."),
                 CommandWithParameter(money_command, show_money, "Näyttää sen hetkiset rahasi."),
                 CommandWithParameter(makkaras_command, show_makkaras, "Näyttää omien makkaroidesi määrän."),
                  CommandWithParameter(profile_command, show_profile, "Näyttää sijaintisi, rahasi, pisteesi ja makkaroidesi määrän."),
                  CommandWithParameter(hole_command, check_if_any_stolen_makkara, "Etsii koloa."),
                 Command(commands_command, give_commands, "Näyttää peruskomennot."),
                 CommandWithParameter(score_command, show_score, "Näyttää pisteesi."),
                 ]
in_section_end_commands = [Command(end_command, cant_end_now, "Sulkee pelin. Edistyminen tallentuu automaattisesti ja voit palata jatkamaan peliä profiilistasi."),
                            Command(give_up_command, cant_end_now, "Lopettaa pelin. Luovuttamisen jälkeen et voi enää jatkaa kyseistä pelikertaa.")]

in_section_commands = basic_commands + in_section_end_commands

def execute_basic_command(answer, game_id, set_of_basic_commands):
    """Checks if the given command is a basic command. If it is, executes the basic
        action and returns True. If it isn't, returns False."""
    for command_object in set_of_basic_commands:
        if answer == command_object.command:
            command_object.execute_action(game_id)
            return True
    return False


def input_in_section(prompt, game_id):
    """Used inside sections. Asks for a user input. If the user input is a basic command, calls execute_basic_command
    and executes the basic action. Asks for an input until it's no longer a basic command and
    returns the input."""
    answer = input(prompt).lower()
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


'''
class AskForCommand:
    def __init__(self, game_id, question, action):
        self.game_id = int(game_id)
        self.prompt = question
        self.action = action

    def ask_for_command(self):
        pass


class YesNoQuestion(AskForCommand):
    def ask_for_command(self):
        """Asks user the question given as a parameter. Returns a dictionary with values
        "yes": Boolean and "finished": Boolean. "yes" tells whether the user answered yes or no
        to the question and "finished" tells whether the user gave finish command or not.
        """
        answer = input(self.prompt).lower
        while answer not in [yes, no, end_command]:
            answer = command_to_action(self.game_id, answer)
        if answer == yes:
            return {"yes": True, "finished": False}
        elif answer == no:
            return {"yes": False, "finished": False}
        elif answer == end_command:
            return {"yes": False, "finished": True}


class ContinueQuestion(AskForCommand):
    def ask_for_command(self):
        """Asks user the question given as a parameter.
        """
        answer = input(self.prompt).lower
        while answer not in [approve, end_command]:
            answer = command_to_action(self.game_id, answer)
        if answer == approve:
            return {"yes": True, "finished": False}
        elif answer == end_command:
            return {"yes": False, "finished": True}'''
