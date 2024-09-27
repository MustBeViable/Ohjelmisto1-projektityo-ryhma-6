from Game.game_texts import yhteys


def fetch_player_makkaras(id):
    sql = (f" SELECT makkara_id"
           f" FROM makkara_reached"
           f" where game_id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    player_makkaras = []
    for i in range(len(result)):
        player_makkaras.append(result[i][0])
    return player_makkaras
