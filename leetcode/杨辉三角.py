class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        listAll = []
        if numRows == 0:
            return listAll
        else:
            list_1 = [1]
            listAll.append(list_1)
            index = 2
            while index <= numRows:
                l_list = listAll[-1]

