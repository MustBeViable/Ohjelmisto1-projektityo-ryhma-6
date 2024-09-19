import random
#funtion parametreiks syötetään pelaajan rahat, mitä tuplaa ja monesko tuplaus menossa
def tuplaus(amount, times):
    luckynumber = random.randint(1, 100)
    print(luckynumber)
    #Tässä määritän voittavan mahiksen suoraa random generaattorista ja jokaisella uudella tuplauskerralla vähennän 10
    #jotta tuplaus vaikeutuisi
    chance1 = luckynumber - (times * 10)
    print(chance1)
    #Tässä määritän "kolikon" toisen puolen. Se on maximi (100, määritetty randintisä) - randomoitu tulos ja lisätään
    # siihen tuo mahdollinen uusien tuplauksien vaikutus
    chance2 = 100 - luckynumber + (times * 10)
    print(chance2)
    #tässä tarkistetaan saiko käyttäjä yli 50, eli 50/50 mahdollisuus ekalla tuplausyrityksellä. Jos tämä onnistuu
    #tuplaan rahat eli amount*2
    if chance1 > chance2:
        print("Tuplaus onnistui!")
        amount = amount * 2
        print(amount)
    else:
        print("Tuplaus epäonnistui!")
        amount = 0
        return amount
def tuplataanko(answer, winnings):
    if answer == "KYLLÄ":
        while answer == "KYLLÄ" and winnings > 0:
            if tuplataanko == "KYLLÄ":
                times = 0
                winnings = tuplaus(winnings, times)
                print(winnings)
                times += 1
                if winnings > 0:
                    answer = input(
                        "Roskiksen keiju tarjoaa mahdollisuuden tuplata tämän rahan!"
                        " Mitä vastaat? (Kyllä/Ei): ").upper()
    else:
        pass
    return winnings
vastaus = input("Vastaus: ").upper()
maara = int(input("Maara: "))
tuplataanko(vastaus,maara)