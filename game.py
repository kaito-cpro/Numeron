from field import Field
from virtualPlayer import VirtualPlayer

class Game:
    ''' numeron の実装クラス '''

    def __init__(self):
        self.field = Field()
        self.player = VirtualPlayer()
        self.winner = None

    def play(self):
        ''' 1回ゲームを行う '''
        while True:
            self.guard()
            self.attack()
            self.call()
            if self.ended():
                self.set_winner()
                break
            self.switch()

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

    def switch(self):
        ''' 手番の交代 '''
        pass
