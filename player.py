class Player:
    ''' Player の実装クラス(抽象インターフェース) '''

    def __init__(self, player_num):
        self.player_num = player_num

    def set_card(self):
        ''' 数字をセットする
            返り値の型は int, str のいずれでもよい '''
        pass

    def set_items(self):
        ''' アイテムをセットする '''
        pass

    def call(self):
        ''' 数字をコールする
            返り値の型は int, str のいずれでもよい '''
        pass

    def end_process(self, winner):
        ''' ゲーム終了時の処理 '''
        pass

    def get_call(self, call_num):
        ''' 相手の call を環境から受け取る
            call_num の型は str '''
        pass

    def get_eat_bite(self, eat, bite):
        ''' Eat/Bite を環境から受け取る '''
        pass
