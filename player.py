class Player:
    ''' Player の実装クラス(抽象インターフェース) '''

    def __init__(self):
        pass

    def receive(self, protocol, option=None):
        ''' 環境からプロトコルを受け取る '''
        if protocol == 'set_card':
            self.set_card()
        elif protocol == 'set_items':
            self.set_items()
        elif protocol == 'end_process':
            self.end_process(option)

    def set_card(self):
        ''' 数字をセットする '''
        pass

    def set_items(self):
        ''' アイテムをセットする '''
        pass

    def end_process(self, winner):
        ''' ゲーム終了時の処理 '''
        pass
