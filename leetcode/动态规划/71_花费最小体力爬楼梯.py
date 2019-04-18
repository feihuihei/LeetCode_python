class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n <= 1:
            return 0
        cost.append(0)
        dp = [0]*(n+1)
        dp[0] = cost[0]
        dp[1] = min(cost[0]+cost[1],cost[1])
        for i in range(2,n+1):
            dp[i] = min(dp[i-1],dp[i-2])+cost[i]
        return dp[n]

obj = Solution()
cost =[0,1,1,0]
print(obj.minCostClimbingStairs(cost))