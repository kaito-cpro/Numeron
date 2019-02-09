from common import *
from playerFactory import PlayerFactory

class VirtualPlayer:
    ''' Class Game と Class Player の仲介クラス '''

    def __init__(self):
        self.player1 = PlayerFactory.create_player(1)
        self.player2 = PlayerFactory.create_player(2)

        self.player = None

        self.turn = {
            self.player1: self.player2,
            self.player2: self.player1}

    def set_former_player(self):
        ''' ランダムに先攻を決める '''
        if random.randint(0, 1) == 0:
            self.player = self.player1
        else:
            self.player = self.player2

    def switch(self):
        ''' 手番の交代 '''
        self.player = self.turn[self.player]

    def set_card(self):
        ''' 数字をセットする '''
        return self.player.receive('set_card')

    def set_items(self):
        ''' アイテムをセットする '''
        return self.player.receive('set_items')

    def end_process(self, winner):
        for i in range(2):
            self.player.receive('end_process', winner)
            self.switch()
