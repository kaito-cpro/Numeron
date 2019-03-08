from common import *

class Field:
    ''' カードとアイテムの実装クラス '''

    def __init__(self):
        self.card = {1: None, 2: None}
        self.items = {1: [], 2: []}

    def set_items(self, player_num, items):
        ''' アイテムをセットする '''
        assert self.check_items(items)
        self.items[player_num] = items

    def check_items(self, items):
        ''' アイテムが適切かどうかの判定 '''
        if BATTLE_TYPE == 'AI_vs_AI':
            return set(items) == set(['shuffle', 'high_and_low', 'slash'])

        flg = True
        num_cnt = []
        for item in ITEMS:
            num_cnt.append(items.count(item))

        if len(items) != NUM_ITEMS:
            flg = False
        if sum(num_cnt) != NUM_ITEMS:
            flg = False
        for cnt in num_cnt:
            if not cnt <= 1:
                flg = False
        if 'high_and_low' in items and 'slash' in items:
            flg = False

        return flg

    def set_card(self, player_num, card):
        ''' 数字をセットする '''
        assert self.check_card(card)
        self.card[player_num] = card

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

    def assert_item(self, item, player_num):
        ''' アイテムが所持アイテムリストに入っていない場合に警告する '''
        assert item in self.items[player_num]

    def remove_item(self, item, player_num):
        ''' アイテムを所持アイテムリストから取り除く '''
        self.items[player_num].remove(item)
