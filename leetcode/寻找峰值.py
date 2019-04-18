class Solution(object):
    #找到数组中的峰值
    def findPeakElement(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        maxnum = nums[0]
        for i in range(n):
            if nums[i] > maxnum:
                maxnum = nums[i]
        return nums.index(maxnum)