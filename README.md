# パッケージに含まれるもの
![test](https://github.com/tamagokake2025/mypkg/actions/workflows/test.yml/badge.svg)
- 'talker' ノード   
0.5 秒ごとに 0.000 ~ 10.000 の範囲で乱数を トピック名:'/rannum'として出力する。
- 'listener' ノード   
'/rannum'の乱数を読み取り、小数点切り捨てでa以上b未満かを判定する。'listener'を起動してから、その範囲の乱数を受信した回数を数える。
- 'tark_listen.launch' ファイル   
'talker'と'listener'のlaunchファイル

## 実行例
1. 'talker'で乱数を発信。
```
$ ros2 run mypkg talker
[INFO] [1767182724.055183308] [talker]: 2.105
[INFO] [1767182724.543917365] [talker]: 2.306
[INFO] [1767182725.043113454] [talker]: 1.641
[INFO] [1767182725.544174821] [talker]: 1.434
[INFO] [1767182726.044014609] [talker]: 3.681
（Ctrl+Cで終了）
```

2. 'listener'で乱数を受信。乱数をどの範囲か判定する。(受信しないと何も表示されないため、別の端末からパブリッシュ)
```
$ ros2 run mypkg listener
[INFO] [1767182877.452304404] [listener]: 4以上5未満（1回目）
[INFO] [1767182877.938288796] [listener]: 7以上8未満（1回目）
[INFO] [1767182878.439248829] [listener]: 5以上6未満（1回目）
[INFO] [1767182878.938215487] [listener]: 7以上8未満（2回目）
[INFO] [1767182879.439284868] [listener]: 2以上3未満（1回目）
[INFO] [1767182879.939480202] [listener]: 6以上7未満（1回目）
[INFO] [1767182880.440337459] [listener]: 7以上8未満（3回目）
[INFO] [1767182880.938297030] [listener]: 5以上6未満（2回目）
（Ctrl+Cで終了）
```

3. launchファイルで'talker','listener'の両方を使用。
```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/...
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [618469]
[INFO] [listener-2]: process started with pid [618471]
[listener-2] [INFO] [1767183252.771101988] [listener]: 5以上6未満（1回目）
[talker-1] [INFO] [1767183252.771119985] [talker]: 5.490
[talker-1] [INFO] [1767183253.261914578] [talker]: 6.964
[listener-2] [INFO] [1767183253.263516760] [listener]: 6以上7未満（1回目）
[talker-1] [INFO] [1767183253.761760157] [talker]: 1.632
[listener-2] [INFO] [1767183253.762508041] [listener]: 1以上2未満（1回目）
[talker-1] [INFO] [1767183254.260908221] [talker]: 3.843
[listener-2] [INFO] [1767183254.261220673] [listener]: 3以上4未満（1回目）
[talker-1] [INFO] [1767183254.762188802] [talker]: 5.345
[listener-2] [INFO] [1767183254.763193178] [listener]: 5以上6未満（2回目）
[talker-1] [INFO] [1767183255.261757949] [talker]: 5.271
[listener-2] [INFO] [1767183255.262587135] [listener]: 5以上6未満（3回目）
[talker-1] [INFO] [1767183255.761863051] [talker]: 5.461
[listener-2] [INFO] [1767183255.762181442] [listener]: 5以上6未満（4回目）
[talker-1] [INFO] [1767183256.261671742] [talker]: 2.933
[listener-2] [INFO] [1767183256.262480028] [listener]: 2以上3未満（1回目）
[talker-1] [INFO] [1767183256.761630254] [talker]: 5.563
[listener-2] [INFO] [1767183256.762313839] [listener]: 5以上6未満（5回目）
[talker-1] [INFO] [1767183257.261788141] [talker]: 4.544
[listener-2] [INFO] [1767183257.262435652] [listener]: 4以上5未満（1回目）
[talker-1] [INFO] [1767183257.761711488] [talker]: 2.922
[listener-2] [INFO] [1767183257.762389273] [listener]: 2以上3未満（2回目）
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

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  - [ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
- © 2025 Keutaro Takeda
