from common import *
from player import Player

class Random(Player):
    ''' テストプレイヤー '''

    def set_card(self):
        print('Random: set_card() is called')   # 開発用
        while True:
            card = str(random.randint(0, 10**N-1)).zfill(N)
            if self.check_card(card):
                break
        print(f'Random: set {card}')   # 開発用
        return card

    def set_items(self):
        print('Random: set_items() is called')  # 開発用
        while True:
            items = random.sample(ITEMS, NUM_ITEMS)
            if self.check_items(items):
                break
        print(f'Random: set {items}')   # 開発用
        return items

    def call(self):
        return random.randint(0, 10**N-1)

    def end_process(self, winner):
        print('Random: end_process() is called')  # 開発用
        return

    def get_call(self, call_num):
        print('Random: get_call() is called.', f'call_num = {call_num}.')  # 開発用
        return

    def get_eat_bite(self, eat, bite):
        print('Random: get_eat_bite() is called.', f'eat = {eat}.', f'bite = {bite}.')  # 開発用
        return

class Human(Player):
    ''' 手動プレイヤー '''

    def set_items(self):
        while True:
            print('\nアイテムをセットしてください')
            items = input().split()
            print(items)
            if self.check_items(items):
                break
        return items

    def set_card(self):
        while True:
            print('\n数字をセットしてください')
            card = input('card: ')
            if self.check_card(card):
                break
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
            if '0'.zfill(N) <= call_num <= str(10**N-1).zfill(N):
                break
        return call_num

    def end_process(self, winner):
        pass

    def get_call(self, call_num):
        print(f'\n相手のコールは {call_num} です')

    def get_eat_bite(self, eat, bite):
        print(f'\n{eat}eat {bite}bite です')
