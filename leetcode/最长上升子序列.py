class Solution:

    def getLongestSub(self,nums):
        if len(nums) <= 0:
            return 0
        arr = [ 1 for i in range(len(nums))]

        for i in range( 1, len(nums)):
            j = i - 1
            while j >= 0:
                if nums[i] > nums[j]:
                    arr[i] = max(arr[i],arr[j] + 1)
                j -= 1
        intmax = 0
        print(arr)
        for i in range(len(arr)):
            if arr[i] > intmax:
                intmax = arr[i]
        return intmax

obj = Solution()
nums = [2,5,3,4,1,7,6]
print(obj.getLongestSub(nums))