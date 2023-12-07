# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」 定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

class Solution(object):

    def n2(self, n):
        result = 0
        while n > 0:
            result += (n % 10) ** 2
            n = n//10
            # n, result = divmod(n, 10)  使用divmod函数，获取商和余数，等效于（(a // b, a % b)）
            # result += result ** 2
        return result

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res_history = []  # 其实非快乐数，最终都会进入这个循环 [4, 16, 37, 58, 89, 145, 42, 20]
        res = n
        while res > 0:

            if res == 1:
                return True
            if res in res_history:
                return False
            res_history.append(res)
            res = self.n2(res)
