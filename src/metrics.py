import numpy as np

def performance_metrics(returns):
    sharpe = np.sqrt(252) * returns.mean() / returns.std()
    cumulative = (1 + returns).cumprod()
    max_drawdown = (cumulative / cumulative.cummax() - 1).min()

    return {
        'Sharpe Ratio': sharpe,
        'Cumulative Return': cumulative.iloc[-1] - 1,
        'Max Drawdown': max_drawdown
    }