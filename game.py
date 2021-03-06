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

    def play(self, times):
        ''' times 回ゲームを行う '''
        self.set_former_player()
        self.set_items()

        won = {1: 0, 2: 0}  # times 回のゲームにおける各プレイヤーの勝数
        for i in range(times):
            self.set_card()
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
                    won[self.winner] += 1
                    if i < times - 1:
                        self.tell_result(tell_cards=False)
                    else:
                        self.tell_result(tell_cards=True)   # セットしていた数字を伝える
                    self.switch()
                    break

                # 攻撃アイテム double についての特別処理
                self.double_flg = max(0, self.double_flg - 1)
                if self.double_flg == 0:
                    self.switch()

        if won[1] > won[2]:
            self.winner = 1
        elif won[1] < won[2]:
            self.winner = 2
        else:
            self.winner = None

    def set_former_player(self):
        self.player.set_former_player()

    def set_items(self):
        if USE_ITEMS:
            items = self.player.set_items()
            self.write_log(self.player, items, 'set_items')

    def set_card(self):
        self.player.set_card()

    def guard(self):
        ''' 防御アイテムの使用 '''
        guard_item, option = self.player.guard()
        if guard_item == None:
            return False
        else:
            self.write_log(self.player, guard_item, option)
            return True

    def attack(self):
        ''' 攻撃アイテムの使用 '''
        attack_item, option = self.player.attack()
        if attack_item == None:
            return False
        else:
            if attack_item == 'double':
                self.double_flg = 2
            self.write_log(self.player, attack_item, option)
            return True

    def call(self):
        ''' 数字のコール '''
        try:
            call_num = self.player.call()
        except:
            print('time out')
            return
        call_num = str(call_num).zfill(N)
        self.write_log(self.player, call_num)

    def write_log(self, player, call_num_or_item, option=None):
        ''' ログを記入する
            アイテムのセットの場合 (player_num, 'set_items', items); items は配列
            コールの場合 (player_num, 'call', call_num, eat, bite); call_num はコールした数字(str). eat, bite は int
            change の場合 (player_num, 'item', 'change', digit, high_and_low); digit は取り替えた桁(int)で high_and_low はその桁の High&Low. High ならば True
            high_and_low の場合 (player_num, 'item', 'high_and_low', high_and_low); high_and_low は True/False のサイズ N の配列
            slash の場合 (player_num, 'item', 'slash', slash); slash はスラッシュナンバー(int)
            target の場合 (player_num, 'item', 'target', target_num, target); target_num はターゲットナンバー(str) で target はターゲットナンバーが含まれるならばその桁, 含まれないならば None
            それ以外のアイテムの場合 (player_num, 'item', item)
             '''
        if option == 'set_items':
            items = call_num_or_item
            self.log.append([self.player.player.player_num, 'set_items', list(items[0])])
            self.tell_log()
            self.log.append([self.player.opponent().player_num, 'set_items', list(items[1])])
            self.tell_log()
        elif call_num_or_item in ITEMS:
            item = call_num_or_item
            if item in GUARD_ITEMS:
                player_num = self.player.opponent().player_num
                if item == 'change':
                    digit, high_and_low = option
                    self.log.append([player_num, 'item', item, digit, high_and_low])
                    return
            elif item in ATTACK_ITEMS:
                player_num = self.player.player.player_num
                if item == 'high_and_low':
                    high_and_low = option
                    self.log.append([player_num, 'item', item, high_and_low])
                    return
                elif item == 'slash':
                    slash = option
                    self.log.append([player_num, 'item', item, slash])
                    return
                elif item == 'target':
                    target_num, target = option
                    self.log.append([player_num, 'item', item, target_num, target])
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

    def tell_result(self, tell_cards=False):
        ''' 各playerにゲームの結果を伝える '''
        if tell_cards:
            self.player.end_process(self.winner, tell_cards=True)
        else:
            self.player.end_process(self.winner, tell_cards=False)

    def show_log(self):
        print('log:')
        for log in self.log:
            print(log)

    def switch(self):
        ''' 手番の交代 '''
        self.player.switch()
