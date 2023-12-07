# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        p_h = 0
        p_n = 0
        while p_h < len(haystack):
            if haystack[p_h] == needle[p_n]:
                if haystack[p_h:p_h + len(needle)] == needle:
                    return p_h
            p_h += 1
        return -1
