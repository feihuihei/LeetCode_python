class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 and n == 0:
            return 0

        dp = [[1 for col in range(m)] for row in range(n) ]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

obj = Solution()
m = 7
n = 3
print(obj.uniquePaths(m,n))