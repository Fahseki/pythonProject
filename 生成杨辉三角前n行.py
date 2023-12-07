class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list_big = list()
        for i in range(numRows):
            list_small = list()
            for j in range(0, i+1):
                if j == 0 or j == i:
                    list_small.append(1)
                else:
                    list_small.append(list_big[i-1][j] + list_big[i-1][j-1])
            list_big.append(list_small)
        return list_big

