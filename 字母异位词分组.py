# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = defaultdict(list)   # 初始化一个哈希表，其值是一个列表

        for st in strs:
            key = "".join(sorted(st))           # 将排序后的值作为 键
            mp[key].append(st)             # 相同键的字符，就放到同一个键的值里

        return list(mp.values())
