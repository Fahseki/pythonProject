class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        sum2 = ""
        # 从最后一位开始循环，保存字符和进位
        while i >= 0 or j >= 0:
            # 判断是否有字符被循环完
            a1 = b1 = 0
            if i < 0:
                a1 = 0
            elif i >= 0:
                a1 = int(a[i])
            if j < 0:
                b1 = 0
            elif j >= 0:
                b1 = int(b[j])
            # 计算每一位的和
            sum1 = a1 + b1 + carry
            if sum1 == 0:
                sum2 += "0"
                carry = 0
            elif sum1 == 1:
                sum2 += "1"
                carry = 0
            elif sum1 == 2:
                sum2 += "0"
                carry = 1
            elif sum1 == 3:
                sum2 += "1"
                carry = 1
            i -= 1
            j -= 1

        # 循环完后，还有一个进位，加上
        if carry == 1:
            sum2 += "1"
        # 反转字符，返回结果
        sum = sum2[::-1]
        return sum
