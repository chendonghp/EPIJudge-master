from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    # return 0.0
    # # brute force
    # max_profit = 0
    # for i in range(1,len(prices)):
    #     for j in range(i):
    #         profit=prices[i]-prices[j]
    #         if max_profit<profit:
    #             max_profit=profit
    # return max_profit

    max_profit=0
    small=0
    max_=0
    for i in range(1,len(prices)):
        if prices[i] < prices[small]:
            small=i
            max_ = max(max_, i)
        if prices[i] > prices[max_]:
            max_= i
        profit=prices[i]-prices[small]
        if profit > max_profit:
            max_profit = profit
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
