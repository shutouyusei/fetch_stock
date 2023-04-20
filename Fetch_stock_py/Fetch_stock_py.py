#!/usr/bin/python
# -*- coding: utf-8 -*-
from asyncio.windows_events import NULL
import os
import datetime as dt
import pandas_datareader.data as web
import sys


end = dt.date.today()
start=dt.datetime(end.year-2,end.month,end.day)
print(start)
print(end)
if __name__ == '__main__':
    args = sys.argv 
    ticker_symbol=args[1]
    if ticker_symbol!=NULL:

            ticker_symbol_dr=ticker_symbol + ".JP"

            df = web.DataReader(ticker_symbol_dr, data_source='stooq', start=start,end=end)

            df.insert(0, "code", ticker_symbol, allow_duplicates=False)

            df.to_csv( os.path.dirname(__file__) + '\s_stock_data_'+ ticker_symbol + '.csv', encoding="shift-jis")


            print(df)
            print("success")
    else:
        print ("ticker is null")
        
