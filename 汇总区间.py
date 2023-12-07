# 给定一个  无重复元素 的 有序 整数数组 nums 。
#
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
#
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
#
# "a->b" ，如果 a != b
# "a" ，如果 a == b
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        res = []
        while i < len(nums):
            j = 0
            if nums[i] == nums[i+1]:
                j = i
                i += 1
            else:
                if i == j:
                    res += "nums[i]"
                else:
                    res += "nums[j]" + "-->" + "nums[i]"
        return res