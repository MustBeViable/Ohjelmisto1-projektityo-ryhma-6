from Game.game_texts import yhteys
from Game.sql_querys.create_and_end_game import start_location

start_score = 0
start_money = 1000
start_mustamakkara = 0

sql_playthrough1 = (f"DROP TABLE IF EXISTS playthrough;")
sql_playthrough2 = (f" CREATE TABLE IF NOT EXISTS playthrough ("
                    f" id           int NOT NULL AUTO_INCREMENT,"
                    f" score        int         DEFAULT {start_score},"
                    f" money        int         DEFAULT {start_money},"
                    f" screen_name  varchar(40),"
                    f" finished     boolean     DEFAULT false,"
                    f" mustamakkara int         DEFAULT {start_mustamakkara},"
                    f" hole_airport varchar(40),"
                    f" location     varchar(40),"
                    f" PRIMARY KEY(id));")

sql_makkara1 = (f" DROP TABLE IF EXISTS playthrough;")
sql_makkara2 = (f" CREATE TABLE IF NOT EXISTS makkara ("
                f" id        int NOT NULL AUTO_INCREMENT,"
                f" name      varchar(255),"
                f" score     int,"
                f" country   varchar(40),"
                f" PRIMARY KEY (id));")

sql_makkara_reached1 = (f" DROP TABLE IF EXISTS makkara_reached;")
sql_makkara_reached2 = (f" CREATE TABLE IF NOT EXISTS makkara_reached("
                        f" id            int NOT NULL AUTO_INCREMENT,"
                        f" game_id       int,"
                        f" makkara_id    int,"
                        f" PRIMARY KEY (id),"
                        f"FOREIGN KEY (game_id)"
                        f"  REFERENCES playthrough(id) ON DELETE CASCADE ON UPDATE CASCADE,"
                        f" FOREIGN KEY (makkara_id)"
                        f"  REFERENCES makkara(id) ON DELETE CASCADE ON UPDATE CASCADE);")

sql_makkaras_in_hole1 = (f" DROP TABLE IF EXISTS makkaras_in_hole;")
sql_makkaras_in_hole2 = (f" CREATE TABLE IF NOT EXISTS makkaras_in_hole ("
                         f" stolen_makkara_id    int,"
                         f" playthrough_id       int,"
                         f" PRIMARY KEY (stolen_makkara_id),"
                         f" FOREIGN KEY (stolen_makkara_id)"
                         f"     REFERENCES makkara_reached(id) ON DELETE CASCADE ON UPDATE CASCADE);")

kursori = yhteys.cursor()

kursori.execute(sql_makkara1)
kursori.execute(sql_makkara2)
print("Makkara luotiin.")

kursori.execute(sql_playthrough1)
kursori.execute(sql_playthrough2)
print("Playthrough luotiin.")

kursori.execute(sql_makkara_reached1)
kursori.execute(sql_makkara_reached2)
print("Makkara_reached luotiin.")

kursori.execute(sql_makkaras_in_hole1)
kursori.execute(sql_makkaras_in_hole2)
print("Makkaras_in_hole luotiin.")