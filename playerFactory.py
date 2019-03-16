from player import Player
from testPlayers import *
from myTestPlayers import *
from agentKaito import *

class PlayerFactory:
    ''' Player の生成クラス '''

    player_dict = {
        1: Random,
        2: Human,
        3: MyTestPlayer1,
        4: Developer,
        5: Kaito1,
        6: Kaito2}

    def create_player(player_num):
        print(f'player{player_num}を選択してください')
        for num, player in PlayerFactory.player_dict.items():
            print('  ', num, ':', player)
        selected_player = int(input((f'player{player_num}: ')))

        player_class = PlayerFactory.player_dict[selected_player]
        return player_class(player_num)
