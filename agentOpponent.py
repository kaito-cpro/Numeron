from common import *
from player import Player
import itertools

class Opponent(Player):
    ''' 相手の仮想エージェント '''

    def __init__(self, player_num):
        self.player_num = player_num
        self.times = 1  # 現在のゲームの回数
        self.turn = 0  # 各ゲームにおける(自分の)ターン
        self.card = None
        self.log = []  # 各セットにおけるログ
        self.valid_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]  # コールやセットが可能な数字(720通り)
        self.candidate_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]  # 相手の数字としてあり得る候補
        self.call_list = []  # コール済の数字
        self.first_call_eat_bite = []
        self.mode = None  # プレイスタイルのモード
        self.guard_items = ['shuffle']
        self.attack_items = ['high_and_low', 'slash']

    def initialize(self):
        ''' メンバ変数の初期化 '''
        self.candidate_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]
        self.call_list = []
        if self.times % 3 == 0:
            self.card = None
            self.log = []
            self.guard_items = ['shuffle']
            self.attack_items = ['high_and_low', 'slash']
        self.turn = 0
        self.times += 1

    def get_candidate_list(self):
        return self.candidate_list

    def get_log(self, log):
        player_num, protocol_type = log[0], log[1]
        if player_num == self.player_num and protocol_type == 'call':
            call, eat, bite = log[2], log[3], log[4]
            for num in self.candidate_list[:]:
                if not self.fill_eat_bite(num, call, eat, bite):
                    self.candidate_list.remove(num)
            self.first_call_eat_bite = [call, eat, bite]
        elif player_num == self.player_num and protocol_type == 'item':
            item = log[2]
            if item == 'high_and_low':
                high_and_low = log[3]
                for num in self.candidate_list[:]:
                    if not self.fill_high_and_low(num, high_and_low):
                        self.candidate_list.remove(num)
            elif item == 'slash':
                slash = log[3]
                for num in self.candidate_list[:]:
                    if not self.fill_slash(num, slash):
                        self.candidate_list.remove(num)
        elif player_num != self.player_num and protocol_type == 'item':
            item = log[2]
            if item == 'shuffle':
                new_candidate_list = set()
                for num in self.candidate_list:
                    for n in itertools.permutations(num):
                        new_candidate_list.add(''.join(n))
                self.candidate_list = list(new_candidate_list)

    def end_process(self, winner, cards_record):
        self.initialize()

    def calc_eat_bite(self, num1, num2):
        num1 = str(num1).zfill(N)
        num2 = str(num2).zfill(N)
        eat, bite = 0, 0
        for i in range(len(num1)):
            if num1[i] == num2[i]:
                eat += 1
            elif num1[i] in num2:
                bite += 1
        return eat, bite

    def fill_eat_bite(self, num1, num2, eat, bite):
        return list(self.calc_eat_bite(num1, num2)) == [eat, bite]

    def fill_high_and_low(self, num, high_and_low):
        flg = True
        for i in range(N):
            if (high_and_low[i]==True and num[i]<'5') or (high_and_low[i]==False and num[i]>='5'):
                flg = False
        return flg

    def fill_slash(self, num, slash):
        return slash == int(max(num)) - int(min(num))
