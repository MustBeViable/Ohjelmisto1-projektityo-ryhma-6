from Game.game_texts import yhteys

#Luo listan pelaajan makkatoista joita pelaajalla on. Parametri on pelaajan uniikki id, pitäs varmaa tarkentaa
# screen_name kanssa?
def fetch_player_makkaras(id):
    sql = (f" SELECT makkara_id"
           f" FROM makkara_reached"
           f" where playthrough_id = '{id}'")
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