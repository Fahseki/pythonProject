#  给定一个数组 prices ，它的第i个元素prices[i] 表示一支给定股票第 i 天的价格。
#  你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#  返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        #  从第一天买入，开始迭代
        i = 1
        price_buy = prices[0]

        while i < len(prices):
            #  先计算第i天卖出，是否能获得最大获利
            if profit < prices[i] - price_buy:
                profit = prices[i] - price_buy
            #  更新i之前出现过的最小值
            if price_buy > prices[i]:
                price_buy = prices[i]
            i += 1
        return profit

