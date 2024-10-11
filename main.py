import random
class Player:
'''
プレイヤークラスのコンストラクタ
引数： name プレイヤーの名前
'''
def __init__(self, name):
self._name = name
self._wincount = 0
'''
じゃんけんの手を出す関数：
0, 1, 2 をランダムに出力する
'''
def show_hand(self):
return random.randrange(3)

class Judge:
# 審判クラスのコンストラクタなし



'''
じゃんけんの手と数値の対応（クラス定数として定義）
グー = 0
チョキ = 1
パー = 2

'''
def print_hand(self, hand):
if hand == 0:
return 'グー'
elif hand == 1:
return 'チョキ'
elif hand == 2:
return 'パー'

