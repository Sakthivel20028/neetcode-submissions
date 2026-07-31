class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit = 0
        minimum_element = 100
        for i in range(len(prices)):
            minimum_element = min(minimum_element,prices[i])
            maximum_profit = max(maximum_profit,prices[i]-minimum_element)
        return maximum_profit    
        