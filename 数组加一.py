class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                # 当前位不是9，就可以+1
                return digits
            else:
                digits[i] = 0
                i -= 1
        # 循环结束，说明现在数组内全是0
        digits = [1] + digits
        return digits
