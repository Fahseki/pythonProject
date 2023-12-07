class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        times = 1
        a = b = 0
        while i <= n:
            a = b    # n-2对应值赋给a
            b = times     # n-1对应值赋给b
            times = a + b  # 计算当前n对应值，就是(n-1)(n-2)两个值相加
            i += 1
        return times

