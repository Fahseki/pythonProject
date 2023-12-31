#  如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
# 字母和数字都属于字母数字字符。
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 多行
        s1 = ''
        for t in s:
            if t.isalnum():          # 判断是不是字母数字
                s1 += t.lower()      # 转小写
        if s1 == s1[::-1]:
            return True
        else:
            return False

        # 一行
        # s1 = ''.join(ch.lower() for ch in s if ch.isalnum())
        # return s1 == s1[::-1]

