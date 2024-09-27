
# ei toimi vielä !!!!!!!!

# !!!!!!!!!!!!!!!!!! kysely väärin !!!!!!!!!!!!!!
def update_makkara_taxfree():
    sql = (f"SELECT id FROM makkara_reached WHERE id = {game_id};")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    print(result)
    return result
