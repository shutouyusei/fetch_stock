#!/usr/bin/python
# -*- coding: utf-8 -*-
from asyncio.windows_events import NULL
from genericpath import exists
import os
import datetime as dt
from tkinter import N
import pandas_datareader.data as web
import sys



if __name__ == '__main__':
    args = sys.argv 
    ticker_symbol=args[1]
    if ticker_symbol!=NULL:
           # get today date
            end = dt.date.today()
            start=dt.datetime(end.year-2,end.month,end.day)
            # accesse pandas_datareader to get stock imf
            ticker_symbol_dr=ticker_symbol + ".JP"

            df = web.DataReader(ticker_symbol_dr, data_source='stooq', start=start,end=end)

            df.insert(0, "code", ticker_symbol, allow_duplicates=False)
            
            # output 
            if df.empty==True:
                print("NUll")
            else:
                # mkdir on cd 
                os.makedirs( os.getcwd()+'\csv_stock_data',exist_ok=True)

                # create csv stock_data
                df.to_csv( os.getcwd() + '\csv_stock_data\s_stock_data_'+ ticker_symbol + '.csv', encoding="shift-jis")
                print("success")
    else:
        # no ticker
        print ("ticker is null")
        
