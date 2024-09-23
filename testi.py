import random


# Function that takes player's money and how many times they have doubled
def tuplaus(amount, times):
    luckynumber = random.randint(1, 100)
    print(f"Onnenluku: {luckynumber}")

    # Calculate the chances for the current double attempt
    chance1 = luckynumber - (times * 10)
    chance2 = 100 - luckynumber + (times * 10)

    print(f"Mahdollisuus voittaa (chance1): {chance1}")
    print(f"Mahdollisuus hävitä (chance2): {chance2}")

    # If chance1 is higher than chance2, the player wins
    if chance1 > chance2:
        print("Tuplaus onnistui!")
        amount *= 2
        print(f"Uusi summa: {amount}")
        return amount
    else:
        print("Tuplaus epäonnistui!")
        return 0  # Player loses all money


def tuplataanko(answer, winnings):
    times = 0  # Initialize times outside the loop to track attempts
    while answer == "KYLLÄ" and winnings > 0:
        winnings = tuplaus(winnings, times)
        times += 1  # Increment times with each double attempt

        if winnings > 0:
            # Ask if the player wants to double again
            answer = input(
                "Roskiksen keiju tarjoaa mahdollisuuden tuplata tämän rahan! "
                "Mitä vastaat? (Kyllä/Ei): ").upper()
        else:
            # Player lost all money
            print("Kaikki rahat menivät!")
            break

    return winnings


# Get user input
vastaus = input("Haluatko tuplata? (Kyllä/Ei): ").upper()
maara = int(input("Paljonko rahaa on panoksena: "))

# Call the function
lopputulos = tuplataanko(vastaus, maara)
print(f"Lopullinen summa: {lopputulos}")
