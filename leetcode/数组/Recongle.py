import math
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        if m == 0:
            return M
        n = len(M[0])
        N = [[0]*n for i in range(m)]
        print(m,n,len(N),len(N[0]))
        if m == 1:
            for i in range(m):
                for j in  range(n):
                    if m == 1:
                        if n == 1:
                            return M
                        else:
                            if j == 0:
                                N[i][j] = math.floor((M[i][j] + M[i][j + 1])/2)
                            elif j == n - 1:
                                N[i][j] = math.floor((M[i][j] + M[i][j - 1])/2)
                            else:
                                N[i][j] = math.floor((M[i][j - 1] + M[i][j] + M[i][j + 1])/3)
        elif n == 1:
            for i in range(m):
                for j in range(n):
                    if n == 1:
                        if i == 0:
                            N[i][j] = math.floor((M[i][j] + M[i + 1][j])/2)
                        elif i == m - 1:
                            N[i][j] = math.floor((M[i][j] + M[i - 1][j])/2)
                        else:
                            N[i][j] = math.floor((M[i - 1][j] + M[i][j] + M[i + 1][j])/2)
        else:
            for i in range(m):
                for j in  range(n):
                    if i != 0 and i != m-1 and j != 0 and j != n-1:
                        N[i][j] = math.floor((M[i-1][j-1] + M[i-1][j] + M[i-1][j+1] +M[i][j-1] + M[i][j]+M[i][j+1]+M[i+1][j-1]+M[i+1][j]+M[i+1][j+1])/9)
                    elif i == 0:
                        if j == 0 or j == n -1:
                            if j == 0:
                                N[i][j] = math.floor((M[i][j]+M[i][j+1]+M[i+1][j]+M[i+1][j+1])/4)
                            else:
                                N[i][j] = math.floor((M[i][j-1]+M[i][j]+M[i+1][j]+M[i+1][j-1])/4)
                        else:
                            N[i][j] = math.floor((M[i][j-1]+M[i+1][j-1]+M[i][j]+M[i][j+1]+M[i+1][j]+M[i+1][j+1])/6)
                    else:
                        if j == 0 or j == n -1:
                            if j == 0:
                                N[i][j] = math.floor((M[i][j]+M[i][j+1]+M[i-1][j]+M[i-1][j+1])/4)
                            else:
                                N[i][j] = math.floor((M[i][j-1]+M[i][j]+M[i-1][j]+M[i-1][j-1])/4)
                        else:
                            N[i][j] = math.floor((M[i][j-1]+M[i-1][j-1]+M[i][j]+M[i][j+1]+M[i-1][j]+M[i-1][j+1])/6)
        return N
#nums = [[1,1,1],[1,0,1],[1,1,1]]
nums = [[1]]
s = Solution()
print(s.imageSmoother(nums))