from common import *
from playerFactory import PlayerFactory

class VirtualPlayer:
    ''' Class Game と Class Player の仲介クラス '''

    def __init__(self):
        self.player1 = PlayerFactory.create_player(1)
        self.player2 = PlayerFactory.create_player(2)
        self.player = None

    def opponent(self):
        ''' 相手プレイヤーのインスタンスを返す '''
        turn = {
            self.player1: self.player2,
            self.player2: self.player1}
        return turn[self.player]

    def set_former_player(self):
        ''' ランダムに先攻を決める '''
        if random.randint(0, 1) == 0:
            self.player = self.player1
        else:
            self.player = self.player2

    def switch(self):
        ''' 手番の交代 '''
        self.player = self.opponent()

    def set_card(self):
        ''' 数字をセットする '''
        return self.player.set_card()

    def set_items(self):
        ''' アイテムをセットする '''
        return self.player.set_items()

    def select_guard(self):
        ''' 使用する防御アイテムの選択 '''
        return self.opponent().select_guard()

    def guard(self, guard_item):
        ''' 防御アイテムの使用 '''
        if guard_item == 'slash':
            self.opponent().slash()
        elif guard_item == 'shuffle':
            self.opponent().shuffle()
        elif guard_item == 'change':
            self.opponent().change()

    def select_attack(self):
        ''' 使用する攻撃アイテムの選択 '''
        return self.player.select_attack()

    def attack(self, attack_item):
        ''' 攻撃アイテムの使用 '''
        if attack_item == 'double':
            self.player.double()
        elif attack_item == 'high_and_low':
            self.player.high_and_low()
        elif attack_item == 'target':
            self.player.target()

    def call(self):
        ''' 数字をコールする '''
        call_num = self.player.call()
        self.player.assert_call(call_num)
        return call_num

    def end_process(self, winner):
        for i in range(2):
            self.player.end_process(winner)
            self.switch()

    def tell_call(self, call_num):
        self.opponent().get_call(call_num)

    def tell_eat_bite(self, eat, bite):
        self.player.get_eat_bite(eat, bite)
