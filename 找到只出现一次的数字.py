
from functools import reduce


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = []
        for i in nums:
            if i in j:
                del j[j.index(i)]
            else:
                j.append(i)
        return j[0]

        #  方法二：使用异或运算 a^b^a = a^a^b = 0^b = b
        #  reduce(),表示对数组内每个均执行操作
        #  return reduce(lambda x, y: x ^ y, nums)

        #  reduce()范例
        #  sentences = ['The Deep Learning textbook is a resource intended to help students and practitioners enter
        #  'the field of machine learning in general and deep learning in particular. ']
        #  word_count = reduce(lambda a, x: a + x.count("learning"), sentences, 0)
        #  print(word_count)
