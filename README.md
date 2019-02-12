# Numeron

battle.py を起動してプログラムを開始する.  
testPlayers.py の中の Random と Human に関しては, 取り敢えずはアイテム込みで動く用にはなってる(はず).  
Random は, 数字もアイテムもランダムに選び, アイテムの使用はしないようになってる(アイテムとして常に None を返す).  
Human は手動なのでアイテムを使用できるが, アイテムの具体的な挙動は未実装なので, Field インスタンス内の所持アイテムが減るだけ. 攻撃アイテム double を使った場合だけはちゃんと2回 call できるようになってるかな...?  
myTestPlayers.py の中はアイテムには非対応なので, common.py で USE_ITEMS=False にすれば動くはず.
