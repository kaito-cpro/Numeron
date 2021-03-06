from common import *

class Player:
    ''' Player の実装クラス(抽象インターフェース) '''

    def __init__(self, player_num):
        self.player_num = player_num

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
        if BATTLE_TYPE == 'AI_vs_AI':
            return ['shuffle', 'high_and_low', 'slash']

    def set_card(self):
        ''' 数字をセットする
            返り値の型は int, str のいずれでもよい(だが str を積極的に使用せよ) '''
        pass

    def select_guard(self):
        ''' 使用する防御アイテムの選択 '''
        pass

    def shuffle(self):
        pass

    def change(self):
        pass

    def select_attack(self):
        ''' 使用する攻撃アイテムの選択 '''
        pass

    def target(self):
        pass

    def call(self):
        ''' 数字をコールする
            返り値の型は int, str のいずれでもよい '''
        pass

    def end_process(self, winner, cards_record):
        ''' ゲーム終了時の処理 '''
        pass

    def get_log(self, log):
        ''' 何かアクションがあったときに log を環境から受け取る '''
        pass

    def assert_call(self, call_num):
        ''' コールした数字が不適切な場合に警告する '''
        assert self.check_card(call_num)
