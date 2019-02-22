from common import *
from player import Player

class MyTestPlayer1(Player):
    ''' Kaito の開発用 '''

    def __init__(self, player_num):
        self.player_num = player_num
        self.items = None
        self.card = None
        self.log = []

    def set_items(self):
        pass

    def set_card(self):
        while True:
            card = random.randint(0, 10**N-1)
            if self.check_card(card):
                break
        self.card = card
        return card

    def call(self):
        ''' 現段階で動かない '''
        while True:
            if len(self.log) == 0:
                call_num = str(random.randint(0, 10**N-1)).zfill(N)
            else:
                num_dict = {}
                for i in range(len(self.log)):
                    for num in range(10**N):
                        num = str(num).zfill(N)
                        num_log = self.log[i][0]
                        eat = self.log[i][1]
                        bite = self.log[i][2]
                        if self.fill_eat_bite(num, num_log, eat, bite):
                            if num in num_dict:
                                num_dict[num] += 1
                            else:
                                num_dict[num] = 1
                num_list = np.array(list(num_dict.items()))
                max_cnt = max(num_list[:, 1])
                call_num = str(random.choice(num_list[num_list[:, 1]==max_cnt][:, 0])).zfill(N)

            if self.check_card(call_num):
                break

        return call_num

    def fill_eat_bite(self, num, num_log, eat, bite):
        num = str(num).zfill(N)
        num_log = str(num_log).zfill(N)

        for i in range(len(num)):
            if num[i] == num_log[i]:
                eat -= 1
            elif num[i] in num_log:
                bite -= 1

        return (eat == bite == 0)

    def end_process(self, winner):
        # print(f'log = {self.log}')    # 開発用
        print(f'MyTestPlayer の数字は {self.card} でした')  # 開発用
        self.log = []
        return

    def get_log(self, log):
        self.log.append(log)
