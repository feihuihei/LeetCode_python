class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [1 for i in range(n+1)]
        for i in range(2,n+1):
            temp = 0
            for j in range(i):
                temp += dp[j]*dp[i-j-1]
            dp[i] = temp
        return dp[n]
obj = Solution()
print(obj.numTrees(4))