class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        answer = strs[0]
        for i in range(1, len(strs)):
            answer = self.LCP(answer, strs[i])
            if len(answer) == 0:
                break
        return answer

    def LCP(self, str1, str2):
        Length, i = min(len(str1), len(str2)), 0
        while i < Length and str1[index] == str2[index]:
            i += 1
        return str1[:index]