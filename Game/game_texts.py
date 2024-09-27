# All the commands that the user can give.
import mysql.connector

yes = "k"
no = "e"

help_command = "ohje"
fly_command = "lennä"

# Dictionary of commands that are normally available and their help texts.
command_and_helptext = {
    help_command: "Näyttää ohjeen.",
    fly_command: "Avaa valikon, josta voit valita, mille lentokentälle lennät seuraavaksi.",
}

# All game texts
give_commmand_str = 'Anna komento: '

not_command_str = (' ei  ole komento, syötä jokin tunnistettava komento. '
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


yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='tuukka',
         password='Muumilaakso',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )
