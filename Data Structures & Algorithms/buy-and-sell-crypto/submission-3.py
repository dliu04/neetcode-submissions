class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        # Buy low, sell high
        # You only ever shift the left pointer (low) if right pointer
        # is somehow lower than left pointer

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            elif prices[r] < prices[l]:
                l = r
            r += 1

        return maxProfit