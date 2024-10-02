from Game.game_texts import yhteys
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location

# Returns the name of the makkara in the location
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
    return result[0]["name"]

#returns makkara_id in player location
def search_makkara_id():
    identi = 1
    lokaatio=fetch_player_location(identi)
    sql = (f"SELECT id "
           f"FROM makkara "
           f"WHERE country in("
           f"select iso_country from country where iso_country in("
           f"select iso_country from airport where ident in("
           f"select player_location from playthrough where player_location='{lokaatio}')))")

    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]["id"]

#searches makkaras points from country where player in

def search_makkara_score():
    identi = 1
    lokaatio=fetch_player_location(identi)
    sql = (f"SELECT score "
           f"FROM makkara "
           f"WHERE country in("
           f"select iso_country from country where iso_country in("
           f"select iso_country from airport where ident in("
           f"select player_location from playthrough where player_location='{lokaatio}')))")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]["score"]
