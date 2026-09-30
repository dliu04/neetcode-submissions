class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # You cannot turn back time
        
        # Create a maxProfit variable to store the number
        maxProfit = 0

        # Double for loop:
        # Iterate and see if the j number is greater than current
        # If it is greater than current, find difference
            # If difference > maxProfit variable, store in maxProfit

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] > prices[i]:
                    difference = prices[j] - prices[i]
                    if difference > maxProfit:
                        maxProfit = difference

        # return maxProfit
        return maxProfit