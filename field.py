from common import *
from virtualPlayer import VirtualPlayer

class Field:
    ''' カードとアイテムの実装クラス '''

    def __init__(self):
        self.card = {1: [], 2: []}
        self.items = {1: [], 2: []}

    def set_field(self, player):
        for i in range(2):
            self.set_card(player.player)
            if use_items:
                self.set_items(player.player)
            player.switch()

    def set_card(self, player):
        ''' 数字をセットする '''
        card = player.set_card()
        # assert
        self.card[player.player_num] = card

    def set_items(self, player):
        ''' アイテムをセットする '''
        items = player.set_items()
        # assert
        self.items[player.player_num] = items

    def get_card(self, player_num):
        return self.card[player_num]

    def get_items(self, player_num):
        return self.items[player_num]
