from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # TODO - you fill in here.
    f_small=float('inf')
    b_max=0
    f_max_profit=0
    b_max_profit=0
    max_profit=0
    f_max_profits=[]
    for i in range(len(prices)):
        if prices[i] < f_small:
            f_small=prices[i]
        if prices[i]-f_small >= f_max_profit:
            f_max_profit=prices[i]-f_small
            f_max_profits.append(f_max_profit)
        else:
            f_max_profits.append(f_max_profit)
    b_max_profits=[0]*len(prices)
    for i in reversed(range(len(prices))):
        if prices[i]>b_max:
            b_max=prices[i]
        if b_max-prices[i]>=b_max_profit:
            b_max_profit=b_max - prices[i]
            b_max_profits[i] = b_max_profit
        else:
            b_max_profits[i]=b_max_profit
    for i in range(len(b_max_profits)):
        if b_max_profits[i]+f_max_profits[i]>max_profit:
            max_profit=b_max_profits[i]+f_max_profits[i]
    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
