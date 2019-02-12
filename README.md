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
  
基本的なレギュレーションについて  
  
まず, Numeron ゲームを複数回対戦して勝数の多い方を勝利とする, ということを想定している.  
そのため, 各 agent は Class Battle の中で初めに生成して, ゲームごとにリセットしない. つまり, 前のゲームの結果を見て学習したりと, 何をしても良いこととする. そのために, 各ゲームが終了したときに winner を返す end_process() メソッドを設けてある.  
  
Class Player の set_items() メソッドは, 所持するアイテムをリストとして返すように設計すること. たとえば, return \['target', 'slash', 'double'\] のように.  
Class Player の set_card() メソッドは, 設定する数字を返すように設計すること. 型は int でも str でも良い. 最高位が 0 の場合は, int で返すならば 0 は付けずに返して良く, str で返すならば 0 を付けても付けなくても良い. つまり, 結構汎用性は高くなってるのであまり気にしなくてOK. call() メソッドも同様.  
あと, call() メソッドについて, 現段階では 334 のような数字が重複する call も許容してるんだけど, Numeron ルール的にこれは許容されるんだろうか?  
Class Player の select_guard(), select_attack() メソッドは, 使用するアイテム名を str で返すように設計すること. 使用しない場合は return None とすること(return 'None' ではなくて). このとき注意が必要で, 上で述べたように, 所持アイテムのリストは Class Field に保管されていて, Class Player から直接アクセスすることはできないので, ちゃんと使用できるアイテムを agent の中で記憶しておかないとマズイ. 使用できないアイテムを選択してしまうと assert でエラーを吐かれる. 
  
あと, Class Battle の show_result() メソッドで, 一番最後に対戦結果のグラフを表示できるようになってるんだけど, y=(x回目までの勝数)/(x回目までの対戦数) にしてるんだけど, この式は適切なんだろうか...? 連続的なグラフにしようと思ったらこれしか思いつかなかったので, もしかすれば改良の余地あり.
