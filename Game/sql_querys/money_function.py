
from Game.game_texts import yhteys


def add_money(amount, game_id):
    sql = (f"UPDATE playthrough SET money = {amount} WHERE id = '{game_id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def use_money( playthrough_id):
    sql = (f"SELECT money FROM playthrough WHERE id = '{playthrough_id}'")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    player_money = result[0]['money']
    print(player_money)

    return player_money

use_money(1)