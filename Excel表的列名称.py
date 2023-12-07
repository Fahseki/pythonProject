# 给一个数字，返回对应的列名：
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
# AZ -> 52
# ...
# ZZ -> 702
# AAA -> 703
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        name = ""
        while columnNumber > 0:
            number2 = (columnNumber - 1) % 26  # 存一下余数
            columnNumber = (columnNumber - 1) // 26  # 存一下整数部分
            name += chr(number2 + ord("A"))  # 根据最后一个余数部分，得到最后的字符
        return name[::-1]

