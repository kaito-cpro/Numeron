from common import *
from virtualPlayer import VirtualPlayer

class Field:
    ''' カードとアイテムの実装クラス '''

    def __init__(self):
        self.card = {1: None, 2: None}
        self.items = {1: None, 2: None}

    def set_field(self, player):
        for i in range(2):
            self.set_card(player.player)
            if use_items:
                self.set_items(player.player)
            player.switch()

    def set_card(self, player):
        ''' 数字をセットする '''
        card = str(player.set_card()).zfill(N)

        # 数字の整合性をチェック
        flg = True
        if not '0'.zfill(N) <= card <= str(10**N-1).zfill(N):
            flg = False
        for i in range(len(card)):
            if card.count(card[i]) > 1:
                flg = False
        assert flg

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
