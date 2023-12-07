class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        list_big = list()
        for i in range(rowIndex+1):
            list_small = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    list_small.append(1)
                else:
                    list_small.append(list_big[i-1][j] + list_big[i-1][j-1])
            list_big.append(list_small)
        return list_big[rowIndex-1]

