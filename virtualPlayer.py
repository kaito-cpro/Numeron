from common import *
from field import Field
from playerFactory import PlayerFactory

class VirtualPlayer:
    ''' Class Game と Class Player の仲介クラス '''

    def __init__(self):
        self.field = Field()
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

    def set_field(self):
        ''' アイテムとカードをセットする '''
        if USE_ITEMS:
            for i in range(2):
                items = self.player.set_items()
                self.field.set_items(self.player.player_num, items)
                self.switch()
        for i in range(2):
            card = str(self.player.set_card()).zfill(N)
            self.field.set_card(self.player.player_num, card)
            self.switch()

    def switch(self):
        ''' 手番の交代 '''
        self.player = self.opponent()

    def set_card(self):
        ''' 数字をセットする '''
        return self.player.set_card()

    def set_items(self):
        ''' アイテムをセットする '''
        return self.player.set_items()

    def guard(self):
        ''' 防御アイテムの使用 '''
        guard_item = self.opponent().select_guard()
        if guard_item == None:
            return None
        assert guard_item in GUARD_ITEMS
        self.field.assert_item(guard_item, self.opponent().player_num)

        if guard_item == 'shuffle':
            new_card = self.opponent().shuffle()
            assert sorted(new_card) == sorted(self.field.get_card(self.opponent().player_num))
            self.field.set_card(self.opponent().player_num, new_card)
        elif guard_item == 'change':
            self.opponent().change()

        self.field.remove_item(guard_item, self.opponent().player_num)
        return guard_item

    def attack(self):
        ''' 攻撃アイテムの使用 '''
        attack_item = self.player.select_attack()
        if attack_item == None:
            return None
        assert attack_item in ATTACK_ITEMS
        self.field.assert_item(attack_item, self.player.player_num)

        if attack_item == 'double':
            pass    # これで実装できている
        elif attack_item == 'high_and_low':
            self.player.high_and_low()
        elif attack_item == 'target':
            self.player.target()
        elif guard_item == 'slash':
            self.player.slash()

        self.field.remove_item(attack_item, self.player.player_num)
        return attack_item

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

    def get_card(self, player_num):
        return self.field.get_card(player_num)
