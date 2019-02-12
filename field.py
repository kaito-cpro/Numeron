from common import *
from virtualPlayer import VirtualPlayer

class Field:
    ''' カードとアイテムの実装クラス '''

    def __init__(self):
        self.card = {1: None, 2: None}
        self.items = {1: [], 2: []}

    def set_field(self, player):
        if USE_ITEMS:
            for i in range(2):
                self.set_items(player.player)
                player.switch()
        for i in range(2):
            self.set_card(player.player)
            player.switch()

    def set_items(self, player):
        ''' アイテムをセットする '''
        items = player.set_items()
        assert self.check_items(items)
        self.items[player.player_num] = items

    def check_items(self, items):
        ''' アイテムが適切かどうかの判定 '''
        flg = True
        num_cnt = []

        if len(items) != NUM_ITEMS:
            flg = False

        num_cnt.append(items.count('double'))
        num_cnt.append(items.count('high_and_low'))
        num_cnt.append(items.count('target'))
        num_cnt.append(items.count('slash'))
        num_cnt.append(items.count('shuffle'))
        num_cnt.append(items.count('change'))

        if sum(num_cnt) != NUM_ITEMS:
            flg = False
        for cnt in num_cnt:
            if not cnt <= 1:
                flg = False
        if 'high_and_low' in items and 'slash' in items:
            flg = False

        return flg

    def set_card(self, player):
        ''' 数字をセットする '''
        card = str(player.set_card()).zfill(N)
        assert self.check_card(card)
        self.card[player.player_num] = card

    def check_card(self, card):
        ''' card の数字が適切かどうかの判定 '''
        card = str(card).zfill(N)
        flg = True

        if not '0'.zfill(N) <= card <= str(10**N-1).zfill(N):
            flg = False
        for i in range(len(card)):
            if card.count(card[i]) > 1:
                flg = False

        return flg

    def get_card(self, player_num):
        return self.card[player_num]

    def get_items(self, player_num):
        return self.items[player_num]
