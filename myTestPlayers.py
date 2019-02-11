from common import *
from player import Player

class MyTestPlayer1(Player):
    ''' Kaito の開発用 '''

    def __init__(self, player_num):
        self.player_num = player_num
        self.my_log = []

    def set_card(self):
        while True:
            card = random.randint(0, 10**N-1)
            if self.check_card(card):
                break

        # print(f'playerC: set {card}.')  # 開発用

        return card

    def call(self):
        if len(self.my_log) == 0:
            call_num = str(random.randint(0, 10**N-1)).zfill(N)
        else:
            num_dict = {}
            for i in range(len(self.my_log)):
                for num in range(10**N):
                    num = str(num).zfill(N)
                    num_log = self.my_log[i][0]
                    eat = self.my_log[i][1]
                    bite = self.my_log[i][2]
                    if self.fill_eat_bite(num, num_log, eat, bite):
                        if num in num_dict:
                            num_dict[num] += 1
                        else:
                            num_dict[num] = 1
            num_list = np.array(list(num_dict.items()))
            max_cnt = max(num_list[:, 1])
            call_num = str(random.choice(num_list[num_list[:, 1]==max_cnt][:, 0])).zfill(N)

        self.my_log.append(call_num)
        return call_num

    def fill_eat_bite(self, num, num_log, eat, bite):
        num = str(num).zfill(N)
        num_log = str(num_log).zfill(N)

        for i in range(len(num)):
            if num[i] in num_log:
                bite -= num_log.count(num[i])
                if num[i] == num_log[i]:
                    eat -= 1
                    bite += 1

        return (eat == bite == 0)

    def end_process(self, winner):
        # print(f'my_log = {self.my_log}')    # 開発用
        self.my_log = []
        return

    def get_call(self, call_num):
        pass

    def get_eat_bite(self, eat, bite):
        self.my_log[-1] = [self.my_log[-1], eat, bite]
