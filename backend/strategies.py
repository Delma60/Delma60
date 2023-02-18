import pandas as pd
import numpy as np
import pandas_ta as ta
import requests

import  yfinance as yf
from datetime import datetime, timedelta
from itertools import combinations

start = datetime.now() - timedelta(days=60) 
end =datetime.now()

def mean_reversion(df, threshold=0.01):
    close = df['close']

    mean = close.rolling(window=100).mean()
    std = close.rolling(window=100).std()
    # close['position'] = 0
    z_score = (close - mean) / std
    sig = pd.Series(0, index=close.index)

    sig[z_score > threshold] = -1.0
    sig[z_score < threshold] = 1.0
    sig.fillna(method="ffill", inplace=True)
    return sig.iloc[-1]

def scalping(df, threshold=.005):
    signal = [0.0]
    for i in range(1, len(df)):
        current_price = df.iloc[i]['close']
        previous_price = df.iloc[i-1]['close']
        high = df.iloc[i]['high']
        low = df.iloc[i]['low']

        if high - low >= threshold:
            if current_price > previous_price:
                signal.append(1.0)
            else:
                signal.append(-1.0)
        else: 
            signal.append("None")
    df['signal'] = signal
    return df['signal'].iloc[-1]

def targetted_news(df, ticker_2={"forex": [], "stock": []}):
    # get news from api 
    apiKey = ""
    

    df_forex = yf.download(ticker_2["forex"], start , end)
    df_stock = yf.download(ticker_2['stock'], start, end )

    df_forex_2 = pd.DataFrame(df_forex)
    df_stock_2 = pd.DataFrame(df_stock)

    events = ['Non-Farm Payroll', "FOMC Meeting", "GDP Report"]
    sources = ['CNN', "Bloomberg", "Fox News"]
    window =3
    if df_forex_2.empty is False:
        for i in range(window, len(df_forex)):
            for event in events:
                if event in df_forex.iloc[i-window:i].columns and df_forex.iloc[i-window:i][event].mean():
                    print("Buy signal for", df_forex.colums[0], "based on", event)
            for source in sources:
                resp = requests.get("htps://newsapi.org/v2/everything", params={'q': df_forex.columns[0], "source": source, 'from':start, 'to': end, "apiKey": apiKey})
                news_df = pd.DataFrame(resp.json()['articles'])
                if news_df['publishedAt'].str.slice(stop=10).isin(df_forex.index[i-window:i].strftime("%Y-%m-%d")).any():
                    print("Buy signal for", df_forex.colums[0], "based on news from:", source)

    if df_stock_2.empty is False:
        for i in range(window, len(df_stock)):
            for event in events:
                if event in df_stock.iloc[i-window:i].columns and df_stock.iloc[i-window:i][event].mean():
                    print("Buy signal for", df_stock.colums[0], "based on", event)
            for source in sources:
                resp = requests.get("htps://newsapi.org/v2/everything", params={'q': df_stock.columns[0], "source": source, 'from':start, 'to': end, "apiKey": apiKey})
                news_df = pd.DataFrame(resp.json()['articles'])
                if news_df['publishedAt'].str.slice(stop=10).isin(df_stock.index[i-window:i].strftime("%Y-%m-%d")).any():
                    print("Buy signal for", df_stock.colums[0], "based on news from:", source)

def price_action(df):
    df['signal'] = 0.0
    df.loc[df['close'] > df['close'].shift(-1), "signal"] = 1.0
    df.loc[df['close'] < df['close'].shift(-1), "signal"] = -1.0
    return df['signal'].iloc[-1]

def arbitrage(tickers=[]):
    new_ticker = []
    for i in tickers:
        new_ticker.append(f"{i}=X")
    pairs = list(combinations(new_ticker, 2))
    df = yf.download(new_ticker, start, end)
    returns = df['Adj Close'].pct_change()
    
    for pair in pairs:
        stock1 = pair[0]
        stock2 = pair[1]
        df_pair = pd.DataFrame()
        df_pair['ret1'] = returns[stock1]   

        df_pair['ret2'] = returns[stock2]
        df_pair = df_pair.dropna()
        df_pair['spread'] = df_pair['ret1'] - df_pair['ret2']
        mean_spread = df_pair['spread'].mean()
        std_spread = df_pair['spread'].std()
        df_pair['zscore'] = (df_pair['spread'] - mean_spread) / std_spread
        last_zscore = df_pair['zscore'].iloc[-1]
        if last_zscore >1:
            print("Pair {} - {} - Zscore {:.2f} Sell sign".format(stock1, stock2, last_zscore))
        elif last_zscore < 1:
            print("Pair {} - {} - Zscore {:.2f} Buy sign".format(stock1, stock2, last_zscore))
        else:
            print("None")