class VirtualPlayer:
    ''' Class Game と Class Player の仲介クラス '''

    def __init__(self):
        self.player1 = PlayerFactory().create_player(1)
        self.player2 = PlayerFactory().create_player(2)
