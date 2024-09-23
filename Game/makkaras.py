import mysql.connector


yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='eliasellu',
         password='Koira123',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )

# def fetch_makkara():
#    sql = (f"SELECT makkara.name, iso_country"
#           f" FROM makkara INNER JOIN country")
