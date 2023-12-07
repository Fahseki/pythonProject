# 颠倒给定的 32 位无符号整数的二进制位。

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = n & 1      # 获得末尾的数字
        for i in range(31):
            n >>= 1            # 循环右移1，去除末尾数字
            ans <<= 1          # 左移1，再加上再次获取的n最后一位
            ans += (n & 1)
        return ans

    '''解答一
    n = '00000010100101000001111010011100'
    m = str(n)
    print(n, m)
    index = {i: element for i, element in enumerate(m)}
    ans = 0
    for i in index:
        ans += (2 ** i) * int(index[i])
    print(ans)
    '''
    '''解答二
    n = 0b00000010100101000001111010011100
    ans = n & 1
    for i in range(31):
        n >>= 1
        ans <<= 1
        ans += (n & 1)
    print(ans)
    '''
    '''解答三
    int("0b" + ("0" * 32 + bin(n)[2:])[-32:][::-1], 2)
    '''