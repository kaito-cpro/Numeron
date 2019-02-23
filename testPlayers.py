from common import *
from player import Player

class Random(Player):
    ''' テストプレイヤー '''

    def set_card(self):
        # print('Random: set_card() is called')   # 開発用
        while True:
            card = str(random.randint(0, 10**N-1)).zfill(N)
            if self.check_card(card):
                break
        print(f'Random: set {card}')   # 開発用
        return card

    def set_items(self):
        # print('Random: set_items() is called')  # 開発用
        while True:
            items = random.sample(ITEMS, NUM_ITEMS)
            if self.check_items(items):
                break
        # print(f'Random: set {items}')   # 開発用
        return items

    def call(self):
        while True:
            call_num = random.randint(0, 10**N-1)
            if self.check_card(call_num):
                break
        return call_num

    def end_process(self, winner):
        # print('Random: end_process() is called')  # 開発用
        return

    def get_log(self, log):
        # print('Random: get_log() is called.', f'log = {log}.')  # 開発用
        return

class Human(Player):
    ''' 手動プレイヤー '''

    def __init__(self, player_num):
        self.player_num = player_num
        self.items = None
        self.card = None

    def set_items(self):
        while True:
            print('\nアイテムをセットしてください')
            items = input().split()
            if self.check_items(items):
                break
        self.items = items
        return items

    def set_card(self):
        while True:
            print('\n数字をセットしてください')
            card = input('card: ')
            if self.check_card(card):
                break
        self.card = card
        return card

    def select_guard(self):
        print('\n防御アイテムを選択してください')
        guard_item = input()
        if guard_item == 'None':
            guard_item = None
        return guard_item

    def select_attack(self):
        print('\n攻撃アイテムを選択してください')
        attack_item = input()
        if attack_item == 'None':
            attack_item = None
        return attack_item

    def call(self):
        while True:
            print('\nコールしてください')
            call_num = input('your call: ')
            if self.check_card(call_num):
                break
        return call_num

    def shuffle(self):
        while True:
            print('\nシャッフルしてください')
            new_card = input('new number: ')
            if sorted(new_card) == sorted(self.card):
                break
        return new_card

    def target(self):
        while True:
            print('\nターゲットナンバーを入力してください')
            target_num = input('target number: ')
            if '0' <= target_num <= '9':
                break
        return target_num

    def change(self):
        while True:
            print('\nチェンジする桁を入力してください')
            digit = int(input('digit: '))
            if not (0 <= digit <= N):
                continue
            print('チェンジする新たな数字を入力してください')
            new_num = input('new_num: ')
            if '0' <= new_num <= '9':
                break
        return digit, new_num

    def end_process(self, winner):
        pass

    def get_log(self, log):
        print(f'\nログ受信: {log}')
