# 给定一个大小为 n 的数组nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = None
        times = 0

        for num in nums:
            if times == 0:
                a = num
                times = 1
            else:
                if a == num:
                    times += 1
                else:
                    times -= 1
        return a
