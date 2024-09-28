#Tää puuttu kokonaan nii ei tee sql hakua
from Game.game_texts import yhteys

#lisäsin toiset parametrit molempiin eli game_id, johon syötetään sen pelikerran id. Päivittää siis oikeita tietoja.
# Sama alempaa funktioon. Muutin myös tablen oikeaksi. SQL komento ei tarvitse ";" suorittaakseen oikein.
def add_money(amount, game_id):
    sql = (f"UPDATE playthrough SET money = {amount} WHERE id = '{game_id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
#lisäsin tänne sen game_id parametrin jotta päivitetään aina oikeaa tietoa. Se tuo myös funktion sisällä add_money
# funktioon saman tiedon ja mulla toimi oikein toi nyt.
def use_money(spent, game_id):
    sql = (f"SELECT money FROM playthrough WHERE id = '{game_id}'")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    print(result)
    new_money = result[0]['money']
    print(new_money)
    new_money -= spent
    print(new_money)
    add_money(new_money, game_id)
    return

#use_money(50,1)