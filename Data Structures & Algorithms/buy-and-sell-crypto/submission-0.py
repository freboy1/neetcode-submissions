class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow, fast, profit = 0, 0, 0

        while slow < len(prices) and fast < len(prices):
            if prices[slow] >= prices[fast]:
                slow = fast
            else:
                temp_profit = prices[fast] - prices[slow]

                if temp_profit > profit:
                    profit = temp_profit
        
            fast += 1

        return profit