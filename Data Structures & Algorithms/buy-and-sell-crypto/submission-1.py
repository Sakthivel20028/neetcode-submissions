class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit = prices[j] - prices[i]
                maximum_profit = max(profit,maximum_profit)
        return maximum_profit    
        