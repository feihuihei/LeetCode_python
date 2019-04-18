import math
class Solution:
    #给定一个数组 [5,6,7,8,9,10,1,2,3,4], 数组存在断点，端点左侧是有序递增的，右侧也是有序递增的，且左侧子元素均大于右侧子元素
    def findLargestNumbers(self, nums):
        n = len(nums)
        if n == 0 :
            return -1
        start, end = 0, n-1
        while start <= end:
            index = math.ceil( (start+end) / 2)
            if nums[index] > nums[start] and nums[index] > nums[end]:
                start = index + 1
            else:
                end = index - 1
        nn = math.ceil(n/2)
        print(start,end)
        return  start

obj = Solution()
nums1 = [5,6,7,8,9,10,1,2,3,4]
nums = [7,8,9,10,1,2,3,4,5,6]
print(obj.findLargestNumbers(nums))


