# You are given an array prices where prices[i] is
# the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.


# Approach:
# - Initialize two variables: min_price to first price and max_profit to 0
# - Iterate through each price in the prices array
#   - Update min_price if the current price is lower than min_price
#   - Calculate potential profit by subtracting min_price from current price
#   - Update max_profit if potential profit is greater than max_profit
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize variables
        min_buy_price = prices[0] # Minimum price to buy the stock
        max_profit = 0            # Maximum profit achievable
        # Iterate through each price
        for price in prices:
            # Update min_buy_price if current price is lower
            if price < min_buy_price:
                min_buy_price = price
            # Update max_profit if potential profit is greater
            if price - min_buy_price > max_profit:
                max_profit = price - min_buy_price
        # Return the maximum profit achievable
        return max_profit
