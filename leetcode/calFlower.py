class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        m = len(flowerbed)
        index = 0
        sum = 0
        for i in range(m):
            if flowerbed[i] == 1:
                continue
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == m-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n-=1
        if n<= 0:
            return True
        else:
            return False
