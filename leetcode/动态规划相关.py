class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # if not triangle:
        #     return 0
        # for i in range(len(triangle) - 2, -1, -1):
        #     for j in range(len(triangle[i]) - 1, -1, -1):
        #         triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
        # return triangle[0][0]
        if not triangle:
            return 0
        n = len(triangle)
        dp = [ [ 0 for i in range(n+1) ] for j in range(n+1) ]

        for i in range(n -1,-1,-1):
            arr = triangle[i]
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i+1][j+1],dp[i+1][j]) + arr[j]
        print(dp)
        return dp[0][0]



obj = Solution()
nums = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(obj.minimumTotal(nums))