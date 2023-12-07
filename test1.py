from functools import reduce
from collections import defaultdict

if __name__ == '__main__':

    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    s = 'MCMXCIV'
    # print(s[::-1])

    NowValue = 1
    answer = 0
    for i in s[::-1]:
        value = SYMBOL_VALUES[i]
        if value >= NowValue:
            answer += value
            NowValue = value
        else:
            answer -= value
        # print(answer, value, NowValue)

    dig = [1, 2, 3]
    # print([0]+dig)

    sum1 = ""
    sum1 += "1"
    # print(sum1)
    sum1 += "0"
    # print(sum1)

    numRows = 'Python'
    #  print(numRows.lower())
    #  print(numRows.upper())
    #  print(numRows.capitalize())
    #  print(numRows.title())
    sentences = ['The Deep Learning textbook is a resource intended to help students and practitioners enter '
                 'the field of machine learning in general and deep learning in particular. ']
    word_count = reduce(lambda a, x: a + x.count("learning"), sentences, 0)
    # print(word_count)

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    index = {element: i for i, element in enumerate(inorder)}
    inorder_root = index[preorder[0]]
    #  print(index[7])

    """
    n = '1001'
    m = int(n, 2)     # 二进制转化十进制  =9
    n1 = 13
    m1 = bin(n1)       # 十进制转化二进制  =0b1101
    print(m1)
    """


    def n2(n):
        result = 0
        while n > 0:
            result += (n % 10) ** 2
            n = n // 10
        return result


    def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        res_history = []
        res = n
        while res > 0:

            if res == 1:
                return True
            if res in res_history:
                return False
            res_history.append(res)
            print(res_history)
            res = n2(res)
            print(res)
    n = 19
    print(isHappy(n))


