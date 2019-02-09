from player import Player
from hogePlayers import *

class PlayerFactory:
    ''' Player の生成クラス '''

    player_dict = {
        'A': Hoge1,
        'B': Hoge2}

    def create_player(player_num):
        print(f'player{player_num}を選択してください')
        print(PlayerFactory.player_dict)
        selected_player = input((f'player{player_num}: '))

        player_class = PlayerFactory.player_dict[selected_player]
        return player_class()
