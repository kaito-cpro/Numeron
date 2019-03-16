from common import *
from player import Player

class MyTestPlayer1(Player):
    ''' テストプレイヤー '''

    def __init__(self, player_num):
        self.player_num = player_num
        self.card_list = [str(n).zfill(N) for n in range(10**N-1) if self.check_card(n)]
        self.log = []
        self.call_list = []

    def set_card(self):
        return '514'

    def select_guard(self):
        return None

    def select_attack(self):
        return None

    def shuffle(self):
        pass

    def call(self):
        if self.card_list == []:
            while True:
                call_num = str(random.randint(0, 10**N-1)).zfill(N)
                if self.check_card(call_num) and call_num not in self.call_list:
                    break
        else:
            call_num = random.choice(self.card_list)
        call_num = str(call_num).zfill(N)
        self.call_list.append(call_num)
        print(call_num)
        return call_num

    def end_process(self, winner, cards_record):
        pass

    def get_log(self, log):
        if log[0] == self.player_num and log[1] == 'call':
            for num in self.card_list[:]:
                if not self.fill_eat_bite(num, log[2], log[3], log[4]):
                    self.card_list.remove(num)

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
