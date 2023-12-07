#  给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        index = {i: element for i, element in enumerate(columnTitle[::-1])}
        ans = 0
        for i in index:
            ans += (26 ** i) * ((ord(index[i]) - ord("A")) + 1)
        return ans
