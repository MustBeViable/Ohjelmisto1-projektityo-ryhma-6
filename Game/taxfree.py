from Game.game_texts import game_id, sausage_price
from Game.sql_querys.score_fetch_and_score_update_querys import player_score_fetch, player_score_update
from sql_querys.makkara_taxfree_sql_update import add_makkara_reached
from sql_querys.makkara_sql_haku import search_makkara, search_makkara_id, search_makkara_score
from sql_querys.money_function import update_player_money, fetch_player_money


def taxfree(player_money, makkara_ID):
    makkara_name = search_makkara()
    add_makkara_reached(game_id,makkara_ID)
    new_money=player_money-sausage_price
    update_player_money(new_money, game_id)
    new_player_score=player_score_fetch(game_id)+search_makkara_score()
    player_score_update(new_player_score,game_id)
    print(f"Ostit makkaran {makkara_name} ja se maksoi {sausage_price} euroa. Sinulla on nyt {new_money} €.")
    return

taxfree(fetch_player_money(game_id), search_makkara_id())
print(player_score_fetch(game_id))

