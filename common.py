import random
import numpy as np
import matplotlib.pyplot as plt
import collections

N = 3   # カードの数字の桁数
USE_ITEMS = False   # アイテムを使用するならば True
NUM_ITEMS = 3   # 所持アイテムの個数
GUARD_ITEMS = ['slash', 'shuffle', 'change']    # 防御アイテム
ATTACK_ITEMS = ['double', 'high_and_low', 'target']   # 攻撃アイテム
ITEMS = GUARD_ITEMS + ATTACK_ITEMS
