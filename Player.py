import random
class Player:
    
    '''
    レイヤークラスのコンストラクタ
    引数： name プレイヤーの名前
    '''

    def __init__(self, name):
        self._name = name
        self._wincount = 0
    '''
    じゃんけんの手を出す関数：
    0   , 1, 2 をランダムに出力する
    '''
    
    def show_hand(self):
        return random.randrange(3)
