from player import Player
from testPlayers import *
from myTestPlayers import *

class PlayerFactory:
    ''' Player の生成クラス '''

    player_dict = {
        'A': TestPlayer1,
        'B': TestPlayer2,
        'C': MyTestPlayer1}

    def create_player(player_num):
        print(f'player{player_num}を選択してください')
        print(PlayerFactory.player_dict)
        selected_player = input((f'player{player_num}: '))

        player_class = PlayerFactory.player_dict[selected_player]
        return player_class(player_num)
