from common import *
from field import Field
from virtualPlayer import VirtualPlayer

class Game:
    ''' numeron の実装クラス '''

    def __init__(self, virtual_player):
        self.player = virtual_player
        self.field = Field()
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
        pass

    def ended(self):
        ''' ゲームが終了したかどうかの判定 '''
        pass

    def set_winner(self):
        pass

    def get_winner(self):
        return self.winner

    def tell_result(self):
        ''' 各playerにゲームの結果を伝える '''
        self.player.end_process(self.winner)

    def switch(self):
        ''' 手番の交代 '''
        pass
