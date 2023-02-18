from strategies import mean_reversion, scalping,targetted_news, arbitrage, price_action
import pandas as pd
import numpy as np
import torch
from sklearn.model_selection import train_test_split
# from keras.models import Sequential
# from keras.layers import Dense


class MachneLearning:
    def __init__(self, tickers):
        self.tickers = tickers
        self.strategies = {
            0: mean_reversion, 
            1: arbitrage, 
            2: scalping, 
            3: price_action, 
            4: targetted_news
            }
        self.model6 = None

    
    def create_dataset(self):
        for i in self.tickers:
            df = pd.read_csv(f"repo/market/{i}.csv")
            df['return'] = np.log(df['close'] / df['close'].shift(1))
            df['volatility'] = df['return'].rolling(window=21).std() * np.sqrt(252)
            df['expected_return'] = df['return'].rolling(window=21).mean() * 252
            df['risk_factor'] = df['volatility'] / df['expected_return']
            df['strategy'] = -1

            df.loc[(df['risk_factor'] < 1) & (df['expected_return'] > 0), "strategy"] = 0 # "mean_reversion"
            df.loc[(df['risk_factor'] < 1) & (df['expected_return'] < 0), "strategy"] = 1 # "arbitrage"
            df.loc[(df['risk_factor'] > 1) & (df['expected_return'] > 0), "strategy"] = 2 # "scalping"
            df.loc[(df['close'] > df['close'].shift(1)) & (df['close'] > df['close'].shift(2)), "strategy"] = 3 # "price_action"
            df.loc[df['return'] > df['return'].rolling(window=21).std(), "strategy"] = 4 # "news_trading"
            df.fillna(0, inplace=True)
            df.to_csv(f"repo/ml_dataset/{i}_ml.csv")

    def train_models(self, symbol):
        # load data 
        
        df = pd.read_csv(f"repo/ml_dataset/{symbol}_ml.csv")
        df2 = pd.read_csv(f"repo/market/{symbol}.csv")
        X_train, X_test, y_train, y_test = train_test_split(df.drop("strategy", axis=1), df['strategy'], test_size=0.2, shuffle=False, random_state=0)
        # first dl model
        self.model6 = torch.nn.Sequential(
            torch.nn.Linear(X_train.shape[1], 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, len(self.strategies)),
            torch.nn.Softmax(dim=1),
        )
        criterion = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.SGD(self.model6.parameters(), lr=.01)
        for epoch in range(100):
            inputs = torch.tensor(X_train.values).float()
            target = torch.clamp(torch.tensor(y_train.values), min=0, max=len(self.strategies) - 1).long()
            optimizer.zero_grad()
            outputs = self.model6(inputs)
            loss = criterion(outputs, target)
            loss.backward()
            optimizer.step()
            
        prediction_6 = self.model6(torch.tensor(X_test.values).float()).argmax().item()
        print("predicted 6 value:", prediction_6)
        strategy = self.strategies[prediction_6]
        return prediction_6, strategy

        # strategy()
        
        
        
    def run(self, symbol):
        df = pd.read_csv(f"repo/market/{symbol}.csv")
        self.create_dataset()
        index, strategy = self.train_models(symbol)
        if index in [0,2,3]:
            return strategy(df)
        elif index == 1:
             return strategy(tickers=self.tickers)
        else:
             return strategy(df, ticker_2={"forex": self.tickers, "stock": self.tickers})