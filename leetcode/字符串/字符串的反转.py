class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        return s[::-1]

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        ss = s.split(' ')
        ret = ""
        for i in range(len(ss)):
            if i != 0:
                ret = ret+' '+ss[i][::-1]
            else:
                ret = ''+ss[i][::-1]
        return ret

obj = Solution()
s = "Let's take LeetCode contest"
print(obj.reverseWords(s))