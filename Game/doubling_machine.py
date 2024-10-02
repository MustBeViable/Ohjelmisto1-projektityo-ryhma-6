import random

from Game.game_texts import yes, no, game_id
from Game.sql_querys.money_function import use_money, add_money


#funtion parametreiks syötetään pelaajan rahat, mitä tuplaa ja monesko tuplaus menossa
#HUOM! Voidaan halutessa tuoda muuttuva lukuarvo muuttujan avulla, jolla kerrannoidaan, kuinka mahdollisuudet putoo.
#itse suosittelen 5 tai 10.
def tuplaus(amount, times):
    luckynumber = random.randint(1, 100)
    #Tässä määritän voittavan mahiksen suoraa random generaattorista ja jokaisella uudella tuplauskerralla vähennän 5
    #jotta tuplaus vaikeutuisi
    chance1 = luckynumber - (times * 5)
    # Tämä on testi printti poista valmiiseen ohjelmaan
    #Tässä määritän "kolikon" toisen puolen. Se on maximi (100, määritetty randintisä) - randomoitu tulos ja lisätään
    # siihen tuo mahdollinen uusien tuplauksien vaikutus
    chance2 = 100 - luckynumber + (times * 5)
    # Tämä on testi printti poista valmiiseen ohjelmaan
    #tässä tarkistetaan saiko käyttäjä yli 50, eli 50/50 mahdollisuus ekalla tuplausyrityksellä. Jos tämä onnistuu
    #tuplaan rahat eli amount*2
    #Sakke olen täällä
    if chance1 >= chance2:
        print("Tuplaus onnistui!")
        amount = amount * 2
        print(f"Tällä hetkellä sinulla on {amount}€.")
        return amount
    else:
        print("Tuplaus epäonnistui!")
        return 0
#HUOM! Vaatii ylemmän funktion toimiakseen!
#funktio tallentaa iteroi montako kertaa pelaaja on jo tuplannut. Se myös tarkistaa onko pelaaja jo hävinnyt
def tuplataanko(answer, winnings):
        times = 0
        #Tässä tarkistetaa halusiko pelaaja tuplata ja oliko pelaaja jo hävinnyt rahansa lisäksi alhaalla seurataa
        #monesko tuplaus kerta menossa
        while answer == yes and winnings > 0:
            if answer == yes:
                winnings = tuplaus(winnings, times)
                times += 1
                #Tässä tarkisteetaa tuplauskierroksen tulos. Jos pelaaja häviää, ohjelma ei kysy haluaako hän tuplata
                #hävityt rahat.
                if winnings > 0:
                    answer = input(f"Roskiksen keiju tarjoaa mahdollisuuden tuplata tämän rahan."
                        f" Mitä vastaat? ({yes}/{no}): ").lower()
                else:
                    print("Tuplaus epäonnistui!")
                    break
            current_money = use_money(game_id)
            current_money += winnings
            current_money = add_money(game_id, current_money)
            print(f"Sinulla on tällä hetkellä rahaa {current_money}€.")
        return winnings
'''
#Testailin alhaalla että funktiot toimii halutulla tavalla
vastaus = input(f"Roskiksen keiju tarjoaa mahdollisuuden tuplata tämän rahan!"
                        f" Mitä vastaat? ({yes}/{no}): ").lower()
raha_maara = 1000
tuplataanko(vastaus,maara)
'''