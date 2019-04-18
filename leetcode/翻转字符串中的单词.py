class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        arr = s.split(" ")
        ss = " ".join(arr)
        return ss

s = "the sky is blue"
obj = Solution()
print(obj.reverseWords(s))