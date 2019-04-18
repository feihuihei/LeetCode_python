class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n ==0 or s[0] == "0":
            return 0

        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(1,len(dp)):
            if s[i-1] =="0":
                dp[i] =0
            else:
                dp[i] = dp[i-1]
            if i>1 and (s[i-2] =="1" or (s[i-2] =="2" and s[i-1] <="6")):
                dp[i] += dp[i-2]
        return dp[n]


obj = Solution()
s = "1212"
print(obj.numDecodings(s))