from common import *
from field import Field
from virtualPlayer import VirtualPlayer

class Game:
    ''' numeron の実装クラス '''

    def __init__(self, virtual_player):
        self.player = virtual_player
        self.field = Field()
        self.turn = 0    # ターン数
        self.log = []   # ゲーム進行のログ
        self.winner = None
        self.double = False  # 攻撃アイテム double が使用されたとき True

    def play(self):
        ''' 1回ゲームを行う '''
        self.set_former_player()
        self.set_field()

        while True:
            self.turn += 1
            if USE_ITEMS and not self.double:
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
            if self.double:
                self.double = False
            if not self.double:
                self.switch()

    def set_former_player(self):
        self.player.set_former_player()

    def set_field(self):
        self.field.set_field(self.player)

    def guard(self):
        ''' 防御アイテムの使用 '''
        guard_item = self.player.select_guard()
        if guard_item != None:
            assert guard_item in GUARD_ITEMS
            assert guard_item in self.field.items[self.player.turn[self.player.player].player_num]
            self.field.items[self.player.turn[self.player.player].player_num].remove(guard_item)
            self.player.guard(guard_item)

    def attack(self):
        ''' 攻撃アイテムの使用 '''
        attack_item = self.player.select_attack()
        if attack_item != None:
            assert attack_item in ATTACK_ITEMS
            assert attack_item in self.field.items[self.player.player.player_num]
            self.field.items[self.player.player.player_num].remove(attack_item)
            self.player.attack(attack_item)
        if attack_item == 'double':
            self.double = True

    def call(self):
        ''' 数字のコール '''
        call_num = self.player.call()
        call_num = str(call_num).zfill(N)
        self.write_log(self.player, call_num)

    def write_log(self, player, call_num):
        ''' ログを記入する(player_num, call_num, eat, bite) '''
        eat, bite = 0, 0
        card = self.field.get_card(3-player.player.player_num)  # 相手のカード

        for i in range(len(card)):
            if call_num[i] in card:
                bite += card.count(call_num[i])
                if call_num[i] == card[i]:
                    eat += 1
                    bite -= 1

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
