class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        profile = 0
        res = 0
        n = len(prices)
        for i in range(1,n ):
            profile += prices[i] - prices[i-1]
            res = max(res , profile)
            profile = max(0,profile)
        return res

prices = [7,1,5,3,6,4]
s = Solution()
res = s.maxProfit(prices)
print(res)