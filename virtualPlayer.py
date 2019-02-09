class VirtualPlayer:
    ''' Class Game と Class Player の仲介クラス '''

    def __init__(self):
        self.player1 = PlayerFactory().create_player(1)
        self.player2 = PlayerFactory().create_player(2)

        self.player = None
        self.set_former_player()

        self.turn = {self.player1: self.player2,    \
                     self.player2: self.player1}

    def set_former_player(self):
        ''' ランダムに先攻を決める '''
        if random.randint(0, 1) == 0:
            self.player = self.player1
        else:
            self.player = self.player2

    def switch(self):
        ''' 手番の交代 '''
        self.player = self.turn[self.player]
