import random
import numpy as np
import matplotlib.pyplot as plt
import collections

N = 3   # カードの数字の桁数
USE_ITEMS = True   # アイテムを使用するならば True
NUM_ITEMS = 3   # 所持アイテムの個数
GUARD_ITEMS = ['shuffle', 'change']    # 防御アイテム
ATTACK_ITEMS = ['high_and_low', 'slash', 'target', 'double']   # 攻撃アイテム
ITEMS = GUARD_ITEMS + ATTACK_ITEMS
BATTLE_TYPE = 'AI_vs_AI'  # 'AI_vs_AI' または 'Human'
TIMEOUT_SEC = 5  # call() の制限時間
