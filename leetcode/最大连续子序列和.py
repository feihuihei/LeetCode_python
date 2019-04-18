import sys
class Solution():

    def maxsub(self,nums):
        if len(nums) <= 0:
            return 0
        maxsub = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum < 0:
                sum = 0
            else:
                if sum > maxsub:
                    maxsub = sum
        return  maxsub

obj =  Solution()
nums = [-2 , 6, -1, 5, 4, -7, 2, 5]
print(obj.maxsub(nums))
