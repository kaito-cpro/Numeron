# Numeron

battle.py を起動してプログラムを開始する.  
  
基本的な構造としては, Class Battle が大元のクラス.  
Class Game はゲームを1回行うクラスで, Class VirtualPlayer と Class Field と繋がってる.  
Class VirtualPlayer は Class Player と繋がってて,  Class Player は抽象インターフェースとして機能するので, この下に agent を継承させて実装していく感じ.  
Class Field には各 agent の数字とアイテムをメンバ変数として置いておく. Class Field は Class Game からしか操作できないので, Class Player から相手の数字を取得したりできない構造になっているので安全. だが, 逆にこの構造によって, アイテム使用の際には数字の操作が必要なので Class Player と Class Game を行き来しないといけなくなるので若干面倒(?)にもなっている(まぁ然程問題ではない).  
  
testPlayers.py の中の Class Random と Class Human に関しては, 取り敢えずはアイテム込みで動く用にはなってる(はず).  
Random は, 数字もアイテムもランダムに選び, アイテムの使用はしないようになってる(アイテム選択メソッドの中身が pass なので, アイテムとして常に None を返す).  
Human は手動なのでアイテムを使用できるが, アイテムの具体的な挙動は未実装なので, Field インスタンス内の所持アイテムリストからアイテムが減るだけ. 攻撃アイテム double を使った場合だけはちゃんと2回 call できるようになってるかな...?  
myTestPlayers.py の中はアイテムには非対応なので, common.py で USE_ITEMS=False にすれば動くはず.
