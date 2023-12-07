class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        length, count = len(strs[0]), len(strs)

        for i in range(length):  # 0,1,2,3,4,5
            answer = strs[0][i]  # f,l,o,w,e,r
            for j in range(1, count):  # 1,2
                if i >= len(strs[j]) or strs[j][i] != answer:
                    return strs[0][:i]
        return strs[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    strs = ["flower", "flow", "flo"]
    i = strs[0]
    j = i[0]
    k = strs[0][0]
    m = Solution().longestCommonPrefix(strs)
    print(m)
