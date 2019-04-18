
class Solution():

    def quicksort(self,nums,start,end):
        if len(nums) <= 1 :
            return nums
        if start < end:
            index = self.partition(nums,start,end)

            self.quicksort(nums, start,index)
            self.quicksort(nums, index + 1, end)

    def partition(self,nums,start,end):
        i = start -1
        for j in range(start,end):
            if nums[j] <= nums[end]:
                i= i + 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1],nums[end] = nums[end],nums[i+1]
        return i

arr=[1,4,7,0,5,3,85,34,75,23,75]
obj = Solution()
obj.quicksort(arr,0,len(arr)-1)
print(arr)