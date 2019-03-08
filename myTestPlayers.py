from common import *
from player import Player

class MyTestPlayer1(Player):
    ''' Kaito の開発用 '''

    def __init__(self, player_num):
        self.player_num = player_num
        self.guard_items = None
        self.attack_items = None
        self.card = None
        self.log = []
        self.epsilon = 0.2
        self.time = 0

    def set_card(self):
        return '345'

    def select_guard(self):
        return None
        if self.guard_items == []:
            return None
        else:
            if random.random(0, 1) < self.epsilon:
                guard_item = random.choice(self.guard_items)
                self.guard_items.remove(guard_item)
                return guard_item

    def select_attack(self):
        return None
        if self.attack_items == []:
            return None
        else:
            if random.random(0, 1) < self.epsilon:
                attack_item = random.choice(self.attack_items)
                self.attack_items.remove(attack_item)
                return attack_item

    def shuffle(self):
        pass

    def target(self):
        pass

    def change(self):
        pass

    def call(self):
        self.time += 1
        print(self.time)
        if self.time >= 2:
            return '345'
        else:
            return '123'

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
        print(log)
        self.log.append(log)
