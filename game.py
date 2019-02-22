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
                self.guard()
                self.attack()
            self.call()
            # print('call: ', self.log[-1])  # 開発用
            self.tell_call()
            self.tell_eat_bite()
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
        self.write_log(self.player, guard_item)

    def attack(self):
        ''' 攻撃アイテムの使用 '''
        attack_item = self.player.attack()
        if attack_item == 'double':
            self.double_flg = 2
        self.write_log(self.player, attack_item)

    def call(self):
        ''' 数字のコール '''
        call_num = self.player.call()
        call_num = str(call_num).zfill(N)
        self.write_log(self.player, call_num)

    def write_log(self, player, call_num_or_item):
        ''' ログを記入する
            コールの場合 (player_num, call_num, eat, bite)
            アイテムの場合 (player_num, item) '''
        if call_num_or_item == None:
            return
        elif call_num_or_item in ITEMS:
            item = call_num_or_item
            if item in GUARD_ITEMS:
                player_num = self.player.opponent().player_num
            elif item in ATTACK_ITEMS:
                player_num = self.player.player.player_num
            self.log.append([player_num, item])
        else:
            call_num = call_num_or_item
            eat, bite = 0, 0
            card = self.player.get_card(player.opponent().player_num)  # 相手のカード

            for i in range(len(card)):
                if card[i] == call_num[i]:
                    eat += 1
                elif call_num[i] in card:
                    bite += 1

            self.log.append([player.player.player_num, call_num, eat, bite])

    def tell_call(self):
        ''' callされたplayerに call を伝える '''
        call_num = self.log[-1][1]
        self.player.tell_call(call_num)

    def tell_eat_bite(self):
        ''' callしたplayerに Eat/Bite を伝える '''
        eat, bite = self.log[-1][2:4]
        self.player.tell_eat_bite(eat, bite)

    def ended(self):
        ''' ゲームが終了したかどうかの判定 '''
        eat = self.log[-1][2]
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
