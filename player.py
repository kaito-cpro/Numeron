from common import *

class Player:
    ''' Player の実装クラス(抽象インターフェース) '''

    def __init__(self, player_num):
        self.player_num = player_num

    def check_items(self, items):
        ''' アイテムが適切かどうかの判定 '''
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

    def set_items(self):
        ''' アイテムをセットする '''
        pass

    def set_card(self):
        ''' 数字をセットする
            返り値の型は int, str のいずれでもよい '''
        pass

    def select_guard(self):
        ''' 使用する防御アイテムの選択 '''
        pass

    def slash(self):
        pass

    def shuffle(self):
        pass

    def change(self):
        pass

    def select_attack(self):
        ''' 使用する攻撃アイテムの選択 '''
        pass

    def double(self):
        pass

    def high_and_low(self):
        pass

    def target(self):
        pass

    def call(self):
        ''' 数字をコールする
            返り値の型は int, str のいずれでもよい '''
        pass

    def end_process(self, winner):
        ''' ゲーム終了時の処理 '''
        pass

    def get_call(self, call_num):
        ''' 相手の call を環境から受け取る
            call_num の型は str '''
        pass

    def get_eat_bite(self, eat, bite):
        ''' Eat/Bite を環境から受け取る '''
        pass
