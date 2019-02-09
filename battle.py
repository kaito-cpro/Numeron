from common import *
from game import Game
from virtualPlayer import VirtualPlayer

class Battle:
    ''' 対戦環境の実装クラス '''

    def __init__(self):
        print('')
        self.virtual_player = VirtualPlayer()   # 各ゲームでプレイヤーをリセットせずに使う
        self.player1, self.player2 = self.set_player_names()
        self.times = self.set_times()
        self.result = []  # 勝ったプレイヤーの番号
        self.run()

    def set_player_names(self):
        print('\n名前を入力してください')
        player1 = input('player1: ')
        player2 = input('player2: ')
        return player1, player2

    def set_times(self):
        ''' 対戦回数を指定 '''
        print('\n対戦回数を入力してください')
        times = int(input('対戦回数: '))
        return times

    def run(self):
        ''' 指定回数回の対戦を行う '''
        for i in range(self.times):
            game = Game(self.virtual_player)
            game.play()
            winner = game.get_winner()
            self.result.append(winner)

        self.show_result(game)

    def show_result(self, game):
        ''' 対戦結果を表示 '''
        winner = None
        result_1 = self.result.count(1)    # player1 の勝数
        result_2 = self.result.count(2)    # player2 の勝数

        print('\n** RESULT **')
        print(f'{self.player1}: {result_1}\n{self.player2}: {result_2}')
        if result_1 > result_2:
            winner = 1
            print(f'winner {self.player1}')
        elif result_1 < result_2:
            winner = 2
            print(f'winner {self.player2}')
        else:
            print('draw')

        use_graph = input('\n対戦結果のグラフを表示しますか(True or False): ')
        if use_graph:
            x = [i for i in range(0, self.times+1)]
            y = [self.result[:i].count(winner)/(i+1) for i in range(0, self.times+1)]
            plt.plot(x, y)
            plt.show()

if __name__ == '__main__':
    Battle()
