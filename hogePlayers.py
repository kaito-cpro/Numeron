from player import Player

class Hoge1(Player):
    ''' デバッグのためのテストプレイヤー '''

    def set_card(self):
        return 345

    def set_items(self):
        return 'items_hoge1'

    def end_process(self, winner):
        pass

class Hoge2(Player):
    ''' デバッグのためのテストプレイヤー '''

    def set_card(self):
        return 678

    def set_items(self):
        return 'items_hoge2'

    def end_process(self, winner):
        pass
