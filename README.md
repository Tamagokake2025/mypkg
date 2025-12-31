# パッケージに含まれるもの
![test](https://github.com/tamagokake2025/mypkg/actions/workflows/test.yml/badge.svg)
- talker ノード(パブリッシャ)   
0.5 秒ごとに 0.000 ~ 10.000 の範囲で乱数を トピック名:　/rannum　として出力する
- listener ノード(サブスクライバ)   
/rannum の乱数を読み取り、小数点切り捨てでa以上b未満かを判定する
- tark_listen.launch ファイル   
talkerノードとlistenerノードのlaunchファイル

## 使用方法
　ターミナルで以下のコマンドを入力。クローン。ビルド。
```
$ git clone https://github.com/Tamagokake2025/myokg.git
$ colcon build
```

## 実行例
1. talkerノードで乱数を発信。
```

```

2. listenerノードで乱数を受信。乱数をどの範囲か判定する。
```

```
3. launchファイルでtalkerノード,listenerノードの両方を使用。
```

```

##テスト環境
- python  
　- リモートテスト済みバージョン: 3.7〜3.10
- Ubuntu  
　- リモートテスト済みバージョン: 22.04.5 LTS

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  - [ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
- © 2025 Keutaro Takeda
