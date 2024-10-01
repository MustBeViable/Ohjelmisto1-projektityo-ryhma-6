from Game.game_texts import yhteys

def all_unique_player_score_fetch_query(screen_name):
    sql = (f" SELECT screen_name, score"
           f" FROM playthrough"
           f" WHERE screen_name = '{screen_name}'")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    result_sorted = sorted(result, key=lambda x: x['score'], reverse=True)
    print(f"Pelaajan {screen_name} kaikkien scorejen lista")
    for i in range(len(result_sorted)):
         print(f"{result_sorted[i]['screen_name']}: {result_sorted[i]['score']:6.0f}")
    return

def unique_player_top_5_score_fetch_query(screen_name):
    sql = (f" SELECT screen_name, score"
           f" FROM playthrough"
           f" WHERE screen_name = '{screen_name}'")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    result_sorted = sorted(result, key=lambda x: x['score'], reverse=True)
    print(f"Pelaajan {screen_name} top 5 lista")
    if len(result_sorted) < 5:
        for i in range(len(result_sorted)):
            print(f"{result_sorted[i]['screen_name']}: {result_sorted[i]['score']:6.0f}")
    else:
        for i in range(5):
         print(f"{result_sorted[i]['screen_name']}: {result_sorted[i]['score']:6.0f}")
    return


unique_player_top_5_score_fetch_query('koloherra')
print("")
all_unique_player_score_fetch_query('koloherra')