class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxP = 0 
        l, r = 0, 1 
    
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                MaxP = max(profit, MaxP)
            else:
                l = r
            r += 1
        return MaxP
        