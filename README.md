# profit_bittrex

## Overview
Bittrexでのトレード損益を、JPYに換算して計算します。

## Description
以下のcsvファイルが必要です。

①Bittrexの売買履歴 "Bittrex.com - Order History.csv"  
②BTC/JPY価格データ(Investing.comからダウンロードしてください) "BTC JPY 過去のデータ.csv"  
※価格データの１番下の２行(高値などが書いてある)は削除してください

JPY価格は終値を基準としています。

## Usage
上の２ファイルとこのスクリプトを同じディレクトリに置いて、実行してください。  
JPY換算した損益が表示されます。  
環境はpython3系です。事前にpandasをインストールする必要があります。

```
git clone https://github.com/pyboot/profit_bittrex.git
pip install pandas
python profit_bittrex.py
```

実行結果

```
合計損益(BTC): 1 BTC
合計損益(円): 1000000 円
```
