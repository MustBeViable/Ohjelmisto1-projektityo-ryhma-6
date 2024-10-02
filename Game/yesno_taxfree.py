from Game.game_texts import sausage_price, no, yes
from Game.sql_querys.makkara_sql_haku import search_makkara, search_makkara_id
from Game.sql_querys.money_function import fetch_player_money
from Game.taxfree import taxfree
#Asking do you want to buy makkara from taxfree

def yes_no_taxfree(game_id):
    print(f"Sinulla on {fetch_player_money(game_id)}€ rahaa. Taxfreestä löytyi hieno {search_makkara(game_id)}"
                         f" ja se maksaa {sausage_price}€.")
    taxfree_answer=input(f"Haluatko ostaa sen? ({yes}/{no})")
    while taxfree_answer not in [yes, no]:
        taxfree_answer = input(f"Haluatko ostaa sen? ({yes}/{no})")


    if taxfree_answer == yes :
                taxfree(fetch_player_money(game_id), search_makkara_id(game_id), game_id)





