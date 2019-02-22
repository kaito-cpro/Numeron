# Numeron

battle.py を起動してプログラムを開始する.  

大幅な改良点  
* Class Field の場所を変更した(Class Game から import していたのを, Class VirtualPlayer からの import に変更).  
* Class Player のメソッド get_call() と get_eat_bite() を一括して get_log() にまとめた. get_log() は, 何かアクション(コールまたはアイテム)があったときにそのログを受け取るメソッドである. log のレギュレーションについては Class Game の write_log() メソッドを参照のこと.  

基本的な構造としては, Class Battle が大元のクラス.  
Class Game はゲームを1回行うクラスで, Class VirtualPlayer と Class Field と繋がってる.->改良: Class Field は Class VirtualPlayer との接続にした(これにより, Class Game の抽象性を高めた(複雑な処理を Class VirtualPlayer に一任できた)).  
Class VirtualPlayer は Class Player と繋がってて,  Class Player は抽象インターフェースとして機能するので, この下に agent を継承させて実装していく感じ.  
Class Field には各 agent の数字とアイテムをメンバ変数として置いておく.

testPlayers.py の中の Class Random と Class Human に関しては, 取り敢えずはアイテム込みで動く用にはなってる.  
Random は, 数字もアイテムもランダムに選び, アイテムの使用はしないようになってる(アイテム選択メソッドの中身が pass なので, アイテムとして常に None を返す).  
Human は手動なのでアイテムを使用できるが, アイテムの具体的な挙動は未実装なので, Field インスタンス内の所持アイテムリストからアイテムが減るだけ. 攻撃アイテム double, high_and_low と防御アイテム shuffle を使った場合だけはちゃんと動作するようになってるはず. double については, Class Game の中の self.double_flg をフラグとして用いて実現してるんだけど, 書き方があまり美しくない(可読性が悪い)ので, 改良の余地あり.  
myTestPlayers.py の中はアイテムには非対応なので, common.py で USE_ITEMS=False にすれば動くはず.

基本的なレギュレーションについて  

まず, Numeron ゲームを複数回対戦して勝数の多い方を勝利とする, ということを想定している.  
そのため, 各 agent は Class Battle の中で初めに生成して, ゲームごとにリセットしない. つまり, 前のゲームの結果を見て学習したりと, 何をしても良いこととする. そのために, 各ゲームが終了したときに winner を返す end_process() メソッドを設けてある.  

Class Player の set_items() メソッドは, 所持するアイテムをリストとして返すように設計すること. たとえば, return \['target', 'slash', 'double'\] のように.  
Class Player の set_card() メソッドは, 設定する数字を返すように設計すること. 型は int でも str でも良い. 最高位が 0 の場合は, int で返すならば 0 は付けずに返して良く, str で返すならば 0 を付けても付けなくても良い. つまり, 結構汎用性は高くなってるのであまり気にしなくてOK. call() メソッドも同様.->でも, str を強く推奨.  
あと, call() メソッドについて, 現段階では 334 のような数字が重複する call も許容してるんだけど, Numeron ルール的にこれは許容されるんだろうか?->改良: このような call は禁止した.  
Class Player の select_guard(), select_attack() メソッドは, 使用するアイテム名を str で返すように設計すること. 使用しない場合は return None とすること(return 'None' ではなくて). このとき注意が必要で, 上で述べたように, 所持アイテムのリストは Class Field に保管されていて, Class Player から直接アクセスすることはできないので, ちゃんと使用できるアイテムを agent の中で記憶しておかないとマズイ. 使用できないアイテムを選択してしまうと assert でエラーを吐かれる.

あと, Class Battle の show_result() メソッドで, 一番最後に対戦結果のグラフを表示できるようになってるんだけど, y=(x回目までの勝数)/(x回目までの対戦数) にしてるんだけど, この式は適切なんだろうか...? 連続的なグラフにしようと思ったらこれしか思いつかなかったので, もしかすれば改良の余地あり.
