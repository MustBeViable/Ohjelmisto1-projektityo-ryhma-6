from Game.game_texts import yhteys

#Luo listan pelaajan makkaroista joita pelaajalla on. Parametri on pelaajan uniikki id.
def fetch_player_makkaras(id):
    sql = (f" SELECT id"
           f" FROM makkara_reached"
           f" where playthrough_id = '{id}'"
           f" and stolen = False")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    player_makkaras = []
    for i in range(len(result)):
        player_makkaras.append(result[i][0])
    return player_makkaras

def fetch_player_stolen_makkaras(id):
    sql = (f" SELECT id"
           f" FROM makkara_reached"
           f" where playthrough_id = '{id}'"
           f" and stolen = True")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    player_makkaras = []
    for i in range(len(result)):
        player_makkaras.append(result[i][0])
    return player_makkaras
