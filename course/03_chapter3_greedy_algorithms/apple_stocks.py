"""
Problem: Write an efficient function that takes stock_prices and returns the
best profit I could have made from one purchase and one sale of one share of
Apple stock yesterday.

Constraint: You have to buy before you can sell
"""

def get_max_profit(stock_prices):
    current_spread = 0
    for bottom in range(len(stock_prices)):
        later = stock_prices[bottom:]
        print(later)
        for top in later:
            if top - stock_prices[bottom] > current_spread:
                current_spread = top - stock_prices[bottom]
    return current_spread


stock_prices = [10, 7, 5, 8, 11, 9]
print(get_max_profit(stock_prices))
