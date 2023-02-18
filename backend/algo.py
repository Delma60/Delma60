import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta
from machineLearning import MachneLearning
from os import path
from tqdm import tqdm
import time
class Algo:
    def __init__(self, account, password, server, ticks=None):
        self.account = account
        self.password = password
        self.server = server
        self.tick = ["EURUSD", "USDJPY", "GBPUSD"]
        self.from_date = datetime.now() - timedelta(days=60)
        self.to_date = datetime.now()
        self.signal = MachneLearning(self.tick)
        self.get_ohlcv(self.tick)

    def connect_to_db(self):
        if not mt5.initialize():
            return mt5.last_error()
        else:
            authorized = mt5.login(self.account, password=self.password, server=self.server)
            if authorized:
                return "login"
            else:
                return "failed to connect at account #{}, error code: {}".format(self.account, mt5.last_error())

    def run(self):
        connection_stat = self.connect_to_db()
        print(connection_stat)
        for i in self.tick:
            signal = self.signal.run(i)
            print("signal: ", signal)
            # self.buy_and_sell()
        
    def buy_and_sell(self, symbol, lot,  price, sl, tp, signal_type=None, deviation=20):
         
        if signal_type == "BUY":
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": lot,
                "type": mt5.ORDER_TYPE_BUY,
                "price": price,
                "sl": sl,
                "tp": tp,
                "deviation": deviation,
                "magic": 234000,
                "comment": "",
                "type_time":mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_RETURN
            }
        elif signal_type == "SELL":
            request = {}
        
        result = mt5.order_send(request)

        pass

    def get_ohlcv(self, symbol):

        print("getting data")
        
        with tqdm(total=len(symbol), desc="Loading data") as pbar:
            for s in symbol:
                df = pd.read_csv(f"repo/market/{s}.csv")
                filePath = path.exists(f"repo/market/{s}.csv")
                if filePath is False or df.empty:
                    data = pd.DataFrame(mt5.copy_rates_range(s, mt5.TIMEFRAME_H3, self.from_date, self.to_date))
                    data.to_csv(f"repo/market/{symbol}.csv")   
                pbar.set_description(f"Loading {s} hisorical data _2")
                pbar.update(1)

    # if filePath is False or df.empty:
        #     for i in tqdm(range(100), desc=f"Loading {symbol} historic data", ascii=False, ncols=100):
        #         data = pd.DataFrame(mt5.copy_rates_range(symbol, mt5.TIMEFRAME_H3, self.from_date, self.to_date))
        #         data.to_csv(f"repo/market/{symbol}.csv")
        # else:
        #     while True :
        #         for i in tqdm(range(100), desc=f"Reloading {symbol} historic data", ascii=False, ncols=100):
        #             data = pd.DataFrame(mt5.copy_rates_range(symbol, mt5.TIMEFRAME_H3, self.from_date, self.to_date))
        #             data.to_csv(f"repo/market/{symbol}.csv")
        #         time.sleep(3600)
