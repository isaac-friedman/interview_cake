"""
Problem: Write an efficient function that takes stock_prices and returns the
best profit I could have made from one purchase and one sale of one share of
Apple stock yesterday.

Constraint: You have to buy before you can sell
"""

def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1]-stock_prices[0]
    for price in stock_prices:
        if (price - min_price) > max_profit:
            max_profit = (price - min_price)
        if price < min_price:
            min_price = price
    return max_profit


stock_prices = [10, 7, 5, 8, 11, 9]
print(get_max_profit(stock_prices))
