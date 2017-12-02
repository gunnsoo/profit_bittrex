#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime as dt
import pandas as pd


#Bittrex履歴読み込み
order_history = pd.read_csv('Bittrex.com - Order History.csv')
order_history = order_history.loc[:, ['Closed Date', 'Cost / Proceeds']]
#BTCJPYデータ読み込み(Investing.com) ※１番下の２行は消してください(高値など書いてあるとこ)
btc_price = pd.read_csv('BTC JPY 過去のデータ.csv')
btc_price = btc_price.loc[:, ['日付け', '終値']]

#比較するために両方の日付けを変更
date = []
for tmp_date in order_history["Closed Date"]:
    try:
        tmp_date = dt.datetime.strptime(tmp_date, '%m/%d/%Y %H:%M:%S AM')
        tmp_date = dt.date(tmp_date.year, tmp_date.month, tmp_date.day)
        date.append(tmp_date)
    except ValueError:
        tmp_date = dt.datetime.strptime(tmp_date, '%m/%d/%Y %H:%M:%S PM')
        tmp_date = dt.date(tmp_date.year, tmp_date.month, tmp_date.day)
        date.append(tmp_date)
order_history['Closed Date'] = date

date = []
for tmp_date in btc_price['日付け']:
    tmp_date = dt.datetime.strptime(str(tmp_date), '%Y年%m月%d日')
    tmp_date = dt.date(tmp_date.year, tmp_date.month, tmp_date.day)
    date.append(tmp_date)
btc_price['日付け'] = date

#終値の "," を取り除き、型をintに変換
price = []
for tmp_price in btc_price["終値"]:
    price.append(int(tmp_price.replace(",", "")))
btc_price["終値"] = price

#BTC換算の利益総額
profit_btc = []
for p in order_history["Cost / Proceeds"]:
    profit_btc.append(p)

#終値＊Cost/ProceedsでJPY損益を算出
profit_yen = []
for i in range(0, len(order_history.index)):
    for x in range(0, len(btc_price.index)):
        if order_history["Closed Date"][i] == btc_price["日付け"][x]:
            profit_yen.append(btc_price["終値"][x] * order_history["Cost / Proceeds"][i])

print("合計損益(BTC):",sum(profit_btc),"BTC")
print("合計損益(円):",sum(profit_yen),"円")
