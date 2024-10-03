# player makkaras eri komennolla lisäksi, jos haluaa
# player location
# player money
# player score
# player top score ?
# player stolen makkaras
from Game.sql_querys.fetch_player_makkaras import fetch_player_makkaras, fetch_player_stolen_makkaras
from Game.sql_querys.money_function import fetch_player_money
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location, fetch_player_location_name


def profile(game_id):
    print(f"Sijaintisi on tällä hetkellä: {fetch_player_location(game_id)}, {fetch_player_location_name(game_id)}")
    print(f"Sinulla on rahaa {fetch_player_money(game_id)} euroa.")
    #print(f"Sinun scoresi on {score_fetch(game_id)}")
    show_makkarat = input("Jos haluat nähdä keräämäsi makkarat, anna komento 'makkarani'.: ")
    if show_makkarat == 'makkarani':
        print(f"Kolovastaava on vienyt sinulta seuraavat makkarat: {fetch_player_stolen_makkaras(game_id)}")
        print(f"Sinulla on {fetch_player_makkaras(game_id)}")

    if show_makkarat == 'makkarani':
        show_makkarat = {{fetch_player_location_name(game_id)}, {fetch_player_makkaras(game_id)}}
        print(show_makkarat)
profile(2)



