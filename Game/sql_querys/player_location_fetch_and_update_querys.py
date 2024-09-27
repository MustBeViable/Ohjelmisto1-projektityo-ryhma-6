from Game.game_texts import yhteys


def fetch_player_location(id):
    sql = (f" SELECT location"
           f" FROM playthrough"
           f" WHERE id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    current_location = result[0][0]
    print(current_location)
    return current_location

def update_player_location(id, new_location):
    sql = (f" UPDATE playthrough"
           f" SET location = '{new_location}'"
           f" WHERE id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
