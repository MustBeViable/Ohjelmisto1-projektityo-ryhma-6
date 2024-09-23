import random
money=int(random.randint(0,1))
#Pelaajatarina 22 jos rahat loppuvat.
#Funktion paramentriksi pelaajan rahat, jos rahat<=0 peli päättyy.
#Tulee myös kysymys, mitä pelaaja haluaa tehdä seuraavaksi.
def tryendgame(money):
    if money<=0:
        print("Rahat loppuivat, hävisit pelin.")
        game_end=input("Haluatko nähdä laedboardin, pelata uudestaan vai lopettaa?")
        return game_end
if money<=0:
    tryendgame(money)
print("jatkuu")