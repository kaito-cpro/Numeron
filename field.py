from game import Game
from virtualPlayer import VirtualPlayer

class Field:
    ''' カードとアイテムの実装クラス '''

    def __init__(self):
        self.card = None
        self.items = None

    def set_field(self, player):
        for i in range(2):
            self.set_card(player)
            self.set_items(player)
            player.switch()

    def set_card(self, player):
        ''' 数字をセットする '''
        card = player.set_card()
        # assert
        self.card = card

    def set_items(self, player):
        ''' アイテムをセットする '''
        items = player.set_items()
        # assert
        self.items = items
