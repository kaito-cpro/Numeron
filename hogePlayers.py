from common import *
from player import Player

class Hoge1(Player):
    ''' デバッグのためのテストプレイヤー '''

    def set_card(self):
        return 345

    def set_items(self):
        pass

    def call(self):
        return random.randint(102, 987)

    def end_process(self, winner):
        pass

    def get_call(self, call_num):
        pass

    def get_eat_bite(self, eat, bite):
        pass

class Hoge2(Player):
    ''' デバッグのためのテストプレイヤー '''

    def set_card(self):
        return 678

    def set_items(self):
        pass

    def call(self):
        return random.randint(102, 987)

    def end_process(self, winner):
        pass

    def get_call(self, call_num):
        pass

    def get_eat_bite(self, eat, bite):
        pass
