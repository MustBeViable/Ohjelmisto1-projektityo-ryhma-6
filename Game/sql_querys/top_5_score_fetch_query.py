from Game.game_texts import yhteys


def top_5_score_fetch_query():
    sql = (f" SELECT screen_name, score"
           f" FROM playthrough")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    result_sorted = sorted(result, key=lambda x: x['score'], reverse=True)
    for i in range(5):
         print(f"{result_sorted[i]['screen_name']}: {result_sorted[i]['score']:6.0f}")
    return

#top_5_score_fetch_query()