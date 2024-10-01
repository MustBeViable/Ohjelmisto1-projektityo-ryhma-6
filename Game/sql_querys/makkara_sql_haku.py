from Game.game_texts import yhteys
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location


def search_makkara():
    identi = 1
    lokaatio=fetch_player_location(identi)
    sql = (f"SELECT name "
           f"FROM makkara "
           f"WHERE country in("
           f"select iso_country from country where iso_country in("
           f"select iso_country from airport where ident in("
           f"select player_location from playthrough where player_location='{lokaatio}')))")

    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    print(result)
    return result[0]["name"]

print(search_makkara())