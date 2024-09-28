from Game.game_texts import yhteys

# siirrä muualle
unfinished = "unfinished"
finished = "finished"

start_money = "1000"
unfinished = "unfinished"
finished = "finished"
start_location = "EFNU"

def sql_connection(sql_text):
    kursori = yhteys.cursor()
    kursori.execute(sql_text)
    result = kursori.fetchall()
    return result

# Creates the game to the database with given screen name. Returns the ID of the new game.
def create_game(screen_name):
    sql_create = (f"INSERT INTO playthrough (score, money, screen_name, status, location) VALUES ('0', {start_money}, '{screen_name}', '{unfinished}', '{start_location}')")
    sql_connection(sql_create)
    sql_id = (f"SELECT id FROM playthrough WHERE screen_name = '{screen_name}' AND status = '{unfinished}' ORDER BY id DESC")
    sql_connection(sql_id)
    new_id = sql_connection(sql_id)[0][0]
    return new_id

def finish_game_in_database(finish_id):
    sql = (f"UPDATE playthrough SET status = '{finished}' WHERE id = '{finish_id}'")
    sql_connection(sql)
    return

'''# testi create_game
k_e = input("Luo uusi käyttäjä? k/e")
if k_e == "k":
    testname = input("Anna testikäyttäjälle nimi: ")
    create_game(testname)
    sql1 = (f"SELECT * FROM playthrough")
    test1 = sql_connection(sql1)
    print("uusi pelikerta oli:")
    print(test1[-1])
    print("kaikki pelikerrat: ")
    print(test1)'''