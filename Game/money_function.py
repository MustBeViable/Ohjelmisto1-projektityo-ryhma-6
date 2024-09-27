def add_money(amount):
    sql = (f'UPDATE game SET money = ''WHERE id = {game_id};')
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def use_money():
    sql = (f"SELECT money FROM game WHERE id = {game_id};")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    print(result)
    return result