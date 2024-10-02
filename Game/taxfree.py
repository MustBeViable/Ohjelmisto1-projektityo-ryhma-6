from Game.game_texts import game_id, sausage_price
from sql_querys.makkara_taxfree_sql_update import add_makkara_reached
from sql_querys.makkara_sql_haku import search_makkara, search_makkara_id
from sql_querys.money_function import add_money, use_money


def taxfree(player_money, makkara_ID):
    makkara_name = search_makkara()
    add_makkara_reached(game_id,makkara_ID)
    new_money=player_money-sausage_price
    add_money(new_money,game_id)
    print(f"Ostit makkaran {makkara_name} ja se maksoi {sausage_price} euroa. Sinulla on nyt {new_money} €.")
    return

taxfree(use_money(game_id),search_makkara_id())

