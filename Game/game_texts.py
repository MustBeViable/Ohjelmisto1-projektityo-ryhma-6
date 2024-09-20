# All the commands that the user can give.
ask_help = "ohje"
komento = "komento"
toinen_komento = "toinen_komento"

# Dictionary of commands and their help texts.
command_and_helptext = {
    ask_help: "Näyttää ohjeen.",
    komento: "Tekee jotain.",
    toinen_komento: "Tekee jotain muuta."
}

# All game texts
give_commmand = 'Anna komento: '

not_command = ('Tuo ei  ollut komento. '
               'Komennolla "ohje" näet kaikki mahdolliset komennot. ')

game_instruction = (f'PELIN OHJE\n'
                    f'Kirjoita haluamasi komento ja paina enter. \n')

game_goal = (f'PELIN TAVOITE\n'
            f'Pelin tavoite on kerätä mahdollisimman paljon makkaroita.\n'
            f'Erilaisista makkaroista saa enemmän pisteitä.\n'
            f'Peli päättyy, kun rahasi loppuvat tai käytät lopetuskomentoa.\n')


commands = f'KOMENNOT\n'

for com in command_and_helptext.keys():
    commands += f'{com}: {command_and_helptext[com]}\n'

give_help = (f"\n"
             f"{game_instruction}\n"
             f"{commands}\n"
             f"{game_goal}"
             )
