from common import *
from virtualPlayer import VirtualPlayer

class Game:
    ''' numeron の実装クラス '''

    def __init__(self, virtual_player):
        self.player = virtual_player
        self.turn = 0    # ターン数
        self.log = []   # ゲーム進行のログ
        self.winner = None
        self.double_flg = 0  # 攻撃アイテム double が使用されたときのフラグ

    def play(self):
        ''' 1回ゲームを行う '''
        self.set_former_player()
        self.set_field()

        while True:
            self.turn += 1
            if USE_ITEMS and self.double_flg == 0:
                guard = self.guard()
                if guard:
                    self.tell_log()
                attack = self.attack()
                if attack:
                    self.tell_log()
            self.call()
            self.tell_log()
            if self.ended():
                self.set_winner()
                self.tell_result()
                break

            # 攻撃アイテム double についての特別処理
            self.double_flg = max(0, self.double_flg - 1)
            if self.double_flg == 0:
                self.switch()

    def set_former_player(self):
        self.player.set_former_player()

    def set_field(self):
        self.player.set_field()

    def guard(self):
        ''' 防御アイテムの使用 '''
        guard_item = self.player.guard()
        if guard_item == None:
            return False
        else:
            self.write_log(self.player, guard_item)
            return True

    def attack(self):
        ''' 攻撃アイテムの使用 '''
        attack_item = self.player.attack()
        if attack_item == None:
            return False
        else:
            if attack_item == 'double':
                self.double_flg = 2
            self.write_log(self.player, attack_item)
            return True

    def call(self):
        ''' 数字のコール '''
        call_num = self.player.call()
        call_num = str(call_num).zfill(N)
        self.write_log(self.player, call_num)

    def write_log(self, player, call_num_or_item):
        ''' ログを記入する
            コールの場合 (player_num, 'call', call_num, eat, bite)
            アイテム(high_and_low 以外)の場合 (player_num, 'item', item)
            high_and_low の場合 (player_num, 'item', item, high_and_low) '''
        if call_num_or_item in ITEMS:
            item = call_num_or_item
            if item in GUARD_ITEMS:
                player_num = self.player.opponent().player_num
            elif item in ATTACK_ITEMS:
                player_num = self.player.player.player_num
                if item == 'high_and_low':
                    high_and_low = self.get_high_and_low(self.player.opponent().player_num)
                    self.log.append([player_num, 'item', item, high_and_low])
                    return
            self.log.append([player_num, 'item', item])
        else:
            call_num = call_num_or_item
            eat, bite = 0, 0
            card = self.player.get_card(player.opponent().player_num)  # 相手のカード

            for i in range(len(card)):
                if card[i] == call_num[i]:
                    eat += 1
                elif call_num[i] in card:
                    bite += 1

            self.log.append([player.player.player_num, 'call', call_num, eat, bite])

    def get_high_and_low(self, player_num):
        return self.player.get_high_and_low(player_num)

    def tell_log(self):
        ''' playerに log を伝える '''
        log = self.log[-1]
        self.player.tell_log(log)

    def ended(self):
        ''' ゲームが終了したかどうかの判定 '''
        eat = self.log[-1][3]
        return eat == N

    def set_winner(self):
        self.winner = self.log[-1][0]

    def get_winner(self):
        return self.winner

    def tell_result(self):
        ''' 各playerにゲームの結果を伝える '''
        self.player.end_process(self.winner)

    def switch(self):
        ''' 手番の交代 '''
        self.player.switch()
