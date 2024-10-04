from Game.Game_ascii_art.casual_garbage_can import ascii_carbage_can
from Game.airport_selection_function import airportselection
from Game.game_texts import garbage_can_question, yes, no, tax_free_question, fligh_question, approve
from Game.garbage_can import garbage_can
from Game.sql_querys.money_function import fetch_player_money
from Game.taxfree import yes_no_taxfree

class Section:
    """Sections of the game. Each section happens max once in one airport."""
    def __init__(self, question, action, approved_answer, other_answer, art):
        self.question = str(question)
        self.action = action
        self.approved_answer = approved_answer
        self.other_answer = other_answer
        self.art = art

    def check_condition(self, parameter_int):
        """Checks if the player fills the condition that has been set for the section. Returns boolean."""
        return True

class SectionWithNumberCondition(Section):
    def __init__(self, question, action, approved_answer, other_answer, art, function_to_number, condition_minimum, condition_explanation):
        super().__init__(question, action, approved_answer, other_answer, art)
        self.condition_function = function_to_number
        self.condition_minimum = condition_minimum
        self.condition_explanation = condition_explanation

    def check_condition(self, parameter_int):
        if self.condition_function(parameter_int) >= self.condition_minimum:
            return True



garbage_can_section = Section(question=garbage_can_question,
                              action=garbage_can,
                              approved_answer=[yes],
                              other_answer=[no],
                              art=ascii_carbage_can)

tax_free_section = Section(question=tax_free_question,
                           action=yes_no_taxfree,
                           approved_answer=[yes],
                           other_answer=[no],
                           art="")

flight_section = SectionWithNumberCondition(question=fligh_question,
                                            action=airportselection,
                                            approved_answer=[approve],
                                            other_answer=[],
                                            art="",
                                            function_to_number=fetch_player_money,
                                            condition_minimum=50,
                                            condition_explanation="Rahasi eivät riitä enää lentämiseen. ")

