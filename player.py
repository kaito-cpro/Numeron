class Player:
    ''' Player の実装クラス(抽象インターフェース) '''

    def __init__(self, player_num):
        self.player_num = player_num

    def receive(self, protocol, option=None):
        ''' 環境からプロトコルを受け取る '''
        if protocol == 'set_card':
            self.set_card()
        elif protocol == 'set_items':
            self.set_items()
        elif protocol == 'end_process':
            self.end_process(option)
        elif protocol == 'eat_bite':
            self.get_eat_bite(option)

    def set_card(self):
        ''' 数字をセットする '''
        pass

    def set_items(self):
        ''' アイテムをセットする '''
        pass

    def end_process(self, winner):
        ''' ゲーム終了時の処理 '''
        pass

    def get_eat_bite(self, eat_bite):
        ''' Eat/Bite を環境から受け取る '''
        pass
