from Game.game_texts import yhteys

#Returns makkaras from kolovastaava to player

def return_player_makkaras(id):
    sql = (f" UPDATE makkara_reached"
           f" SET stolen = false"
           f" where playthrough_id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
