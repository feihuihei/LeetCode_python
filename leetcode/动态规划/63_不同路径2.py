class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        if n == 0:
            return 0
        m = len(obstacleGrid[0])
        if m == 0:
            return 0
        dp = [[0 for col in range(m)] for row in range(n)]

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i ==0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j ==0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]
obj = Solution()
arr = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(obj.uniquePathsWithObstacles(arr))