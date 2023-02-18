

def get_strats(df):
    strategies = {0: "mean_reversion", 1: "arbitrage", 2: "scalping", 3: 'new_trading'}
    volatility = ""
    expected_return = ""
    risk_factor = ""
    trend = ""
    momentum = ""

    if risk_factor < 0.1 and momentum < 30:
        return strategies[0]
    elif expected_return > 5 and volatility < 10:
        return strategies[1]

    elif volatility > 10:
        return strategies[2]
    elif trend == 1 and momentum > 70:
        return strategies[3]