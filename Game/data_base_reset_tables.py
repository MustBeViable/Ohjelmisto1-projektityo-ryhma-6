from game_texts import yhteys

def table_remove(table):
    sql = "DROP TABLE {table} "
    kursori = yhteys.cursor()
    kursori.execute(sql.format(table=table))
    return
#lisää listaa tablen nimi ku lisäät uuden tablen tietokantaa
test_list = ["makkara", "makkara_reached", "playthrough"]
for i in test_list:
    table_remove(table=i)