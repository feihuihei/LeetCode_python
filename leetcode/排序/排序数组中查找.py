class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        arr = [-1,-1]
        if n == 0:
            return arr
        index = self.twoSearch(nums,target)
        if index == -1:
            return arr
        temp = index
        while nums[index - 1] == target:
            index -= 1
        while nums[temp + 1] == target:
            temp += 1
        return [index,temp]

    def twoSearch(self,nums,target):
        mid = len(nums)//2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            self.twoSearch(nums[mid+1:],target)
        else:
            self.twoSearch(nums[:mid], target)
        return -1

array = [5,7,7,8,8,10]
target = 6
obj = Solution()
print(obj.searchRange(array,target))