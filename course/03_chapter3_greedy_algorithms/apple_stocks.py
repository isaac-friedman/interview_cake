"""
Problem: Write an efficient function that takes stock_prices and returns the
best profit I could have made from one purchase and one sale of one share of
Apple stock yesterday.
"""

def get_max_profit(stock_prices):
    # If we were to allow shorting, buying on margin and all of the usual financial shenanigans
    return(max(stock_prices) - min(stock_prices))

stock_prices = [10, 7, 5, 8, 11, 9]
get_max_profit(stock_prices)
