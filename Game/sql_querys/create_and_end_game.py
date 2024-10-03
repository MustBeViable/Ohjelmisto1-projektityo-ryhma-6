from Game.game_texts import yhteys

def sql_connection(sql_text):
    kursori = yhteys.cursor()
    kursori.execute(sql_text)
    result = kursori.fetchall()
    return result

# Creates the game to the database with given screen name. Returns the ID of the new game.
def create_game(screen_name):
    sql_create = (f"INSERT INTO playthrough (screen_name) VALUES ('{screen_name}')")
    sql_connection(sql_create)
    sql_id = (f"SELECT id FROM playthrough WHERE screen_name = '{screen_name}' AND finished = false ORDER BY id DESC")
    sql_connection(sql_id)
    new_id = sql_connection(sql_id)[0][0]
    return new_id

# Marks the game with the given id as finished in the databased.
def finish_game_in_database(finish_id):
    sql = (f"UPDATE playthrough SET finished = true WHERE id = '{finish_id}'")
    sql_connection(sql)
    return


# Fetches unfinished playthroughs of the player. Returns a list of the unfinished playthroughs.
# Returns an empty list if there are no unfinished playthroughs.
def fetch_unfinished_playthrough(screen_name):
    sql = (f"SELECT id FROM playthrough WHERE screen_name = '{screen_name}' AND finished = false")
    unfinished_game_list = sql_connection(sql)
    return unfinished_game_list

# Returns each screen name ones.
def fetch_all_screen_names():
    sql = (f"select distinct screen_name from playthrough;")
    screen_names_list = sql_connection(sql)
    fine_screen_name_list = []
    for name in screen_names_list:
        fine_screen_name_list.append(name[0])
    return fine_screen_name_list

# testi create_game
'''k_e = input("Luo uusi käyttäjä? k/e")
if k_e == "k":
    testname = input("Anna testikäyttäjälle nimi: ")
    create_game(testname)
    sql1 = (f"SELECT * FROM playthrough")
    test1 = sql_connection(sql1)
    print("uusi pelikerta oli:")
    print(test1[-1])
    print("kaikki pelikerrat: ")
    print(test1)'''