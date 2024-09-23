from Game.player_profile import own_money, own_makkaras

country_makkara="country makkara"

def buy(original_money, price):
    new_money = original_money - price
    return new_money

#Jos törmäät outoon bugiin tuo parametreinä ei globaaleina muutujat.
def buy_makkara(price):
    global own_money, own_makkaras
    own_money=own_money-price
    own_makkaras.append(country_makkara)
    return own_makkaras, own_money

makkara_price=500
player_money=10000

print(buy(1000, 20))
print(buy_makkara(makkara_price))
