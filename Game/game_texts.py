# All the commands that the user can give.
import mysql.connector

yes = "k"
no = "e"

game_id = 1

start_money = 1000
start_score = 0
start_mustamakkara = 0
start_location = "EFNU"
sausage_price = 100

help_command = "ohje"
fly_command = "lennä"
end_command = "lopeta"
give_up_command = "luovuta"

# Dictionary of commands that are normally available and their help texts.
command_and_helptext = {
    help_command: "Näyttää ohjeen.",
    end_command: "Sulkee pelin. Edistymisen tallentuu automaattisesti ja voit palata jatkamaan peliä profiilistasi.",
    give_up_command: "Lopettaa pelin. Luovuttamisen jälkeen et voi enää jatkaa kyseistä pelikertaa."
}


# All game texts
give_commmand_str = 'Anna komento: '

not_command_str = (' ei  ole komento, syötä jokin tunnistettava komento. '
                   'Komennolla "ohje" näet kaikki mahdolliset komennot. ')

not_command_yes_no_str = (f' ei  ole komento. Komennolla "{yes}" vastaat kyllä, '
                          f'komennolla "{no}" vastaat ei. '
                          'Komennolla "ohje" näet kaikki mahdolliset komennot. ')

game_instruction_str = (f'PELIN OHJE\n'
                        f'Kirjoita konsoliin haluamasi komento ja paina enter. \n')

game_goal_str = (f'PELIN TAVOITE\n'
                 f'Pelin tavoite on kerätä mahdollisimman paljon makkaroita.\n'
                 f'Makkaroita voi ostaa lentokenttien Tax free -myymälöistä. Kullakin maalla on oma makkaransa.\n'
                 f'Erilaisista makkaroista saa enemmän pisteitä.\n'
                 f'Peli päättyy, kun rahasi loppuvat tai käytät lopetuskomentoa.\n')

# String of commands and what they do
commands_str = f'KOMENNOT\n'

for com in command_and_helptext.keys():
    commands_str += f'{com}: {command_and_helptext[com]}\n'

# Combines all instructions to one manual.
give_help_str = (f"\n"
                 f"{game_instruction_str}\n"
                 f"{commands_str}\n"
                 f"{game_goal_str}")

dumpster_question = "Haluatko kaivaa roskista? "
fligh_question = "Haluatko lentää? "
tax_free_question = "Haluatko shoppailla? "

yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='makkara_game',
         user='palautukset',
         password='moro3',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )
