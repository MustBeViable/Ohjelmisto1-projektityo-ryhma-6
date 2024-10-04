# All the commands that the user can give.
import mysql.connector

yes = "k"
no = "e"
approve = "j"

start_money = 1000
start_score = 0
start_mustamakkara = 0
start_location = "EFNU"
sausage_price = 100
finnair_makkara = 69420
finnair_donation = 500
price_multiplier = 50


help_command = "ohje"
commands_command = "komennot"
end_command = "lopeta"
give_up_command = "luovuta"
money_command = "bank"
makkaras_command = "makkarat"
cancel_command = "palaa"
score_command = "pisteet"

# Dictionary of commands that are normally available and their help texts.
command_and_helptext = {
    money_command: "Näyttää omat rahasi.",
    makkaras_command: "Näyttää omat makkarasi.",
    score_command: "Näyttää pisteesi.",
    commands_command: "Näyttää peruskomennot.",
    help_command: "Näyttää ohjeen.",
    end_command: "Sulkee pelin. Edistymisen tallentuu automaattisesti ja voit palata jatkamaan peliä profiilistasi.",
    give_up_command: "Lopettaa pelin. Luovuttamisen jälkeen et voi enää jatkaa kyseistä pelikertaa."
}


# All game texts
give_commmand_str = 'Anna komento: '

not_command_str = (' ei  ole komento, syötä jokin tunnistettava komento. '
                   'Komennolla "komennot" näet kaikki peruskomennot. ')

not_command_yes_no_str = (f' ei  ole komento. Komennolla "{yes}" vastaat kyllä, '
                          f'komennolla "{no}" vastaat ei. '
                          'Komennolla "komennot" näet kaikki peruskomennot. ')

game_instruction_str = (f'PELIN OHJE\n'
                        f'Sinulta kysytään kysymys. Kirjoita konsoliin haluamasi vastaus ja paina enter. '
                        f'Voit kirjoittaa myös jonkin peruskomennoista (katso alta).\n')

game_goal_str = (f'PELIN TAVOITE\n'
                 f'Pelin tavoite on kerätä mahdollisimman paljon makkaroita ja siten kerryttää pistesaalista.\n'
                 f'Makkaroita voi ostaa lentokenttien Tax free -myymälöistä. Kullakin maalla on oma makkaransa.\n'
                 f'Erilaisista makkaroista saa eri määrän pisteitä.\n'
                 f'Peli päättyy, kun sinulla ei ole enää rahaa ostaa lentolippua.'
                 f'Edistymisesi tallentuu automaattisesti.\n')

# String of commands and what they do
commands_str = f'PERUSKOMENNOT\n'

for com in command_and_helptext.keys():
    commands_str += f'{com}: {command_and_helptext[com]}\n'

# Combines all instructions to one manual.
give_help_str = (f"{game_instruction_str}\n"
                 f"{commands_str}\n"
                 f"{game_goal_str}")

garbage_can_question = f"Haluatko kaivaa roskista? ({yes}/{no})"
fligh_question = "Kävelet kohti lipunmyyntiautomaattia. Paina enter nähdäksesi lähtevät lennot."
tax_free_question = f"Haluatko shoppailla? ({yes}/{no})"

yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='kolovastaava',
         password='kolovastaava',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )
