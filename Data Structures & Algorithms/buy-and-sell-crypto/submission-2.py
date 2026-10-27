class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Philosophy: shift pointers if you lose profit
        # Record max profit if profited, then shift pointers
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else: # Lower than the left pointer, so shift over
                l = r
            r += 1

        return maxProfit