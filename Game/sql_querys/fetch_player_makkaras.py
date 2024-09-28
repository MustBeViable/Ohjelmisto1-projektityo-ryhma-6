from Game.game_texts import yhteys

#Luo listan pelaajan makkatoista joita pelaajalla on. Parametri on pelaajan uniikki id, pitäs varmaa tarkentaa
# screen_name kanssa?
def fetch_player_makkaras1(id):
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

def fetch_player_makkaras2(id, screen_name):
    sql = (f" SELECT makkara_id"
           f" FROM makkara_reached, playthrough"
           f" where game_id = playthrough.id"
           f" AND game_id = '{id}'"
           f" AND screen_name = '{screen_name}'")
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    player_makkaras = []
    for i in range(len(result)):
        player_makkaras.append(result[i][0])
    return player_makkaras

'''
koloherra = 'koloherra'
print(fetch_player_makkaras2(1,koloherra))
'''