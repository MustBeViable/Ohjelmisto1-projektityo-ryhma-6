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

sql_makkara1 = (f"DROP TABLE IF EXISTS playthrough;")
sql_makkara2 = (f"CREATE TABLE IF NOT EXISTS makkara ("
               f" id        int NOT NULL AUTO_INCREMENT,"
               f" name      varchar(255),"
               f" score     int,"
               f" country   varchar(40),"
               f" PRIMARY KEY (id));")

sql_makkara_reached1 = (f"DROP TABLE IF EXISTS makkara_reached;")
sql_makkara_reached2 = (f"CREATE TABLE IF NOT EXISTS makkara_reached("
                       f" id            int NOT NULL AUTO_INCREMENT,"
                       f" game_id       int,"
                       f" makkara_id    int,"
                       f" PRIMARY KEY (id));")

sql_makkaras_in_hole1 = (f"DROP TABLE IF EXISTS makkaras_in_hole;")
sql_makkaras_in_hole2 = (f"CREATE TABLE IF NOT EXISTS makkaras_in_hole ("
                         f"stolen_makkara_id    int,"
                        f" playthrough_id       int,"
                        f" PRIMARY KEY (stolen_makkara_id));")


fk_makkara_reached_sql = (f" ALTER TABLE makkara_reached"
                          f" ADD CONSTRAINT FK_game_id FOREIGN KEY (game_id) REFERENCES playthrough(id) ON DELETE CASCADE ON UPDATE CASCADE,"
                          f" ADD CONSTRAINT FK_makkara_id foreign key (makkara_id) references makkara(id) ON DELETE CASCADE ON UPDATE CASCADE;")

#Constraintin lisäämällä teet elämästä huomattavasti helpompaa kun poistat FK yhdistelmiä. Nimi voi olla muute hankala
fk_playthrough_sql = (f" ALTER TABLE playthrough "
                      f" ADD CONSTRAINT FK_location"
                      f" FOREIGN KEY (location) REFERENCES airport(ident) ON DELETE CASCADE ,"
                      f" ADD CONSTRAINT FK_hole_airport"
                      f" FOREIGN KEY (hole_airport) REFERENCES airport(ident) ON DELETE CASCADE;")


fk_makkara_sql = (f" ALTER TABLE makkara"
                  f" ADD CONSTRAINT FK_iso_country"
                  f" FOREIGN KEY (country) REFERENCES country(iso_country) ON DELETE CASCADE;")


fk_makkaras_in_hole_sql = (f" ALTER TABLE makkaras_in_hole"
                           f" ADD CONSTRAINT FK_makkara_reached_id"
                           f" FOREIGN KEY (makkara_reached) REFERENCES makkara_reached(id) ON DELETE CASCADE;")

kursori = yhteys.cursor()
kursori.execute(sql_playthrough1)
kursori.execute(sql_playthrough2)
print("Playthrough luotiin.")

kursori.execute(sql_makkara1)
kursori.execute(sql_makkara2)
print("Makkara luotiin.")

kursori.execute(sql_makkara_reached1)
kursori.execute(sql_makkara_reached2)
print("Makkara_reached luotiin.")

kursori.execute(sql_makkaras_in_hole1)
kursori.execute(sql_makkaras_in_hole2)
print("Makkaras_in_hole luotiin.")

kursori.execute(fk_makkara_reached_sql)
print("Makkaras_reached tehtiin fk.")

kursori.execute(fk_playthrough_sql)
print("Playthrough tehtiin fk.")

kursori.execute(fk_makkara_sql)
print("Makkara tehtiin fk.")

kursori.execute(fk_makkaras_in_hole_sql)
print("Makkaras_in_hole tehtiin fk.")