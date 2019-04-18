import sys
class Solution():

    def gupiao(self,nums):
        if len(nums) <= 0:
            return  0
        profit = 0
        minprice = sys.maxsize
        for i in range(len(nums)):
            if nums[i] < minprice :
                minprice = nums[i]
            elif nums[i] - minprice > profit:
                profit = nums[i] - minprice
        return profit

obj = Solution()
prices = [7,5,4,2,1,6]
print(obj.gupiao(prices))