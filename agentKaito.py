from common import *
from player import Player
import itertools

class Kaito1(Player):
    ''' Kaito の agent 1'''

    def __init__(self, player_num):
        self.player_num = player_num
        self.times = 1  # 現在のゲームの回数
        self.turn = 0  # 各ゲームにおける(自分の)ターン
        self.log = []  # 各セットにおけるログ
        self.valid_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]  # コールやセットが可能な数字(720通り)
        self.candidate_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]  # 相手の数字としてあり得る候補
        self.call_list = []  # コール済の数字
        self.first_call_eat_bite = []
        self.mode = None  # プレイスタイルのモード

    def set_card(self):
        return '810'

    def select_guard(self):
        return None

    def select_attack(self):
        return None

    def shuffle(self):
        pass

    def call(self):
        self.turn += 1
        if self.turn == 1:
            call = self.call_mini_max(1)
        elif self.turn == 2:
            first_call, first_eat, first_bite = self.first_call_eat_bite
            call = self.call_mini_max(2, first_call, first_eat, first_bite)
        else:
            call = self.call_expect()
        self.call_list.append(call)
        print(f'Kaito1 candidate: {len(self.candidate_list)}')
        print(f'Kaito1 call: {call}')
        return call

    def call_mini_max(self, turn, first_call=None, eat=None, bite=None):
        ''' ミニマックス法に従って O(1) でコールを返す '''
        if turn == 1:
            while True:
                call = str(random.randint(0, 10**N-1)).zfill(N)
                if self.check_card(call):
                    break
        elif turn == 2:
            unused_num = [str(num) for num in range(10) if str(num) not in first_call]  # first_call で使わなかった数字
            replace_idx = {}  # call から first_call へのインデックスの置換
            add_num = []  # 置換が恒等であるインデックスに入れる数字
            if eat == 2 and bite == 0:
                rnd = random.sample(range(0, 3), 3)
                replace_idx[rnd[0]] = rnd[0]
                replace_idx[rnd[1]] = rnd[2]
                add_num = [random.choice(unused_num)]
            elif eat == 1 and bite == 2:
                rnd = random.sample(range(0, 3), 3)
                replace_idx[0] = rnd[0]
                replace_idx[1] = rnd[2]
                replace_idx[2] = rnd[1]
            elif eat == 1 and bite == 1:
                rnd = random.randint(0, 2)
                replace_idx[rnd] = rnd
                add_num = random.sample(unused_num, 2)
            elif eat == 1 and bite == 0:
                rnd = random.sample(range(0, 3), 3)
                replace_idx[rnd[0]] = rnd[0]
                replace_idx[rnd[1]] = rnd[2]
                add_num = [random.choice(unused_num)]
            elif eat == 0 and bite == 3:
                rnd = random.sample(range(0, 3), 3)
                replace_idx[rnd[0]] = rnd[1]
                replace_idx[rnd[1]] = rnd[2]
                replace_idx[rnd[2]] = rnd[0]
            elif eat == 0 and bite == 2:
                rnd = random.choice([0, 2])
                if rnd == 0:
                    replace_idx[1] = 0
                    replace_idx[2] = 1
                else:
                    replace_idx[0] = 1
                    replace_idx[1] = 2
                add_num = [random.choice(unused_num)]
            elif eat == 0 and bite == 1:
                rnd = random.sample(range(0, 3), 2)
                replace_idx[rnd[0]] = rnd[1]
                replace_idx[rnd[1]] = rnd[0]
                add_num = [random.choice(unused_num)]
            elif eat == 0 and bite == 0:
                add_num = random.sample(unused_num, 3)
            call = ''
            for i in range(N):
                if i in replace_idx.keys():
                    call += first_call[replace_idx[i]]
                else:
                    call += add_num.pop(0)
        return call

    def call_expect(self):
        ''' 残る候補数の期待値を最小化するようなコールを返す '''
        call_candidate = []  # このターンでコールする数字の候補
        best_exp = float('inf')  # 期待値
        for call in self.candidate_list:
            call = str(call.zfill(N))
            if call in self.call_list:
                continue
            # 期待値の計算
            exp = 0
            for correct_num in self.candidate_list:
                #  self.candidate_list の中から相手の数字が correct_num であると仮定する
                for num in self.candidate_list:
                    if list(self.calc_eat_bite(correct_num, call)) == list(self.calc_eat_bite(num, call)):
                        exp += 1
                if exp < best_exp:
                    best_exp = exp
                    call_candidate = [call]
                elif exp == best_exp:
                    call_candidate.append(call)
        call_candidate2 = [call for call in call_candidate if call in self.candidate_list]  # call_candidate のうち self.candidate_list に属する数字
        call = random.choice(call_candidate2)
        return call

    def end_process(self, winner, cards_record):
        self.initialize()

    def get_log(self, log):
        player_num, protocol_type = log[0], log[1]
        if player_num == self.player_num and protocol_type == 'call':
            call, eat, bite = log[2], log[3], log[4]
            for num in self.candidate_list[:]:
                if not self.fill_eat_bite(num, call, eat, bite):
                    self.candidate_list.remove(num)
            self.first_call_eat_bite = [call, eat, bite]
        elif player_num != self.player_num and protocol_type == 'item':
            item = log[2]
            if item == 'shuffle':
                new_candidate_list = set()
                for num in self.candidate_list:
                    for n in itertools.permutations(num):
                        new_candidate_list.add(''.join(n))
                self.candidate_list = list(new_candidate_list)

    def initialize(self):
        ''' メンバ変数の初期化 '''
        self.valid_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]
        self.candidate_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]
        self.call_list = []
        if self.times % 3 == 0:
            self.log = []
        self.turn = 0
        self.times += 1

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

class Kaito2(Player):
    ''' Kaito の agent 2'''

    def __init__(self, player_num):
        self.player_num = player_num
        self.times = 1  # 現在のゲームの回数
        self.turn = 0  # 各ゲームにおける(自分の)ターン
        self.log = []  # 各セットにおけるログ
        self.valid_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]  # コールやセットが可能な数字(720通り)
        self.candidate_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]  # 相手の数字としてあり得る候補
        self.call_list = []  # コール済の数字
        self.first_call_eat_bite = []
        self.mode = None  # プレイスタイルのモード

    def set_card(self):
        return '810'

    def select_guard(self):
        return None

    def select_attack(self):
        return None

    def shuffle(self):
        pass

    def call(self):
        call = random.choice(self.candidate_list)
        self.call_list.append(call)
        print(f'Kaito2 call: {call}')
        return call

    def end_process(self, winner, cards_record):
        self.initialize()

    def get_log(self, log):
        player_num, protocol_type = log[0], log[1]
        if player_num == self.player_num and protocol_type == 'call':
            call, eat, bite = log[2], log[3], log[4]
            for num in self.candidate_list[:]:
                if not self.fill_eat_bite(num, call, eat, bite):
                    self.candidate_list.remove(num)
            self.first_call_eat_bite = [call, eat, bite]
        elif player_num != self.player_num and protocol_type == 'item':
            item = log[2]
            if item == 'shuffle':
                new_candidate_list = set()
                for num in self.candidate_list:
                    for n in itertools.permutations(num):
                        new_candidate_list.add(''.join(n))
                self.candidate_list = list(new_candidate_list)

    def initialize(self):
        ''' メンバ変数の初期化 '''
        self.valid_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]
        self.candidate_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]
        self.call_list = []
        if self.times % 3 == 0:
            self.log = []
        self.turn = 0
        self.times += 1

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
