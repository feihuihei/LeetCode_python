class Solution(object):
    #给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr=[]
        for i in s:
            if i.isalnum():
              arr.append(i.lower())
        if arr[::] == arr[::-1]:
            return True
        return False
    #反转元音字母
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        i =0
        j = n-1
        array = [i for i in s]
        arr = ["a","e","i","o","u","A","E","I","O","U"]
        while i < j:
            if not array[i] in arr:
                i+=1
                continue
            if not array[j] in arr:
                j-=1
                continue
            array[i],array[j] = array[j],array[i]
            i += 1
            j -= 1
        return "".join(array)
    #盛最多水的容器
    def maxArea(self, height):
        n = len(height)
        if n <= 1:
            return 0
        i = 0
        j = n-1
        maxarea = 0
        while i<j:
            area = min(height[i],height[j])*(j-i)
            maxarea = max(maxarea,area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxarea
    #长度最小的子数组给定一个含有 n 个正整数的数组和一个正整数 s ，
    # 找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        if n == 0:
            return 0
        i = 0
        j = 0
        minlen = n+1
        sum = nums[0]
        while i <= j and j <= n - 1:
            if sum == s:
                minlen = min(minlen,j-i+1)
            if sum > s:
                sum -= nums[i]
                i += 1
            else:
                j += 1
                if j >= n:
                    break
                sum += nums[j]
        return minlen if minlen < n+1 else 0
    #颜色分类
    def sortColors(self, nums):
        n = len(nums)
        if n == 0:
            return
        start = -1
        i = 0
        end = n - 1
        while i <= end:
            if nums[i] == 1:
                i+=1
            elif nums[i] == 2:
                nums[end],nums[i] = nums[i],nums[end]
                end -= 1
            else:
                start += 1
                nums[start] , nums[i] = nums[i] ,nums[start]
                i += 1

obj = Solution()
s = "aA"
height = [1,8,6,2,5,4,8,3,7]
nums = [2,0,2,1,1,0]
print(obj.sortColors(nums))
print(nums)