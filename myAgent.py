from common import *
from player import Player

class MyAgent(Player):
    ''' Agent '''
    def __init__(self, player_num):
        super().__init__(player_num)

    def set_card(self):
        # print('Random: set_card() is called')   # 開発用
        while True:
            card = str(random.randint(0, 10**N-1)).zfill(N)
            if self.check_card(card):
                break
        print(f'{self.__class__.__name__}{self.player_num}: set {card}')   # 開発用
        return card

    def call(self):
        while True:
            call_num = random.randint(0, 10**N-1)
            if self.check_card(call_num):
                break
        return call_num

    def end_process(self, winner, cards_record):
        # print('Random: end_process() is called')  # 開発用
        return

    def get_log(self, log):
        print(f'{self.__class__.__name__}{self.player_num}: get_log() is called.', f'log = {log}.')  # 開発用
        return

