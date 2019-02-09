from common import *
from game import Game

class Battle:
    ''' 対戦環境の実装クラス '''

    def __init__(self):
        self.player1, self.player2 = self.set_player_names()
        self.times = self.set_times()
        self.result = {1: 0, 2: 0}  # 各playerの勝数
        self.run()

    def set_player_names(self):
        player1 = input('player1: ')
        player2 = input('player2: ')
        return player1, player2

    def set_times(self):
        ''' 対戦回数を指定 '''
        times = int(input('対戦回数: '))
        return times

    def run(self):
        ''' 指定回数回の対戦を行う '''
        for i in range(self.times):
            game = Game()
            game.play()
            winner = game.get_winner()
            self.result[winner] += 1

        self.show_result(game)

    def show_result(self, game):
        ''' 対戦結果を表示 '''
        print('\n** RESULT **')
        print(f'{self.player1}: {self.result[1]}\n{self.player2}: {self.result[2]}')
        if self.result[1] > self.result[2]:
            print(f'winner {self.player1}')
        elif self.result[1] < self.result[2]:
            print(f'winner {self.player2}')
        else:
            print('draw')

if __name__ == '__main__':
    Battle()
