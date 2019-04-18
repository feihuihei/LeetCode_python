class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxpos = 0
        for i in range(len(nums) - 1):
            maxpos = max(maxpos,i+nums[i])
            if maxpos == i:
                return False
        return True