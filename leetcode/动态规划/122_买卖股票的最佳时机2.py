class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        profile = 0
        high = prices[0]
        n = len(prices)
        for i in range(1,n):
            if(prices[i] > prices[i-1]):
                profile += prices[i] - prices[i-1]
        return profile