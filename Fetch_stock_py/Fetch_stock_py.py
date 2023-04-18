#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import datetime as dt
import pandas_datareader.data as web
 
ticker_symbol="7177"
ticker_symbol_dr=ticker_symbol + ".JP"
 
start='2022-01-01'
end = dt.date.today()
 

df = web.DataReader(ticker_symbol_dr, data_source='stooq', start=start,end=end)

df.insert(0, "code", ticker_symbol, allow_duplicates=False)

df.to_csv( os.path.dirname(__file__) + '\s_stock_data_'+ ticker_symbol + '.csv', encoding="shift-jis")

print(df)
print("success")