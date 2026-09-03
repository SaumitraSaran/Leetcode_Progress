class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = prices[0]
        max_profit = 0
        for i in prices:
            if i < minimum:
                minimum = i
                
            profit = i - minimum

            if profit > max_profit:
                max_profit = profit
    
        return max_profit