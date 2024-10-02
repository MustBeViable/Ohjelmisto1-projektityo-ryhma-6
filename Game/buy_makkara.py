from Game.sql_querys.money_function import update_player_money, fetch_player_money

country_makkara="country makkara"

#def buy(original_money, price):
    #new_money = original_money - price
    #return new_money

#Jos törmäät outoon bugiin tuo parametreinä ei globaaleina muutujat.
def buy_makkara(price):

    player_money=player_money-price
    own_makkaras.append(country_makkara)
    fetch_player_money(price)
    return own_makkaras, player_money
makkara_price=500
player_money=fetch_player_money()
update_player_money(amount)

#print(buy(1000, 20))
#print(buy_makkara(makkara_price))
