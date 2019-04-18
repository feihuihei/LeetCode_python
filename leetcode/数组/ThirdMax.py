import sys
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
        else:
            print()
            a = -sys.maxsize
            b = -sys.maxsize
            c = -sys.maxsize
            for i in range(n):
                if nums[i] > a:
                    c = b
                    b = a
                    a =nums[i]
                elif nums[i] > b and nums[i] < a:
                    c = b
                    b = nums[i]
                elif nums[i] > c and nums[i] < b:
                    c = nums[i]
            return c
        return 0
nums = [3,2,1]
s = Solution()
print(s.thirdMax(nums))