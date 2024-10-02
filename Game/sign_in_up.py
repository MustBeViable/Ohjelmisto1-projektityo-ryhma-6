from Game.sql_querys.create_and_end_game import fetch_all_screen_names

sign_up = "uusi"
sign_in = "kirjaudu"
cancel = "peru"
give_screen_name_str = "Anna käyttäjänimi: "
sign_in_or_up_str = f"Kirjoita {sign_in} jos haluat kirjautua sisään. Kirjoita {sign_up} jos haluat luoda uuden käyttäjätunnuksen.\n"

def sign_in_function():
    name = input(give_screen_name_str).lower()
    while name not in fetch_all_screen_names() and name != cancel:
        print(f"Käyttäjätunnusta {name} ei löydy.\n")
        name = input(give_screen_name_str).lower()
    return name

def sign_up_function():
    name = input(give_screen_name_str).lower()
    while name in fetch_all_screen_names() and name != cancel:
        print(f"Käyttäjätunnus {name} on jo käytössä. Valitse toinen nimi.\n")
        name = input(give_screen_name_str).lower()
    return name

def ask_sign_in_or_up():
    answer = input(sign_in_or_up_str).lower()
    if answer == sign_in:
        a = sign_in_function()
    elif answer == sign_up:
        a = sign_up_function()
    else:
        a = ask_sign_in_or_up()
    return a