from common import *
from player import Player

class TestPlayer1(Player):
    ''' テストプレイヤー(strでコールする) '''

    def set_card(self):
        return '07'

    def set_items(self):
        pass

    def call(self):
        return str(random.randint(0, 10**N-1))

    def end_process(self, winner):
        print('player1: end_process() is called')  # 開発用
        return

    def get_call(self, call_num):
        print('player1: get_call() is called.', f'call_num = {call_num}.')  # 開発用
        return

    def get_eat_bite(self, eat, bite):
        print('player1: get_eat_bite() is called.', f'eat = {eat}.', f'bite = {bite}.')  # 開発用
        return

class TestPlayer2(Player):
    ''' テストプレイヤー(intでコールする) '''

    def set_card(self):
        while True:
            card = random.randint(0, 10**N-1)
            if self.check_card(card):
                break

        # print(f'player2: set {card}')   # 開発用

        return card

    def set_items(self):
        pass

    def call(self):
        return random.randint(0, 10**N-1)

    def end_process(self, winner):
        # print('player2: end_process() is called')  # 開発用
        return

    def get_call(self, call_num):
        # print('player2: get_call() is called.', f'call_num = {call_num}.')  # 開発用
        return

    def get_eat_bite(self, eat, bite):
        # print('player2: get_eat_bite() is called.', f'eat = {eat}.', f'bite = {bite}.')  # 開発用
        return
