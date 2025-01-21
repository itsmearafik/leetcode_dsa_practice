from typing import List


def maxProfit(prices: List[int]) -> int:
    # initialize variables for price and profit 
    buy_price = prices[0]
    profit = 0

    # loop through prices whiles calculating profits
    for p in prices[1:]:
        if buy_price > p:
            buy_price = p
        
        profit = max(profit, p - buy_price)
    # return price with max profit 
    return profit 
price = [7,1,5,3,6,4]
print(maxProfit(price))