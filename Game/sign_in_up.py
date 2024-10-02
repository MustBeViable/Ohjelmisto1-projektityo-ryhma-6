from Game.sql_querys.create_and_end_game import fetch_all_screen_names

sign_up = "uusi"
sign_in = "kirjaudu"
cancel = "peru"
give_screen_name_str = "Anna käyttäjänimi: "
sign_in_or_up_str = f"Kirjoita {sign_in} jos haluat kirjautua sisään. Kirjoita {sign_up} jos haluat luoda uuden käyttäjätunnuksen.\n"


def ask_sign_in_or_up():
    answer = input(sign_in_or_up_str).lower()
    while answer not in [sign_in, sign_up]:
        answer = input(sign_in_or_up_str).lower()
    name = input(give_screen_name_str).lower()
    if answer == sign_up:
        while name in fetch_all_screen_names() and name != cancel:
            print(f"Käyttäjätunnus {name} on jo käytössä. Valitse toinen nimi.\n")
            name = input(give_screen_name_str).lower()
        else:
            print(f"Loit tunnuksen nimellä {name}.")
    elif answer == sign_in:
        while name not in fetch_all_screen_names():
            print(f"Käyttäjätunnusta {name} ei löydy.\n")
            name = input(give_screen_name_str).lower()
    return name