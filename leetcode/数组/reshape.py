class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if nums == None:
            return nums
        n = len(nums)
        m = len(nums[0])
        if n*m == r*c:
            arr = []
            res = []
            index = 0
            for i in range(n):
                for j in range(m):
                    arr.append(nums[i][j])
            print(arr)
            for i in range(r):
                temp = []
                for j in range(c):
                    temp.append(arr[index])
                    index += 1
                res.append(temp)
            return res
        else:
            return nums

nums = [[1,2],[3,4]]
s = Solution()
print(s.matrixReshape(nums,4,1))