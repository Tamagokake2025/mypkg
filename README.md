## パッケージに含まれるもの
- talker ノード(パブリッシャ)   
0.5 秒ごとに 0.000 ~ 10.000 の範囲で乱数を トピック名:　/rannum　として出力する
- listener ノード(サブスクライバ)   
/rannum の乱数を読み取り、小数点切り捨てでa以上b未満かを判定する
- tark_listen.launch ファイル   
talkerノードとlistenerノードのlaunchファイル

![test](https://github.com/tamagokake2025/mypkg/actions/workflows/test.yml/badge.svg)


### ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  - [ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
- © 2025 Keutaro Takeda
