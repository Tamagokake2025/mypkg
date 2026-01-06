# このRos２パッケージに含まれるもの
![test](https://github.com/tamagokake2025/mypkg/actions/workflows/test.yml/badge.svg)
- `random` ノード   
0.5 秒ごとに 0.000 ~ 10.000 の範囲で乱数をトピック名: `/rannum`(Float32型) としてpublishする。
- `checkcount` ノード   
`/rannum`の乱数を読み取り、小数点切り捨てでa以上b未満かを判定する。`checkcount`を起動してから、その範囲の乱数を受信した回数を数える。数えた結果は、乱数を読み取る度にトピック名: `/numcou`(String型) としてpublishする。
- `random_count.launch` ファイル   
`random`と`checkcount`のlaunchファイル

## 実行例
1. `random`で乱数を発信。
```
$ ros2 run mypkg random
[INFO] [1767547081.935833557] [random]: 1.246
[INFO] [1767547082.419356870] [random]: 1.417
[INFO] [1767547082.919340115] [random]: 0.782
[INFO] [1767547083.418940644] [random]: 9.016
[INFO] [1767547083.919719645] [random]: 7.333
[INFO] [1767547084.420914546] [random]: 7.084
[INFO] [1767547084.919737199] [random]: 3.138
[INFO] [1767547085.421205072] [random]: 9.742
[INFO] [1767547085.920649850] [random]: 8.392
(Ctrl+Cで終了）
```

2. `checkcount`で乱数を受信。乱数をどの範囲か判定する。(受信しないと何も表示されないため、別の端末からpublish)
```
$ ros2 run mypkg checkcount
[INFO] [1767547148.183329062] [checkcount]: 6以上7未満（1回目）
[INFO] [1767547148.636761505] [checkcount]: 4以上5未満（1回目）
[INFO] [1767547149.136375853] [checkcount]: 1以上2未満（1回目）
[INFO] [1767547149.637586947] [checkcount]: 4以上5未満（2回目）
[INFO] [1767547150.138244285] [checkcount]: 5以上6未満（1回目）
[INFO] [1767547150.637261829] [checkcount]: 9以上10未満（1回目）
[INFO] [1767547151.137597402] [checkcount]: 8以上9未満（1回目）
[INFO] [1767547151.639136053] [checkcount]: 3以上4未満（1回目）
[INFO] [1767547152.137490784] [checkcount]: 3以上4未満（2回目）
[INFO] [1767547152.638034607] [checkcount]: 7以上8未満（1回目）
[INFO] [1767547153.138539779] [checkcount]: 4以上5未満（3回目）
（Ctrl+Cで終了）
```

3. `/numcou`の内容(`checkcount`がpublishしている時に確認可能。)
```
$ ros2 topic echo /numcou
data: '1以上2未満: 1回

  2以上3未満: 1回

  3以上4未満: 1回

  5以上6未満: 2回

  6以上7未満: 1回

  8以上9未満: 2回'
---
data: '1以上2未満: 2回

  2以上3未満: 1回

  3以上4未満: 1回

  5以上6未満: 2回

  6以上7未満: 1回

  8以上9未満: 2回'
---
data: '1以上2未満: 2回

  2以上3未満: 1回

  3以上4未満: 1回

  5以上6未満: 3回

  6以上7未満: 1回

  8以上9未満: 2回'
---
data: '1以上2未満: 2回

  2以上3未満: 2回

  3以上4未満: 1回

  5以上6未満: 3回

  6以上7未満: 1回

  8以上9未満: 2回'
---
data: '1以上2未満: 2回

  2以上3未満: 2回

  3以上4未満: 1回

  4以上5未満: 1回

  5以上6未満: 3回

  6以上7未満: 1回

  8以上9未満: 2回'
---
（Ctrl+Cで終了）
```
4. launchファイルで`random`,`checkcount`の両方を使用。
```
$ ros2 launch mypkg random_count.launch.py
[INFO] [launch]: All log files can be found below /home/...
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [random-1]: process started with pid [629264]
[INFO] [checkcount-2]: process started with pid [629266]
[checkcount-2] [INFO] [1767546896.566834239] [checkcount]: 2以上3未満（1回目）
[random-1] [INFO] [1767546896.566834259] [random]: 2.815
[random-1] [INFO] [1767546897.045922733] [random]: 2.191
[checkcount-2] [INFO] [1767546897.046493759] [checkcount]: 2以上3未満（2回目）
[random-1] [INFO] [1767546897.549655688] [random]: 3.557
[checkcount-2] [INFO] [1767546897.550774609] [checkcount]: 3以上4未満（1回目）
[random-1] [INFO] [1767546898.049929257] [random]: 0.594
[checkcount-2] [INFO] [1767546898.051213560] [checkcount]: 0以上1未満（1回目）
[random-1] [INFO] [1767546898.547848225] [random]: 7.055
[checkcount-2] [INFO] [1767546898.549350733] [checkcount]: 7以上8未満（1回目）
[random-1] [INFO] [1767546899.047933816] [random]: 9.679
[checkcount-2] [INFO] [1767546899.048705938] [checkcount]: 9以上10未満（1回目）
[random-1] [INFO] [1767546899.547101565] [random]: 9.922
[checkcount-2] [INFO] [1767546899.547576397] [checkcount]: 9以上10未満（2回目）
[random-1] [INFO] [1767546900.047241766] [random]: 3.570
[checkcount-2] [INFO] [1767546900.048246344] [checkcount]: 3以上4未満（2回目）
[random-1] [INFO] [1767546900.549142181] [random]: 5.931
[checkcount-2] [INFO] [1767546900.550156959] [checkcount]: 5以上6未満（1回目）
[random-1] [INFO] [1767546901.048270898] [random]: 3.903
[checkcount-2] [INFO] [1767546901.048870293] [checkcount]: 3以上4未満（3回目）
[random-1] [INFO] [1767546901.546270667] [random]: 6.387
[checkcount-2] [INFO] [1767546901.546967903] [checkcount]: 6以上7未満（1回目）
（Ctrl+Cで終了）
```

## テスト環境
- python  
　- リモートテスト済みバージョン: 3.7〜3.10
- Ubuntu  
　- リモートテスト済みバージョン: 22.04.5 LTS

## 参考サイト
- [ノードの参考](https://stray-cat.com/blog_01_4_about_publisher/)
- [乱数の参考](https://note.nkmk.me/python-random-randrange-randint/)
- [判定回数のカウントの参考](https://note.nkmk.me/python-in-basic/)
- [bashでのif文の参考](https://af-e.net/linux-bash-if/)
- [パブリッシュする文字列を並べ替える方法の参考](https://maku77.github.io/p/qqkggoz/?utm_source=chatgpt.com)
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  - [ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
- © 2025 Keutaro Takeda
