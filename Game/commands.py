from Game.actions import give_help, show_money, show_makkaras, cant_end_now, give_commands, show_score, faulty_command
from Game.game_texts import help_command, yes, no, end_command, makkaras_command, money_command, approve, \
    give_up_command, commands_command, commands_str, score_command, not_command_str


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
give_help_command_action = Command(help_command, give_help, "Näyttää ohjeen.")
show_money_command_action = CommandWithParameter(money_command, show_money, "Näyttää sen hetkiset rahasi.")
show_makkara_amount_command_action = CommandWithParameter(makkaras_command, show_makkaras, "Näyttää omien makkaroidesi määrän.")
commands_command_action = Command(commands_command, give_commands, "Näyttää peruskomennot.")
score_command_action = CommandWithParameter(score_command, show_score, "Näyttää pisteesi.")
cant_end_command_action = Command(end_command, cant_end_now, "Sulkee pelin. Edistymisen tallentuu automaattisesti ja voit palata jatkamaan peliä profiilistasi.")
give_up_command_action = Command(give_up_command, cant_end_now, "Lopettaa pelin. Luovuttamisen jälkeen et voi enää jatkaa kyseistä pelikertaa.")

basic_commands = [give_help_command_action,
                 show_money_command_action,
                 show_makkara_amount_command_action,
                 commands_command_action,
                 score_command_action,
                 cant_end_command_action,
                 give_up_command_action
                 ]

out_section_commands = [c for c in basic_commands if c not in [cant_end_command_action, give_up_command_action]]

in_section_commands = [c for c in basic_commands if c not in [give_up_command_action]]

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
    command_was_basic_command = execute_basic_command(answer, game_id, out_section_commands)
    if command_was_basic_command:
        answer = input_outside_section(prompt, game_id)
    return answer

'''
def outside_section_boolean_question(question, action, game_id,):
    """Asks the user the given question until answered yes, no, give up command or end command.
    If the user answers yes, executes the given action. If the user answers no, does nothing.
    Returns [Boolean, Boolean] meaning [player wants to end game, player wants to give up]
    """
    answer = input_outside_section(question, game_id)
    while answer not in [yes, no, end_command]:
        answer = input_outside_section(question, game_id)
    if answer == end_command:
        return [True, False]
    if answer == give_up_command:
        return [True, True]
    if answer == yes:
        action(game_id)
    return [False, False]

def outside_section_continue_question(question, action, game_id):
    """Asks the user the given question until answered approved or end command.
        If the user approves to continue, executes the given action.
        Returns Boolean: whether the player wants to end the game or not.
        """
    answer = input_outside_section(question, game_id)
    while answer not in [approve, end_command]:
        answer = input_outside_section(question, game_id)
    if answer == end_command:
        return True
    if answer == approve:
        action(game_id)
    return False
    '''

def outside_section_question(question, action, accepted_commands, other_commands, game_id):
    """Asks the user the given question until answered one of the given commands, give-up-command or end-command.
    If the user answers yes, executes the given action. If the user answers no, does nothing.
    Returns {end: Boolean, give up: Boolean} meaning {end: player wants to end game, give up: player wants to give up}
    """
    answer = input_outside_section(question, game_id)
    while answer not in ([end_command, give_up_command] + accepted_commands + other_commands):
        faulty_command(answer)
        answer = input_outside_section(question, game_id)
    if answer == end_command:
        return {"finish": True, "give up": False}
    if answer == give_up_command:
        return {"finish": True, "give up": True}
    if answer in accepted_commands:
        action(game_id)
    return {"finish": False, "give up": False}


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
