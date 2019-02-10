from common import *
from field import Field
from virtualPlayer import VirtualPlayer

class Game:
    ''' numeron の実装クラス '''

    def __init__(self, virtual_player):
        self.player = virtual_player
        self.field = Field()
        self.log = []   # ゲーム進行のログ
        self.winner = None

    def play(self):
        ''' 1回ゲームを行う '''
        self.set_former_player()
        self.set_field()

        while True:
            if use_items:
                self.guard()
                self.attack()
            self.call()
            self.tell_call()
            self.tell_eat_bite()
            if self.ended():
                self.set_winner()
                self.tell_result()
                break
            self.switch()

    def set_former_player(self):
        self.player.set_former_player()

    def set_field(self):
        self.field.set_field(self.player)

    def guard(self):
        ''' 防御アイテムの使用 '''
        pass

    def attack(self):
        ''' 攻撃アイテムの使用 '''
        pass

    def call(self):
        ''' 数字のコール '''
        call_num = self.player.call()
        self.write_log(self.player, call_num)

    def write_log(self, player, call_num):
        ''' ログを記入する(player_num, call_num, eat, bite) '''
        eat, bite = 0, 0
        card = str(self.field.get_card(3-player.player.player_num))  # 相手のカード
        call_num = str(call_num)

        for i in range(len(card)):
            if call_num[i] == card[i]:
                eat += 1
            elif call_num[i] in card:
                bite += 1

        self.log.append([player.player.player_num, int(call_num), eat, bite])

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
