from common import *
from field import Field
from playerFactory import PlayerFactory
from timeout import timeout

class VirtualPlayer:
    ''' Class Game と Class Player の仲介クラス '''

    def __init__(self):
        self.field = Field()
        self.player1 = PlayerFactory.create_player(1)
        self.player2 = PlayerFactory.create_player(2)
        self.player = None
        self.cards_record = []  # 各プレイヤーがセットした数字の記録

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

    def set_items(self):
        ''' アイテムをセットする '''
        res = []
        for i in range(2):
            items = self.player.set_items()
            self.field.set_items(self.player.player_num, items)
            res.append(items)
            self.switch()
        return res

    def set_card(self):
        ''' カードをセットする '''
        for i in range(2):
            card = str(self.player.set_card()).zfill(N)
            self.field.set_card(self.player.player_num, card)
            self.cards_record.append([self.player.player_num, 'set_card', card])
            self.switch()

    def switch(self):
        ''' 手番の交代 '''
        self.player = self.opponent()

    def guard(self):
        ''' 防御アイテムの使用 '''
        guard_item = self.opponent().select_guard()
        option = None

        if guard_item == None:
            return [None, option]
        assert guard_item in GUARD_ITEMS
        self.field.assert_item(guard_item, self.opponent().player_num)

        if guard_item == 'shuffle':
            new_card = self.opponent().shuffle()
            assert sorted(new_card) == sorted(self.field.get_card(self.opponent().player_num))
            self.field.set_card(self.opponent().player_num, new_card)
        elif guard_item == 'change':
            digit, new_num = self.opponent().change()   # 桁と数字
            card = self.field.get_card(self.opponent().player_num)
            assert 1 <= digit <= N
            assert '0' <= new_num <= '9'
            assert (card[N-1] >= '5') == (new_num >= '5')   # 取り替える数字は high か low かが一致している必要がある
            option = [digit, (card[N-1]>='5')]
            card = list(card)
            card[N-digit] = new_num
            card = ''.join(card)
            self.field.set_card(self.opponent().player_num, card)

        self.field.remove_item(guard_item, self.opponent().player_num)
        return guard_item, option

    def attack(self):
        ''' 攻撃アイテムの使用 '''
        attack_item = self.player.select_attack()
        option = None   # アイテムごとに異なるオプションを返す

        if attack_item == None:
            return [None, option]
        assert attack_item in ATTACK_ITEMS
        self.field.assert_item(attack_item, self.player.player_num)

        if attack_item == 'double':
            pass    # これで実装できている
        elif attack_item == 'high_and_low':
            option = self.get_high_and_low(self.opponent().player_num)
        elif attack_item == 'target':
            target_num = self.player.target()
            assert '0' <= target_num <= '9'
            option = [target_num, self.get_target(self.opponent().player_num, target_num)]
        elif attack_item == 'slash':
            option = self.get_slash(self.opponent().player_num)

        self.field.remove_item(attack_item, self.player.player_num)
        return attack_item, option

    def get_high_and_low(self, player_num):
        card = list(self.field.get_card(player_num))
        card = np.array(card)
        high_and_low = (card>='5')
        return list(high_and_low)

    def get_slash(self, player_num):
        card = list(self.field.get_card(player_num))
        slash = int(max(card)) - int(min(card))
        return slash

    def get_target(self, player_num, target_num):
        card = self.field.get_card(player_num)
        if target_num in card:
            return N - card.index(target_num)   # target_num が card の i 桁目であるときの i の値(一の位を1桁目とする)
        else:
            return None

    @timeout(TIMEOUT_SEC)
    def call(self):
        ''' 数字をコールする '''
        call_num = self.player.call()
        self.player.assert_call(call_num)
        return call_num

    def end_process(self, winner, tell_cards=False):
        for i in range(2):
            if tell_cards:
                self.player.end_process(winner, self.cards_record)
                self.cards_record = []
            else:
                self.player.end_process(winner, None)
            self.switch()

    def tell_log(self, log):
        for i in range(2):
            self.player.get_log(log)
            self.switch()

    def get_card(self, player_num):
        return self.field.get_card(player_num)
