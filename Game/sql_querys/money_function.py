
def add_money(amount):
    sql = (f'UPDATE game SET money = {amount} WHERE id = {game_id};')
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def use_money(spent):
    sql = (f"SELECT money FROM game WHERE id = {game_id};")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    new_money = result[0]['money']
    new_money -= spent
    add_money(new_money)
    print(result)
    return result
#monke